## 准备工作

建议打开typora的大纲视图模式.

![大纲视图](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukie85kj30mo0isq59.jpg)

## 需要安装的软件

1. Python 官方安装文件.

2. IPython (Python交互窗口,相当于git bash)

3. vscode (编辑器,相当于word,typora等,有很多输入辅助功能)

4. Anaconda (数据分析和科学计算的神兵利器) 可选, 是大数据分析最先进的工具.

5. [软件的下载的百度链接](https://pan.baidu.com/s/1veDBZmfBRKU_6o5vbtu7Ug)

   https://pan.baidu.com/s/1veDBZmfBRKU_6o5vbtu7Ug

   ![安装清单](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukjr5gwj30v40h23zn.jpg)




### 1. 安装python

1. 如果已经安装, 需要先卸载,重启电脑.(没有安装,直接进入第三步)

   打开下载的python安装程序,运行后选择卸载 uninstall

   ![卸载1](https://ws3.sinaimg.cn/large/006tNc79ly1fp6ukfj3u7j30jp0cbmyj.jpg)

   ![卸载2](https://ws3.sinaimg.cn/large/006tNc79ly1fp6ukhte8jj30ip0bidgm.jpg)

   ​

2. 卸载后重启电脑.

3. 开始安装 (如果电脑上之前没有安装,直接操作这一步)

![安装](https://ws4.sinaimg.cn/large/006tNc79ly1fp6uktnpksj30fn0aggn3.jpg)

4. 等待安装完成后,打开 git bash,

   输入命令 

   `python -i'  输入后等一会.

   进去玩一会.  i 是interactive的首字母,代表交互模式.

   ```python
   import sys
   path = sys.executable
   print(path)

   import subprocess
   subprocess.run('start www.baidu.com', shell=True)
   quit()
   #quit()  很关键, 不用交互界面就退出回到 git bash命令行.
   ```

   ![python -i](https://ws3.sinaimg.cn/large/006tNc79ly1fp6uk7c561j30vl0jddlx.jpg)



### 2. 安装ipython

ipython是一个优化的python交互界面.

体验一下自动化安装的乐趣.

继续输入命令

```python
pip install ipython
#然后,系统会自动下载和安装, 站起来溜达溜达,等电脑这个slave完工.
# pip 是python installs packages的缩写.
```

![pip install ipython](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukdc7h2j30wu0gfgth.jpg)

安装完成后,在进去玩一会,
输入命令:

```python
ipython -i
#注意这里跟iphone一样,在python前面多了一个i,
#从现在开始可以忘记python -i 这个命令,全部用ipython -i 取代.
```

![做作业](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukrntv0j30u70fngo6.jpg)

**补充资料**

> 嵌入到git bash的python交互界面,是python shell的其中一种,也是最高效的方式,
> 还有很多方式可以使用python交互界面,(python shell或者叫IDLE)
>
> 1) 比如,python自带的交互界面.
>
> ![python idle](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukt3jgaj30c80hngmn.jpg)
>
> ![python idle 2](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukg18plj30il08taca.jpg)
>
> 如果使用python自带的交互界面,需要在git bash和python shell之间不断地切换,很不方便.
>
> 
>
> 2) 还有一个更加不方便的是在windows原生的dos命令行内的交互python界面.\
>
> ![dos command](https://ws1.sinaimg.cn/large/006tNc79ly1fp6uk9xi9nj30c10ie0tg.jpg)
>
> ![dos command 2](https://ws2.sinaimg.cn/large/006tNc79ly1fp6ukqopumj30i108iaan.jpg)

**总结,** 

在git bash中用`ipython -i`, 运行python shell交互界面, 是比较好的选择.

另外ipython有很多魔术功能,大幅度提高效率,可以到英文主页上探索探索,



### 3. 安装vscode

vscode, 相当于typora,Word,text, note等,文本编辑器,只是写代码更方便和高效.

1. 将文件安装到D盘,节省C盘的空间.(安装到C盘最好,如果电脑配置高,不怕消耗C盘)

![vscode_1](https://ws2.sinaimg.cn/large/006tNc79ly1fp6ukf242rj30eu0bhmy9.jpg)

2. 其他选项全部勾选,

   ​

   ![vscode_2](https://ws2.sinaimg.cn/large/006tNc79ly1fp6ukgj3y5j30ek0bnabi.jpg)

3. 杀毒报错的处理

![vscode_3](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukjaxd8j30i10dqtb3.jpg)



4. 安装完成,进去玩一会, 进入git bash界面,用vscode打开English文件夹下的所有文件.

   ```python
   cd ~desktop/english #切到english文件夹下.
   code .
   # code 是vscode的咒语,
   ```

   ![vscode_dakai](https://ws1.sinaimg.cn/large/006tNc79ly1fp6uksa5x3j30n306z75g.jpg)

5. 打开后

   ![vscode_4](https://ws3.sinaimg.cn/large/006tNc79ly1fp6ukh6smpj30ug0j4tdo.jpg)

6. 高效的搜索功能.(文件夹内搜索和文件内搜索),

   跨文件搜索是程序猿用的文本编辑器的标配,对文本管理和知识管理帮助很大.

   ![vscode搜索功能](https://ws4.sinaimg.cn/large/006tNc79ly1fp6uk91sevj30qf0ipq6m.jpg)

7. 当然最关键的功能是写代码.



### 4. 安装Anaconda

这是可选项,可能一两个月内用不到,

谁知道呢? 只有装上才能想起来用.

从穆紫学的单词, tool is implement.

1. 选择安装到D盘,节省C盘空间.

![anacoda_install_to_d](https://ws3.sinaimg.cn/large/006tNc79ly1fp6ukcbk2sj30i60bp40l.jpg)



2. 高级选项,都勾选

   ![anacoda_install_to_d_2](https://ws3.sinaimg.cn/large/006tNc79ly1fp6uksnlxaj30dt0awq4d.jpg)

3. 最后跳过vscode的安装(已经安装过了)

![跳过vscode的安装](https://ws4.sinaimg.cn/large/006tNc79ly1fp6ukr842cj30ef0bhta6.jpg)



### 5. python的应用实例

实例中不涉及第四个软件Anaconda, 

#### 1) 从交互界面中运行程序.

1. 到刚才下载的安装清单中,找到文件`dictionaries.py`, 

   1) 设置默认打开程序为vscode.

   ![默认打开程序为vscode](https://ws1.sinaimg.cn/large/006tNc79ly1fp6uk6km6rj30l20bxq4g.jpg)

   2) 打开后复制里面的代码.

   ![复制代码](https://ws3.sinaimg.cn/large/006tNc79ly1fp6ukav4wnj30pb0a1gn7.jpg)

   3)切换到git bash中.(快捷键 Alt +Tab),

   先启动python交互界面

   ```python
   ipython -i
   ```

   将刚才复制的内容,粘贴到交互窗口中.

   ![ipython中打开dict](https://ws2.sinaimg.cn/large/006tNc79ly1fp6uk830a7j30lp0iu77o.jpg)

   ​

   4. 关闭浏览器.

      ​



#### 2.从文件中运行程序

1. 将刚才的文件复制到桌面上,可以手动操作,

   也可以在git bash中用下面的代码

   ```python
   #退出python交互界面
   quit()
   #复制文件到桌面
   cp  /c/Users/Administrator/Desktop/Homework/dictionaries.py  ~/desktop
   #git bash的切换到桌面上工作
   cd ~/desktop
   /desktop前面加波浪线 ~, 是绝对路径,无论现在哪里都能切换回到桌面.
   ```

   cp是copy, 将文件拖拽到cp的后面,会自动出现`/c/Users/Administrator/Desktop/Homework/dictionaries.py`,然后是桌面 ` ~/desktop`

   ​

2. 在git bash中运行文件.

   ```python
   ipython dictionaries.py
   #或者
   python dictionaris.py
   都能从dictionaries这个python代码文件中打开词典网页.
   推荐用ipython,这样与 ipython -i 保持一致.
   省去了手工的操作..
   ```

   ![最后一步](https://ws1.sinaimg.cn/large/006tNc79ly1fp6ukbdni1j30iu04rwf2.jpg)

3. 以后每次要查词典,做作业的时候,两部操作

   ```python
   cd ~/desktop #确保在桌面的目录下
   ipython dictionaries.py
   ```

   ​

## 收尾

推荐在大纲视图下,阅读和写作.

![收尾](https://ws2.sinaimg.cn/large/006tNc79ly1fp6uke8zkrj30ea0eiwgb.jpg)