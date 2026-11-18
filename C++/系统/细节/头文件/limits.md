`<limits>` 提供**各类数值类型的取值范围**，最常用的是 `numeric_limits<int>::max()` 这类写法。

---

# 一、最常用的一句

```cpp
#include <limits>
using namespace std;

int mx = numeric_limits<int>::max();          // 2147483647
int mn = numeric_limits<int>::min();          // -2147483648
long long L = numeric_limits<long long>::max();  // 9.22e18
```

算法题里设“无穷大”就靠它：

```cpp
const int INF = numeric_limits<int>::max() / 2;    // 除以 2，防止 INF + x 溢出
```

# 二、和 `<climits>` 的老写法对照

| 新写法（`<limits>`） | 老写法（`<climits>`） | 值 |
| --- | --- | --- |
| `numeric_limits<int>::max()` | `INT_MAX` | 2147483647 |
| `numeric_limits<int>::min()` | `INT_MIN` | -2147483648 |
| `numeric_limits<long long>::max()` | `LLONG_MAX` | 9223372036854775807 |
| `numeric_limits<double>::max()` | — | 1.79769e308 |
| `numeric_limits<double>::infinity()` | — | 正无穷 |

两种都能用，`<limits>` 的好处是**模板写法统一**，换类型只改尖括号里的名字。

# 三、其它常用成员

```cpp
numeric_limits<int>::digits10;      // 十进制有效位数 → 9
numeric_limits<double>::epsilon();  // 浮点最小正差，用于判相等
numeric_limits<int>::is_signed;     // 是否有符号
```

判浮点数相等：

```cpp
if (fabs(a - b) < 1e-9) { /* 认为相等 */ }
```

# 四、常见坑

1. `INT_MIN` 取负会溢出：`-INT_MIN` 仍是负数，属于未定义行为。
2. `INF` 别直接用 `INT_MAX`，两个 INF 相加立刻溢出成负数；用 `INT_MAX / 2`。
3. `int` 是 32 位，能存到约 2.1e9；题目数据到 1e10 就要 `long long`。

# 五、一句话总结

`<limits>` = 查类型上下限的模板库；`INF` 用 `max()/2`，超过 2e9 就换 `long long`。
