#!/usr/bin/env python3
"""Post-build SEO step for the mdBook output.

Usage: python3 seo.py [BOOK_DIR] [SITE_URL]

Given the built book directory it:
  * writes BOOK_DIR/sitemap.xml listing every indexable page,
  * writes BOOK_DIR/robots.txt pointing at the sitemap,
  * inserts <link rel="canonical"> into the <head> of every indexable page.

The sitemap and the canonical tags use the same, clean URL form:
  index.html            -> https://site/
  rfc/sip/index.html    -> https://site/rfc/sip/
  rfc/sip/sip-timers.html -> https://site/rfc/sip/sip-timers.html
so search engines see one preferred address per page, even though the
sidebar mdBook generates links to the "index.html" form.

mdBook helper pages (print.html, toc.html, 404.html) are left alone:
mdBook already marks the first two noindex, and 404.html is not a page.
Only the Python standard library is used.
"""

import os
import re
import sys
from os.path import join, relpath
from xml.sax.saxutils import escape

DEFAULT_BOOK_DIR = "book"
DEFAULT_SITE_URL = "https://carnet.danielhan.dev/"

# Files mdBook writes that must not be listed or canonicalised.
HELPER_PAGES = {"print.html", "toc.html", "404.html"}

_CANONICAL_RE = re.compile(r'<link rel="canonical"[^>]*>\s*', re.IGNORECASE)


def page_url(site_url, page_path):
    """Map a path relative to the book dir to its public URL."""
    if page_path == "index.html":
        return site_url
    if page_path.endswith("/index.html"):
        return site_url + page_path[: -len("index.html")]
    return site_url + page_path


def indexable_pages(book_dir):
    """Return sorted, book-relative paths of every HTML page worth indexing."""
    pages = []
    for root, _dirs, files in os.walk(book_dir):
        for name in files:
            if not name.endswith(".html"):
                continue
            rel = relpath(join(root, name), book_dir).replace(os.sep, "/")
            if rel in HELPER_PAGES:
                continue
            pages.append(rel)
    return sorted(pages)


def write_sitemap(book_dir, site_url):
    urls = [page_url(site_url, p) for p in indexable_pages(book_dir)]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        lines.append("  <url><loc>%s</loc></url>" % escape(url))
    lines.append("</urlset>")
    with open(join(book_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return urls


def write_robots(book_dir, site_url):
    with open(join(book_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % site_url)


def add_canonical_links(book_dir, site_url):
    """Insert one canonical <link> before </head> in each indexable page."""
    count = 0
    for page in indexable_pages(book_dir):
        path = join(book_dir, page)
        with open(path, encoding="utf-8") as f:
            html = f.read()
        html = _CANONICAL_RE.sub("", html)  # idempotent on re-runs
        tag = '<link rel="canonical" href="%s">\n' % escape(page_url(site_url, page), {'"': "&quot;"})
        new_html, n = re.subn(r"</head>", lambda m: tag + m.group(0), html, count=1, flags=re.IGNORECASE)
        if n != 1:
            print("seo.py: no </head> in %s, skipped" % page, file=sys.stderr)
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        count += 1
    return count


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    book_dir = argv[0] if len(argv) > 0 else DEFAULT_BOOK_DIR
    site_url = argv[1] if len(argv) > 1 else DEFAULT_SITE_URL
    if not site_url.endswith("/"):
        site_url += "/"
    if not os.path.isdir(book_dir):
        sys.exit("seo.py: book directory %r not found (run `mdbook build` first)" % book_dir)

    urls = write_sitemap(book_dir, site_url)
    write_robots(book_dir, site_url)
    canonicals = add_canonical_links(book_dir, site_url)
    print("seo.py: sitemap.xml with %d URLs, robots.txt, %d canonical tags" % (len(urls), canonicals))


if __name__ == "__main__":
    main()
