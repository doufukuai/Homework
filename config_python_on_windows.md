

### 3.1.3. Removing the MAX_PATH Limitation

Windows historically has limited path lengths to 260 characters. This meant that paths longer than this would not resolve and errors would result.

In the latest versions of Windows, this limitation can be expanded to approximately 32,000 characters. Your administrator will need to activate the “Enable Win32 long paths” group policy, or set the registry value`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem@LongPathsEnabled` to `1`.

This allows the [`open()`](https://docs.python.org/3/library/functions.html#open) function, the [`os`](https://docs.python.org/3/library/os.html#module-os) module and most other path functionality to accept and return paths longer than 260 characters when using strings. (Use of bytes as paths is deprecated on Windows, and this feature is not available when using bytes.)

After changing the above option, no further configuration is required.

Changed in version 3.6: Support for long paths was enabled in Python.



### 3.3.1. Excursus: Setting environment variables[¶](https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables)

```python
C:\>set PATH=C:\Program Files\Python 3.6;%PATH%
C:\>set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib
C:\>python
```

### 怎样用 Windows 入门Python？

Python 对 Windows 相当友好啊，你们不要吓唬新人。去下载安装一个 ActivePython，能给 VC/C# 程序员当辅助工具了。再装一个 Ulipad 当开发工具，在windows上可以愉悦的使用Python。不否认 Python 在 *nix 环境中的价值，但是 Python 与 windows 也是非常好的搭档。只有你需要学习 *nix 的知识时，才需要去了解如何在 *nix 中使用 Python。当你对 Python 内置的交互环境有初步了解以后，可以安装一个 ipython 作为日常的 python 交互环境使用，这个 shell 更友好，而且随着你对 python 的深入了解，还会发现 ipython 有很多高级的功能可以提高你的生产力。如果你会用 Emacs ，Emacs的Python插件使用起来非常便利。你可以尝试将 ipython 集成进去，形成一个很好的集成开发环境。作者：刘鑫链接：https://www.zhihu.com/question/21713337/answer/34481848来源：知乎著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





### Python [编辑器和集成开发环境](https://woodpecker.org.cn/diveintopython3/installing-python.html#editors)

如果要以 Python 编写程序，idle 并不是唯一的编辑器选择。尽管它对于初学该语言非常有帮助，但许多开发人员更喜欢其它文本编辑器或集成开发环境。（ides）在此我不想展开阐述，Python 社区维护了一份 [Python 相关编辑器的清单](http://wiki.python.org/moin/PythonEditors)，涵盖了各种各样支持平台和软件许可协议。

您可能也想查看一下这份 [Python相关 ides](http://wiki.python.org/moin/IntegratedDevelopmentEnvironments) 的清单，尽管其中还只有少数才支持 Python 3 。其中之一是 [PyDev](http://pydev.sourceforge.net/)，[Eclipse](http://eclipse.org/) 的一种插件，它将Eclipse 变成了一种成熟的 Python ide。Eclipse 和 PyDev 都是跨平台的开源软件。

在商业方面，有 ActiveState 公司的 [Komodo ide](http://www.activestate.com/komodo/) 。它需要用户为单位的授权许可，但学生可以得到折扣，同时还有时间受限的免费试用版。

在用 Python 编程的九年中，我使用 [GNU Emacs](http://www.gnu.org/software/emacs/) 编辑 Python 程序，并在命令行 Python Shell 中进行调试。对于使用 Python 开发来说，编辑器之选没有绝对的正确和错误。重要的是找到适合自己的道路！



1. 点击菜单——>点击计算机——>系统属性

   ——>高级系统设置——>环境变量——>TEMP——>编辑path——>输入python安装路径

   [![如何在Windows命令行下运行python脚本程序](https://imgsa.baidu.com/exp/w=500/sign=ceb37ea93aadcbef01347e069caf2e0e/e1fe9925bc315c602ab92c8286b1cb13495477aa.jpg)](http://jingyan.baidu.com/album/f7ff0bfc3b6d172e26bb1314.html?picindex=3)

2. 2

   打开cmd窗口，输入python，然后输入python命令

   [![如何在Windows命令行下运行python脚本程序](https://imgsa.baidu.com/exp/w=500/sign=f4872e3d3fa85edffa8cfe23795509d8/f9dcd100baa1cd113a3d354db212c8fcc2ce2dd7.jpg)](http://jingyan.baidu.com/album/f7ff0bfc3b6d172e26bb1314.html?picindex=4)

   END

# 怎样查看win10下Python安装路径？

转载 2017年08月11日 17:48:32

- **6593
- 怎样查看python安装路径？

```
你的安装路径是
C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35
一般来说python最好直接安排在C盘根目录下：
C:\\Python35-32
类似这样。
```





# Install and configure Python[¶](http://interactivepython.org/runestone/static/pip2/Installation/pythonInstall.html#install-and-configure-python)

Now, you’ll need to install the Python interpreter on your computer. This process will again be a little bit different depending on whether you have a computer that runs a Mac or the Windows operating system. Follow the appropriate set of instructions:

- [*Windows*](http://interactivepython.org/runestone/static/pip2/Installation/pythonInstall.html#windows-python-install)
- [*Mac*](http://interactivepython.org/runestone/static/pip2/Installation/pythonInstall.html#mac-python-install)

## Install and configure python for Windows

Please download and install Python 2.7 from:

<https://www.python.org/downloads/release/python-278/>

Download and install the file Windows x86 MSI Installer (2.7.8) - when the install process asks you which directory to use - make sure to keep the default directory of C:Python27. If you are not sure if your Windows is 64-bit - install the 32-bit version of Python, the one that just says, “Windows x86 MSI Installer (2.7.8)”. If you know that you have 64-bit Windows, you can download the X86-64 MSI Installer.

Note

Make sure that you install the latest version of Python 2.x - do not install Python 3.x. There are signficant differences between Python 2 and Python 3 and this book/site is based on Python 2.

With just this installation, you can get an interactive python interpreter where you can type code one line at a time and have it executed. You may find some options on the Windows menu for this, such as Idle. We *do not* recommend using these.

With just this installation it is also possible to run python from the Windows command prompt. But the Windows command prompt is tricky to deal with. To establish greater consistency with the environment in which Mac users will be working and because it’s just a better command prompt, we will invoke Python using Git Bash.

You have one configuration to do, to tell Git Bash where in the file system to find the Python interpreter. Follow the steps below to do that.

1. Launch the program Git Bash in the usual way that you launch Windows programs. A shortcut for Git Bash was created during installation.
2. At the command prompt, paste this command `export PATH="$PATH:/c/Python27"`. That will tell Windows where to find Python. (This assumes that you installed it in C:\Python27, as we told you to above.)
3. Check to make sure that this worked correctly by entering the command `python --version`. It should say Python 2.7.8 (or 2.7.something), as shown in the figure below.
4. Assuming that worked correctly, you will want to set up git bash so that it always knows where to find python. To do that, enter the following command: `echo 'export PATH="$PATH:/c/Python27"' > .bashrc`. That will save the command into a file called .bashrc. .bashrc is executed every time git bash launches, so you won’t have to manually tell the shell where to find python again.
5. Check to make sure that worked by typing exit, relaunching git bash, and then typing `python --version` again.

## Install and configure python for Mac







# Python On Windows Git Bash

**[JULY 21, 2016](https://sonalsatpute.wordpress.com/2016/07/21/python-on-windows-git-bash/) **[SONAL SATPUTE](https://sonalsatpute.wordpress.com/author/sonalsatpute/)**[LEAVE A COMMENT](https://sonalsatpute.wordpress.com/2016/07/21/python-on-windows-git-bash/#respond)

Follow below steps to enable Python from Windows Git Bash.

Assuming you already installed  Python on **C:\Python27\** if not then please install the Python from [here](https://www.python.org/downloads/)

Open the Git Bash and follow bellow steps

```
sonal@sonal-pc MINGW64 ~
$ export PATH="$PATH:/c/Python27"
```

This will tell bash where to find Python.

```
sonal@sonal-pc MINGW64 ~
$ python --version
Python 2.7.12
```

It should say Python 2.7.12 (or 2.7.xxx)

If you want to enable Python each time you open Git Bash then apply below command; this  command will add the entry in **\*~/****.bashrc*** which is executed evety time we launch Git Bash

```
sonal@sonal-pc MINGW64 ~
$ echo 'export PATH="$PATH:/c/Python27"' > .bashrc
```

Lets Close the Git Bash and launch it again to make sure its working.

```
sonal@sonal-pc MINGW64 ~
$ python --version
Python 2.7.12
```

all set have fun !