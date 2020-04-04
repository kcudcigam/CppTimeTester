# 源码要求文档

你应该把你的一个名为 "check.cpp" 与至少一个的测试代码放在这个文件夹内

其中 "check.cpp" 需要能读入一个参数 Number, 并生成与 Number 等规模的数据进行输出

just like this:

```cpp
#include<bits/stdc++.h>
using namespace std;
int main() {
    int Num;
    cin >> Num;
    for(int i = 1; i <= n; i++)
        cout << i << endl;
    return 0;
}
```

其中所有的包括 "check.cpp" 的源码中都必须为**标准输入输出**, 不要添加任何类似于 “freopen” 等的文件重定向, 且**文件名中不得有空格**

评测中不开 O2, 默认已开大空间,  若有需要, 可自行手动修改 TimeTester.py中的参数(以后可能会添加这个功能的)
