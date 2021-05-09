# [跟我一起写Makefile](https://wiki.ubuntu.org.cn/%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile)


<br>
<span><br>
[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=1" title="编辑段落: 概述">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E6%A6%82%E8%BF%B0&amp;variant=zh-cn" title="跟我一起写Makefile:概述">概述 </a></span>
<ul><li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E6%A6%82%E8%BF%B0&amp;variant=zh-cn#.E5.85.B3.E4.BA.8E.E7.A8.8B.E5.BA.8F.E7.9A.84.E7.BC.96.E8.AF.91.E5.92.8C.E9.93.BE.E6.8E.A5" title="跟我一起写Makefile:概述">关于程序的编译和链接 </a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=2" title="编辑段落: MakeFile介绍">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn" title="跟我一起写Makefile:MakeFile介绍">MakeFile介绍 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#makefile.E7.9A.84.E8.A7.84.E5.88.99" title="跟我一起写Makefile:MakeFile介绍">makefile的规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E4.B8.80.E4.B8.AA.E7.A4.BA.E4.BE.8B" title="跟我一起写Makefile:MakeFile介绍">一个示例</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#make.E6.98.AF.E5.A6.82.E4.BD.95.E5.B7.A5.E4.BD.9C.E7.9A.84" title="跟我一起写Makefile:MakeFile介绍">make是如何工作的</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#makefile.E4.B8.AD.E4.BD.BF.E7.94.A8.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:MakeFile介绍">makefile中使用变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E8.AE.A9make.E8.87.AA.E5.8A.A8.E6.8E.A8.E5.AF.BC" title="跟我一起写Makefile:MakeFile介绍">让make自动推导</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E5.8F.A6.E7.B1.BB.E9.A3.8E.E6.A0.BC.E7.9A.84makefile" title="跟我一起写Makefile:MakeFile介绍">另类风格的makefile</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E6.B8.85.E7.A9.BA.E7.9B.AE.E6.A0.87.E6.96.87.E4.BB.B6.E7.9A.84.E8.A7.84.E5.88.99" title="跟我一起写Makefile:MakeFile介绍">清空目标文件的规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#Makefile.E9.87.8C.E6.9C.89.E4.BB.80.E4.B9.88.EF.BC.9F" title="跟我一起写Makefile:MakeFile介绍">Makefile里有什么？</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#Makefile.E7.9A.84.E6.96.87.E4.BB.B6.E5.90.8D" title="跟我一起写Makefile:MakeFile介绍">Makefile的文件名</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E5.BC.95.E7.94.A8.E5.85.B6.E5.AE.83.E7.9A.84Makefile" title="跟我一起写Makefile:MakeFile介绍">引用其它的Makefile</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#.E7.8E.AF.E5.A2.83.E5.8F.98.E9.87.8F_MAKEFILES" title="跟我一起写Makefile:MakeFile介绍">环境变量 MAKEFILES</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:MakeFile%E4%BB%8B%E7%BB%8D&amp;variant=zh-cn#make.E7.9A.84.E5.B7.A5.E4.BD.9C.E6.96.B9.E5.BC.8F" title="跟我一起写Makefile:MakeFile介绍">make的工作方式</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=3" title="编辑段落: 书写规则">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn" title="跟我一起写Makefile:书写规则">书写规则 </a></span>
<ul><li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E8.A7.84.E5.88.99.E4.B8.BE.E4.BE.8B" title="跟我一起写Makefile:书写规则">规则举例</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E8.A7.84.E5.88.99.E7.9A.84.E8.AF.AD.E6.B3.95" title="跟我一起写Makefile:书写规则">规则的语法</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E5.9C.A8.E8.A7.84.E5.88.99.E4.B8.AD.E4.BD.BF.E7.94.A8.E9.80.9A.E9.85.8D.E7.AC.A6" title="跟我一起写Makefile:书写规则">在规则中使用通配符</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E6.96.87.E4.BB.B6.E6.90.9C.E5.AF.BB" title="跟我一起写Makefile:书写规则">文件搜寻</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E4.BC.AA.E7.9B.AE.E6.A0.87" title="跟我一起写Makefile:书写规则">伪目标</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E5.A4.9A.E7.9B.AE.E6.A0.87" title="跟我一起写Makefile:书写规则">多目标</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E9.9D.99.E6.80.81.E6.A8.A1.E5.BC.8F" title="跟我一起写Makefile:书写规则">静态模式</a>
</li>
<li><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E8.87.AA.E5.8A.A8.E7.94.9F.E6.88.90.E4.BE.9D.E8.B5.96.E6.80.A7" title="跟我一起写Makefile:书写规则">自动生成依赖性<br>
</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=4" title="编辑段落: 书写命令">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn" title="跟我一起写Makefile:书写命令">书写命令 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn#.E6.98.BE.E7.A4.BA.E5.91.BD.E4.BB.A4" title="跟我一起写Makefile:书写命令">显示命令</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn#.E5.91.BD.E4.BB.A4.E6.89.A7.E8.A1.8C" title="跟我一起写Makefile:书写命令">命令执行</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn#.E5.91.BD.E4.BB.A4.E5.87.BA.E9.94.99" title="跟我一起写Makefile:书写命令">命令出错</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn#.E5.B5.8C.E5.A5.97.E6.89.A7.E8.A1.8Cmake" title="跟我一起写Makefile:书写命令">嵌套执行make</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%B9%A6%E5%86%99%E5%91%BD%E4%BB%A4&amp;variant=zh-cn#.E5.AE.9A.E4.B9.89.E5.91.BD.E4.BB.A4.E5.8C.85" title="跟我一起写Makefile:书写命令">定义命令包</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=5" title="编辑段落: 使用变量">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn" title="跟我一起写Makefile:使用变量">使用变量 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E5.8F.98.E9.87.8F.E7.9A.84.E5.9F.BA.E7.A1.80" title="跟我一起写Makefile:使用变量">变量的基础</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E5.8F.98.E9.87.8F.E4.B8.AD.E7.9A.84.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:使用变量">变量中的变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E5.8F.98.E9.87.8F.E9.AB.98.E7.BA.A7.E7.94.A8.E6.B3.95" title="跟我一起写Makefile:使用变量">变量高级用法</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E8.BF.BD.E5.8A.A0.E5.8F.98.E9.87.8F.E5.80.BC" title="跟我一起写Makefile:使用变量">追加变量值</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#override_.E6.8C.87.E7.A4.BA.E7.AC.A6" title="跟我一起写Makefile:使用变量">override 指示符</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E5.A4.9A.E8.A1.8C.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:使用变量">多行变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E7.8E.AF.E5.A2.83.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:使用变量">环境变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E7.9B.AE.E6.A0.87.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:使用变量">目标变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F&amp;variant=zh-cn#.E6.A8.A1.E5.BC.8F.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:使用变量">模式变量</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=6" title="编辑段落: 使用条件判断">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E6%9D%A1%E4%BB%B6%E5%88%A4%E6%96%AD&amp;variant=zh-cn" title="跟我一起写Makefile:使用条件判断">使用条件判断 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E6%9D%A1%E4%BB%B6%E5%88%A4%E6%96%AD&amp;variant=zh-cn#.E7.A4.BA.E4.BE.8B" title="跟我一起写Makefile:使用条件判断">示例</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E6%9D%A1%E4%BB%B6%E5%88%A4%E6%96%AD&amp;variant=zh-cn#.E8.AF.AD.E6.B3.95" title="跟我一起写Makefile:使用条件判断">语法</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=7" title="编辑段落: 使用函数">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn" title="跟我一起写Makefile:使用函数">使用函数 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#.E5.87.BD.E6.95.B0.E7.9A.84.E8.B0.83.E7.94.A8.E8.AF.AD.E6.B3.95" title="跟我一起写Makefile:使用函数">函数的调用语法</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#.E5.AD.97.E7.AC.A6.E4.B8.B2.E5.A4.84.E7.90.86.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">字符串处理函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#.E6.96.87.E4.BB.B6.E5.90.8D.E6.93.8D.E4.BD.9C.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">文件名操作函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#foreach_.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">foreach 函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#if_.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">if 函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#call.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">call函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#origin.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">origin函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#shell.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">shell函数</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8%E5%87%BD%E6%95%B0&amp;variant=zh-cn#.E6.8E.A7.E5.88.B6make.E7.9A.84.E5.87.BD.E6.95.B0" title="跟我一起写Makefile:使用函数">控制make的函数</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=8" title="编辑段落: make运行">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn" title="跟我一起写Makefile:make运行">make运行 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn#make.E7.9A.84.E9.80.80.E5.87.BA.E7.A0.81" title="跟我一起写Makefile:make运行">make的退出码</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn#.E6.8C.87.E5.AE.9AMakefile" title="跟我一起写Makefile:make运行">指定Makefile</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn#.E6.8C.87.E5.AE.9A.E7.9B.AE.E6.A0.87" title="跟我一起写Makefile:make运行">指定目标</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn#.E6.A3.80.E6.9F.A5.E8.A7.84.E5.88.99" title="跟我一起写Makefile:make运行">检查规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:make%E8%BF%90%E8%A1%8C&amp;variant=zh-cn#make.E7.9A.84.E5.8F.82.E6.95.B0" title="跟我一起写Makefile:make运行">make的参数<br>
</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=9" title="编辑段落: 隐含规则">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn" title="跟我一起写Makefile:隐含规则">隐含规则 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E4.BD.BF.E7.94.A8.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99" title="跟我一起写Makefile:隐含规则">使用隐含规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99.E4.B8.80.E8.A7.88" title="跟我一起写Makefile:隐含规则">隐含规则一览</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99.E4.BD.BF.E7.94.A8.E7.9A.84.E5.8F.98.E9.87.8F" title="跟我一起写Makefile:隐含规则">隐含规则使用的变量</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99.E9.93.BE" title="跟我一起写Makefile:隐含规则">隐含规则链</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E5.AE.9A.E4.B9.89.E6.A8.A1.E5.BC.8F.E8.A7.84.E5.88.99" title="跟我一起写Makefile:隐含规则">定义模式规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E8.80.81.E5.BC.8F.E9.A3.8E.E6.A0.BC.E7.9A.84.22.E5.BE.8C.E7.BC.80.E8.A7.84.E5.88.99.22" title="跟我一起写Makefile:隐含规则">老式风格的"后缀规则"</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E9%9A%90%E5%90%AB%E8%A7%84%E5%88%99&amp;variant=zh-cn#.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99.E6.90.9C.E7.B4.A2.E7.AE.97.E6.B3.95" title="跟我一起写Makefile:隐含规则">隐含规则搜索算法</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=10" title="编辑段落: 使用make更新函数库文件">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8make%E6%9B%B4%E6%96%B0%E5%87%BD%E6%95%B0%E5%BA%93%E6%96%87%E4%BB%B6&amp;variant=zh-cn" title="跟我一起写Makefile:使用make更新函数库文件">使用make更新函数库文件 </a></span>
<ul><li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8make%E6%9B%B4%E6%96%B0%E5%87%BD%E6%95%B0%E5%BA%93%E6%96%87%E4%BB%B6&amp;variant=zh-cn#.E5.87.BD.E6.95.B0.E5.BA.93.E6.96.87.E4.BB.B6.E7.9A.84.E6.88.90.E5.91.98" title="跟我一起写Makefile:使用make更新函数库文件">函数库文件的成员</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8make%E6%9B%B4%E6%96%B0%E5%87%BD%E6%95%B0%E5%BA%93%E6%96%87%E4%BB%B6&amp;variant=zh-cn#.E5.87.BD.E6.95.B0.E5.BA.93.E6.88.90.E5.91.98.E7.9A.84.E9.9A.90.E5.90.AB.E8.A7.84.E5.88.99" title="跟我一起写Makefile:使用make更新函数库文件">函数库成员的隐含规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8make%E6%9B%B4%E6%96%B0%E5%87%BD%E6%95%B0%E5%BA%93%E6%96%87%E4%BB%B6&amp;variant=zh-cn#.E5.87.BD.E6.95.B0.E5.BA.93.E6.96.87.E4.BB.B6.E7.9A.84.E5.BE.8C.E7.BC.80.E8.A7.84.E5.88.99" title="跟我一起写Makefile:使用make更新函数库文件">函数库文件的后缀规则</a>
</li>
<li> <a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E4%BD%BF%E7%94%A8make%E6%9B%B4%E6%96%B0%E5%87%BD%E6%95%B0%E5%BA%93%E6%96%87%E4%BB%B6&amp;variant=zh-cn#.E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9" title="跟我一起写Makefile:使用make更新函数库文件">注意事项</a></li></ul>
<span>[<a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&amp;action=edit&amp;section=11" title="编辑段落: 后序">编辑</a>]</span> <span><a href="http://wiki.ubuntu.org.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile:%E5%90%8E%E5%BA%8F&amp;variant=zh-cn" title="跟我一起写Makefile:后序">后序 </a></span>
