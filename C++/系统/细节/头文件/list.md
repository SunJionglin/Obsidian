`<list>` 是**双向链表**：任意位置插入删除都是 O(1)，但没有下标、不能随机访问。

---

# 一、基本操作

```cpp
#include <list>
using namespace std;

list<int> L = {1, 2, 3};
L.push_back(4);      // 尾部插入
L.push_front(0);     // 头部插入
L.pop_back();        // 尾部删除
L.pop_front();       // 头部删除
L.insert(it, 9);     // 在 it 前插入
L.erase(it);         // 删除 it 指向的元素
L.size();  L.empty();
```

遍历只能用迭代器或范围 for：

```cpp
for (int x : L) cout << x << " ";
```

# 二、和 vector / deque 的比较

| | `vector` | `deque` | `list` |
| --- | --- | --- | --- |
| 随机访问 `v[i]` | ✅ 快 | ✅ 稍慢 | ❌ 不支持 |
| 头尾插入 | 尾快头慢 | 都快 | 都快 |
| 中间插入删除 | O(n) | O(n) | **O(1)** |
| 内存 | 连续 | 分段 | 每节点额外两个指针 |

# 三、两个坑

1. **不能 `L[0]`**，也没有 `sort(L.begin(), L.end())`（迭代器不是随机访问），要用成员函数 `L.sort()`。
2. 每个节点额外存前后指针，同样的数据比 `vector` 更占内存，缓存也不友好。

# 四、什么时候用

题目明确要求「频繁在中间插入删除，且不需要下标访问」时才用。**绝大多数场景 `vector` 更快**，因为 CPU 缓存友好。

# 五、一句话总结

`list` = 双向链表，中间增删 O(1)、不能下标；`sort` 要用 `L.sort()`，日常还是 `vector`。
