`<array>` 提供**定长数组** `std::array<T, N>`：大小在编译期固定，但比 C 数组安全、好用。

---

# 一、基本用法

```cpp
#include <array>
using namespace std;

array<int, 5> a = {1, 2, 3, 4, 5};
a[0];              // 1，下标访问（不检查越界）
a.at(0);           // 带越界检查，越界抛异常
a.size();          // 5，编译期常量
a.fill(0);         // 全部填 0
```

遍历和普通数组一样：

```cpp
for (int x : a) cout << x << " ";
sort(a.begin(), a.end());
```

# 二、比 C 数组好在哪

| | `int a[5]` | `array<int,5>` |
| --- | --- | --- |
| 知道自己的大小 | 不知道，会退化成指针 | `a.size()` |
| 整体赋值 | 不行 | `a = b;` 可以 |
| 传函数 | 退化成指针 | 按值/引用整体传 |
| 能否放进容器 | 不行 | 可以 `vector<array<int,3>>` |
| 性能 | 同 | 同（零开销封装） |

# 三、典型场景

```cpp
vector<array<int, 3>> edges;      // 存三元组，比 struct 短
edges.push_back({u, v, w});

array<array<int, 3>, 3> mat = {{{1,0,0},{0,1,0},{0,0,1}}};   // 定长矩阵
```

# 四、注意

1. `array` 在栈上分配，`N` 太大（比如百万级）会爆栈，改用 `vector`。
2. `N` 必须是**编译期常量**，运行时才知道大小就用 `vector`。
3. 默认**不会自动初始化为 0**，`array<int,5> a;` 里是垃圾值，要写 `{}` 才是全 0。

# 五、一句话总结

`array` = 知道自己大小的 C 数组，零开销、可整体赋值、能进容器；定长就选它，变长用 `vector`。
