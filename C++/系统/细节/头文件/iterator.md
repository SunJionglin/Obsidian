`<iterator>` 提供**迭代器的通用工具**：`next`、`prev`、`advance`、`distance`、`back_inserter`。

---

# 一、四个常用函数

```cpp
#include <iterator>
using namespace std;

auto it = next(v.begin());          // 往后挪一位
auto jt = prev(v.end());            // 往前挪一位
advance(it, 3);                     // 原地向前挪 3 步（改变自己）
int d = distance(v.begin(), v.end());  // 两个迭代器之间的距离（元素个数）
```

`next` / `prev` **返回新迭代器**，`advance` **改动原迭代器**，这是最容易搞混的地方。

# 二、插入迭代器

```cpp
vector<int> a = {1, 2, 3}, b;
copy(a.begin(), a.end(), back_inserter(b));       // 往 b 尾部追加
copy(a.begin(), a.end(), inserter(b, b.begin())); // 往指定位置插
```

`merge`、`set_union` 这类算法要求「输出到别处」，就得配 `back_inserter`。

# 三、迭代器失效（重点坑）

| 容器 | 什么操作会让迭代器失效 |
| --- | --- |
| `vector` | 扩容（`push_back` 触发）、`insert`、`erase` |
| `deque` | 头尾插入会让迭代器失效 |
| `list` / `set` / `map` | 只有被删的那个失效，其他没事 |

所以 `vector` 里边遍历边删要小心：

```cpp
for (size_t i = 0; i < v.size(); ) {
    if (v[i] == 0) v.erase(v.begin() + i);   // 删了就不要 i++
    else i++;
}
```

# 四、一句话总结

`<iterator>` 最常用 `next` / `prev` / `advance` / `<back_inserter>`；`vector` 边删边遍历会失效，`list` / `map` 只有被删的那个失效。
