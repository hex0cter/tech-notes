
date: None  
author(s): None  

# [Gnome 桌面环境中 Metacity 窗口管理器设置窗口按钮的位置 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/gnome/gnome_buttons)

通常的Windows,Gnome,KDE等中的窗口总是将最小化minimize／最大化maximize／关闭close等按钮放置于窗口标题栏的右边，而Mac风格的主题习惯将他们放在标题栏的左边。Gnome桌面环境中的默认窗口管理器是Metacity，通过对他的简单设置就可以实现Mac中窗口标题栏按钮的放置方式。

以Ubuntu为例，点击主菜单的“应用程序”——“系统工具”——“配置编辑器”打开“配置编辑器”（如果系统工具中没有配置编辑器菜单项，可以点击主菜单的“系统”——“首选项”——“主菜单”，在“应用程序”“系统工具”中找到“配置编辑器”并勾选显示即可）。或者运行gconf-editor命令亦可。

在“配置编辑器”中展开/--apps--metacity选中general在右侧的名称中找到button_layout将值改为：

close,maximize,minimize:menu

就可以把窗口按钮移动到窗口左边了，要想恢复成原来的样子可以把值改回

menu:minimize,maximize,close

即可。

<http://hi.baidu.com/lisan1233/blog/item/7dab13d8b4dc193132fa1cec.html>  
  
---

