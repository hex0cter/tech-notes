# Set transparency in top panel of GNOME Shell

```
/usr/share/gnome-shell/theme/gnome-shell.css
```

```diff
/usr/share/gnome-shell/theme $ diff -u gnome-shell.css.orig gnome-shell.css

--- gnome-shell.css.orig 2012-02-04 21:29:55.192625986 +0100

+++ gnome-shell.css 2012-02-04 21:56:53.959439312 +0100

@@ -277,8 +277,9 @@

#panel {

color: #ffffff;

- background-color: black;

- border-image: url("panel-border.svg") 1;

+ /* background-color: black; */

+ background-color: rgba(0,0,0,0.6);

+ /* border-image: url("panel-border.svg") 1; */

font-size: 10.5pt;

font-weight: bold;

height: 1.86em;
```
