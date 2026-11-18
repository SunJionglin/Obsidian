`<climits>` 是 **C 语言的数值上下限宏**，提供 `INT_MAX`、`LLONG_MAX` 这类常量。

---

# 一、常用宏

| 宏 | 值 |
| --- | --- |
| `INT_MAX` | 2147483647 |
| `INT_MIN` | -2147483648 |
| `UINT_MAX` | 4294967295 |
| `LLONG_MAX` | 9223372036854775807 |
| `CHAR_BIT` | 8（一个字节的位数） |
| `SHRT_MAX` | 32767 |

```cpp
#include <climits>
const int INF = INT_MAX / 2;
```

# 二、和 `<limits>` 的关系

| | `<climits>` | `<limits>` |
| --- | --- | --- |
| 写法 | 宏 `INT_MAX` | 模板 `numeric_limits<int>::max()` |
| 类型安全 | 无 | 有，换类型只改尖括号 |
| 历史 | C 语言 | C++ |

两者等价，**新代码建议用 [[limits]]**，宏在面试题和别人的代码里见得多。

# 三、坑

1. `INT_MIN` 取负会溢出，属于未定义行为。
2. `INT_MAX + 1` 也是溢出，别拿它当「无穷大」直接相加，用 `INT_MAX / 2`。
3. 宏没有类型，`max(INT_MAX, 1LL)` 这种混用会编译错误。

# 四、一句话总结

`<climits>` = `INT_MAX` 那一堆宏，能看懂就行；自己写代码用 `numeric_limits` 更稳。
