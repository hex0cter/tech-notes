#!/usr/bin/env python3
"""Tests for seo.py (run with: python3 -m unittest test_seo.py)."""

import os
import tempfile
import unittest
import xml.etree.ElementTree as ET
from os.path import join

import seo

SITE = "https://carnet.danielhan.dev/"

PAGE = """<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title} - Tech notes</title>
    </head>
    <body>{title}</body>
</html>
"""


class SeoTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.book = self.tmp.name
        self.pages = {
            "index.html": "Welcome",
            "rfc/index.html": "Rfc",
            "rfc/sip/index.html": "Sip",
            "rfc/sip/sip-category.html": "Sip category",
            "print.html": "Print",
            "toc.html": "Toc",
            "404.html": "Not found",
        }
        for path, title in self.pages.items():
            os.makedirs(join(self.book, os.path.dirname(path)), exist_ok=True)
            with open(join(self.book, path), "w") as f:
                f.write(PAGE.format(title=title))
        # A non-HTML asset must never appear in the sitemap.
        with open(join(self.book, "book.js"), "w") as f:
            f.write("// js")

    def tearDown(self):
        self.tmp.cleanup()

    def test_page_url_uses_clean_directory_form(self):
        self.assertEqual(seo.page_url(SITE, "index.html"), SITE)
        self.assertEqual(seo.page_url(SITE, "rfc/sip/index.html"), SITE + "rfc/sip/")
        self.assertEqual(
            seo.page_url(SITE, "rfc/sip/sip-category.html"),
            SITE + "rfc/sip/sip-category.html",
        )

    def test_indexable_pages_excludes_mdbook_helper_pages(self):
        pages = seo.indexable_pages(self.book)
        self.assertEqual(
            sorted(pages),
            ["index.html", "rfc/index.html", "rfc/sip/index.html", "rfc/sip/sip-category.html"],
        )

    def test_sitemap_lists_each_indexable_page_once(self):
        seo.write_sitemap(self.book, SITE)
        tree = ET.parse(join(self.book, "sitemap.xml"))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text for el in tree.getroot().findall("sm:url/sm:loc", ns)]
        self.assertEqual(
            locs,
            [
                SITE,
                SITE + "rfc/",
                SITE + "rfc/sip/",
                SITE + "rfc/sip/sip-category.html",
            ],
        )
        self.assertEqual(len(locs), len(set(locs)))

    def test_robots_points_at_sitemap(self):
        seo.write_robots(self.book, SITE)
        with open(join(self.book, "robots.txt")) as f:
            robots = f.read()
        self.assertIn("User-agent: *", robots)
        self.assertIn("Allow: /", robots)
        self.assertIn("Sitemap: " + SITE + "sitemap.xml", robots)

    def test_canonical_added_to_indexable_pages_only(self):
        seo.add_canonical_links(self.book, SITE)
        with open(join(self.book, "rfc/sip/index.html")) as f:
            html = f.read()
        self.assertEqual(html.count('<link rel="canonical"'), 1)
        self.assertIn('<link rel="canonical" href="' + SITE + 'rfc/sip/">', html)
        # It must land inside <head>, before </head>.
        self.assertLess(html.index('<link rel="canonical"'), html.index("</head>"))
        for helper in ("print.html", "toc.html", "404.html"):
            with open(join(self.book, helper)) as f:
                self.assertNotIn("canonical", f.read())

    def test_canonical_is_idempotent(self):
        seo.add_canonical_links(self.book, SITE)
        seo.add_canonical_links(self.book, SITE)
        with open(join(self.book, "index.html")) as f:
            self.assertEqual(f.read().count('rel="canonical"'), 1)

    def test_main_writes_everything(self):
        seo.main([self.book, SITE])
        self.assertTrue(os.path.exists(join(self.book, "sitemap.xml")))
        self.assertTrue(os.path.exists(join(self.book, "robots.txt")))
        with open(join(self.book, "index.html")) as f:
            self.assertIn('rel="canonical"', f.read())


if __name__ == "__main__":
    unittest.main()
