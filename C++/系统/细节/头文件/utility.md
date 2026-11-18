`<utility>` 提供最基础的两个工具：**数对 `pair`** 和 **交换 `swap`**。名字不起眼，用得极多。

---

# 一、pair：把两个值捆在一起

```cpp
#include <utility>
using namespace std;

pair<int, int> p = {3, 5};
p.first;                  // 3
p.second;                 // 5

p = make_pair(7, 9);      // 另一种构造
pair<string, int> q("abc", 2);
```

`pair` 自带比较：**先比 first，first 相等再比 second**，所以直接 `sort` 就是双关键字排序。

```cpp
vector<pair<int, int>> v = {{2, 9}, {1, 5}, {2, 3}};
sort(v.begin(), v.end());
// 结果：(1,5) (2,3) (2,9)
```

# 二、和结构体的取舍

| | `pair` | `struct` |
| --- | --- | --- |
| 写法 | 短，`{a, b}` 直接构造 | 要定义类型 |
| 字段名 | 只能 `first` / `second` | 可以起有意义的名字 |
| 比较 | 自带字典序 | 要自己写 `<` |
| 适合 | 临时打包、图论存边、键值 | 字段多、要可读性 |

```cpp
struct Edge { int to, w; };                 // 语义清楚用它
vector<pair<int, int>> g[1005];             // 顺手存边用它
```

# 三、swap

```cpp
int a = 1, b = 2;
swap(a, b);          // a=2, b=1

vector<int> x{1,2}, y{3,4};
swap(x, y);          // 整体交换，O(1)，只换内部指针
```

用 `swap` 清空容器是常用技巧（`vector<int>().swap(v)` 真正释放内存）。

# 四、一句话总结

`pair` 是自带字典序的两元组，图论存边、双关键字排序首选；`swap` 交换容器是 O(1) 的。
