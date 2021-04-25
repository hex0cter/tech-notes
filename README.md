# Technical notes

This site was converted from [https://sites.google.com/site/xiangyangsite](https://sites.google.com/site/xiangyangsite) before Google forced it to be migrated to their new site template (which doesn't have many features the old one had, such as subpage listing, page attachment, etc.)

## How to generate the mark down files:

Install [mercury-parser](https://github.com/postlight/mercury-parser) with
```
npm -g install @postlight/mercury-parser
```

Download a mark down converter called [reader](https://github.com/zyocum/reader).

Assume in the `reader` repository, run
```
mercury-parser https://example.com/path | ./reader.py  -f md - > path.md
```
