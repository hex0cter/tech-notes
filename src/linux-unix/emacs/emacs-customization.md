# Emacs customization (example)

[Download `espresso.el`](http://download.savannah.gnu.org/releases-noredirect/espresso/espresso.el) and put it somewhere in your `load-path`. Then add the following to your `.emacs`:

```
          (autoload #'espresso-mode "espresso" "Start espresso-mode" t)
          (add-to-list 'auto-mode-alist '("\\.js$" . espresso-mode))
          (add-to-list 'auto-mode-alist '("\\.json$" . espresso-mode))
```
