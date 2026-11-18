`<cstdlib>` 是 C 标准库的通用工具头文件，管**整数取绝对值、字符串转数字、随机数、程序退出**这些杂活。

---

# 一、整数绝对值

```cpp
#include <cstdlib>
using namespace std;

abs(-5);        // 5，注意：<cstdlib> 的 abs 是整型
llabs(-5LL);    // long long 版
```

浮点数的绝对值在 `<cmath>` 里：`fabs(-3.5)`。混用会截断小数，是常见 bug。

# 二、字符串转数字

```cpp
atoi("123");            // 123，遇到非数字就停
atol("123456789012");   // long
atoll("...");           // long long

strtol("ff", nullptr, 16);   // 按 16 进制解析 → 255
```

`atoi` 遇到非法输入返回 0，**不会报错**，所以输入是否合法要自己保证。C++ 里更推荐：

```cpp
stoi("123");    // <string>，非法输入会抛异常
stoll("123456789012");
```

# 三、随机数（老写法）

```cpp
#include <cstdlib>
#include <ctime>

srand(time(0));              // 用时间做种子，只调一次
int x = rand() % 100;        // 0～99
int y = rand() % 100 + 1;    // 1～100
```

`rand()` 的范围通常是 0～32767，**随机性很差**。正经随机数用 `<random>` 的 `mt19937`。

# 四、退出程序

```cpp
exit(0);      // 正常退出
exit(1);      // 异常退出，返回给操作系统
```

在 `main` 里直接 `return 0;` 就行，`exit` 主要在深层函数里想立刻结束时用。

# 五、别用的东西

```cpp
system("pause");   // Windows 专用，交作业时经常被判“不规范”
system("cls");     // 同上
```

`system` 会起一个新进程执行命令，慢且有安全隐患，报告和比赛里都别写。

# 六、一句话总结

`<cstdlib>` = 整数 `abs`、`atoi`、`rand/srand`、`exit`；浮点绝对值走 `<cmath>`，正经随机数走 `<random>`。
