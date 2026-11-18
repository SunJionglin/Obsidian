`<set>` 提供**有序集合** `set`（自动去重、自动升序）和 `multiset`（允许重复）。底层是红黑树，单次操作 O(log n)。

---

# 一、set：有序 + 去重

```cpp
#include <set>
using namespace std;

set<int> s;
s.insert(3);
s.insert(1);
s.insert(3);            // 重复插入无效
s.size();               // 2
s.count(3);             // 1，存在返回 1，否则 0
s.find(3) != s.end();   // 是否存在
s.erase(3);             // 按值删，返回删掉的个数
for (int x : s) cout << x << " ";   // 输出 1 3，永远有序
```

# 二、二分查找：lower_bound / upper_bound

```cpp
set<int> s = {1, 3, 5, 7};
auto it = s.lower_bound(3);   // 第一个 >= 3 的位置 → 指向 3
auto it2 = s.upper_bound(3);  // 第一个 >  3 的位置 → 指向 5
if (it != s.end()) cout << *it;
```

这是 `set` 最值钱的地方：**边插入边查询前驱/后继**，数组排序做不到。

# 三、multiset：允许重复

```cpp
multiset<int> ms;
ms.insert(3); ms.insert(3);
ms.count(3);        // 2
ms.erase(ms.find(3));    // 只删一个 3
ms.erase(3);             // 把 3 全删光
```

注意上面两行 `erase` 的区别，这是最容易踩的坑。

# 四、自定义排序

```cpp
struct Node { int x, y; };
struct cmp {
    bool operator()(const Node& a, const Node& b) const {
        return a.x < b.x;        // 按 x 升序
    }
};
set<Node, cmp> s;
```

# 五、set 与 unordered_set 怎么选

| | `set` | `unordered_set` |
| --- | --- | --- |
| 是否有序 | 有序，能二分 | 无序 |
| 单次复杂度 | O(log n) | 平均 O(1)，最坏 O(n) |
| 能否 lower_bound | 能 | 不能 |
| 适用 | 要前驱后继、要顺序输出 | 只判存在、去重 |

# 六、一句话总结

`set` = 有序去重集合，核心是 `insert` + `lower_bound`；要重复用 `multiset`，`erase` 分「删一个」和「删全部」。
