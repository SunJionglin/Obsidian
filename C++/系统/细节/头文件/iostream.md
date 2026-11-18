`<iostream>` 是 C++ 的**标准输入输出头文件**，`cin`、`cout`、`cerr`、`endl` 全在这里。写任何 C++ 程序几乎都避不开它。

---

# 一、四个标准流对象

| 对象 | 方向 | 用途 |
| --- | --- | --- |
| `cin` | 输入 | 从键盘读数据，对应 C 的 `scanf` |
| `cout` | 输出 | 往屏幕写数据，对应 C 的 `printf` |
| `cerr` | 输出 | 报错信息，不带缓冲，程序崩了也能看见 |
| `clog` | 输出 | 日志，带缓冲 |

# 二、基本用法

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;              // 链式读入，自动跳过空格换行
    cout << a + b << endl;      // 链式输出
    return 0;
}
```

`>>` 和 `<<` 的返回值还是流本身，所以能一直串下去。读入时会**自动跳过空白字符**（空格、Tab、换行），并按变量类型转换。

# 三、读一整行

```cpp
string s;
getline(cin, s);        // 读一整行，保留空格，不保留换行符
```

坑：`cin >> n;` 之后紧接 `getline`，会读到那个残留的换行，读到一个空串。中间要加：

```cpp
cin >> n;
cin.ignore();           // 吃掉一个字符（换行）
getline(cin, s);
```

# 四、提速

```cpp
ios::sync_with_stdio(false);   // 关掉与 C 标准流的同步
cin.tie(0);                    // 解除 cin 与 cout 的绑定
```

大数据量读入（十万级以上）时这两行能快好几倍，算法题必写。

# 五、endl 与 '\n'

| 写法 | 作用 |
| --- | --- |
| `endl` | 换行 **并刷新缓冲区**，慢 |
| `'\n'` | 只换行，快 |

循环里输出几十万行时用 `'\n'`，别用 `endl`。

# 六、一句话总结

`<iostream>` = `cin` / `cout` / `getline` / `endl`；读整行要配 `cin.ignore()`，大数据要 `sync_with_stdio(false)`。
