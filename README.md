# CppTimeTester

测试一个或多个程序的运行时间效率, 并生成可视化图表

(目前仅支持 windows 下 cpp 文件)

<img src="https://i.loli.net/2020/04/04/M2ecpXxJCPADST9.png" width="600" hegiht="300" align=center />

### Deloy

在运行这个项目之前, 请确保你拥有 g++,  python3 (并且均放在根目录下) 以及 python 的 altair 包

其中, 在你已经安装 python 后, 你可以通过在终端中输入 "pip install altair" 来安装 altair包

最后, 将这个仓库 clone 到本地即可

### Compiling

你可以在这个文件夹的路径中通过在终端输入 "python TimeTester.py" 来运行程序

在此之前, 你需要在 Code 文件夹中 (请确保 Code 文件夹与 Timetester.py 文件在同一目录内! ) 提供一个名为 "check.cpp" 的数据生成器以及你的至少一个的测试代码, 其中的具体要求可见 "源码要求文档" (very important)

在代码进行编译后, 你需要输入四个数, 分别为:

1. the Minimum Data: 你需要测试数据的最小规模
2. the Maximum Data: 你需要测试数据的最大规模
3. the Delta Data: 两次测试之间的数据大小间隔
4. the Time Limit: 程序最大限定运行时间, 超出时限的程序将会自动关闭

其中 the Delta Data 不建议过小, 可能因为评测中的波动而出现图表中有强烈振动, 其两次运行中的**计算次数**建议至少相差 1e5 以上

然后等待程序运行结束后, 文件夹内的 "result.html" 即为结果

<img src="https://i.loli.net/2020/04/02/4ZMAslS6Uw2RbFn.gif" width="600" hegiht="300" align=center />

#### Tips

请务必参阅 "源码要求文档"!
