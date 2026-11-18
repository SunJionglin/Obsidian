`<tuple>` 是**多元组**：`pair` 只能装两个，`tuple` 能装任意多个类型。

---

# 一、创建与取值

```cpp
#include <tuple>
using namespace std;

tuple<int, string, double> t(1, "abc", 2.5);
get<0>(t);            // 1
get<1>(t);            // "abc"

auto u = make_tuple(3, 'x', 1.5);   // 自动推导类型
```

# 二、解包：tie

```cpp
int a; string b; double c;
tie(a, b, c) = t;         // 一次拆开

// 只关心第二个
string only;
tie(ignore, only, ignore) = t;
```

# 三、比较与排序

`tuple` 自带字典序比较（先比第 0 个，再比第 1 个……），可以直接 `sort`：

```cpp
vector<tuple<int, int, int>> v = {{2, 1, 5}, {1, 9, 0}, {1, 2, 3}};
sort(v.begin(), v.end());
// (1,2,3) (1,9,0) (2,1,5)
```

# 四、和 pair / struct 怎么选

| | 字段数 | 可读性 | 适合 |
| --- | --- | --- | --- |
| `pair` | 2 | `first` / `second` | 键值、图论边 |
| `tuple` | 任意 | `get<i>`，多了就晕 | 三元组、临时打包 |
| `struct` | 任意 | 有名字 | 字段多、要长期维护 |

# 五、坑

1. `get<2>(t)` 的 `2` 必须是**编译期常量**，不能是变量。
2. 字段超过 3 个建议换 `struct`，`get<3>` 看代码的人会疯。

# 六、一句话总结

`tuple` = 任意元组，`get<i>` 取值、`tie` 解包、自带字典序；字段一多就用 `struct`。
