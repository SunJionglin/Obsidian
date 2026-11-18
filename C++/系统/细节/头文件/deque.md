`<deque>` 是**双端队列**：两头都能进能出，还能像数组一样随机访问。

---

# 一、基本操作

```cpp
#include <deque>
using namespace std;

deque<int> dq;
dq.push_back(1);      // 尾部入
dq.push_front(0);     // 头部入
dq.pop_back();        // 尾部出
dq.pop_front();       // 头部出
dq.front();  dq.back();
dq[0];                // 支持下标访问
dq.size();  dq.empty();
```

`vector` 只能尾部高效增删，`deque` 两端都是 O(1)。

# 二、典型场景

**1. 单调队列（滑动窗口最值）**

```cpp
// 求每个长度为 k 的窗口的最大值
deque<int> dq;                    // 存下标，对应值单调递减
for (int i = 0; i < n; i++) {
    while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
    dq.push_back(i);
    if (dq.front() <= i - k) dq.pop_front();
    if (i >= k - 1) cout << a[dq.front()] << " ";
}
```

**2. 0-1 BFS**：边权只有 0 和 1 时，0 边从前端入队、1 边从后端入队。

**3. 需要两头操作的模拟题**（如双端队列模拟、回文构造）。

# 三、和 vector 的区别

| | `vector` | `deque` |
| --- | --- | --- |
| 尾部增删 | O(1) | O(1) |
| 头部增删 | O(n) | O(1) |
| 随机访问 | 快 | 稍慢（分段连续） |
| 内存 | 一整块连续 | 多块拼接 |

日常优先 `vector`；确实要在头部反复增删时再换 `deque`。

# 四、一句话总结

`deque` = 两头都能动的数组，滑动窗口最值、0-1 BFS 靠它；不要因为它能 `push_front` 就到处用。
