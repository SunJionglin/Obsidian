`<queue>` 提供两个容器适配器：**队列 `queue`**（先进先出）和**优先队列 `priority_queue`**（堆）。

---

# 一、queue：先进先出

```cpp
#include <queue>
using namespace std;

queue<int> q;
q.push(1);      // 入队（队尾）
q.push(2);
q.front();      // 看队头 → 1
q.back();       // 看队尾 → 2
q.pop();        // 出队（队头），不返回值！
q.empty();      // 是否为空
q.size();       // 元素个数
```

**BFS 就是靠它**：起点入队 → 取队头扩展 → 邻居入队 → 循环到队空。

```cpp
queue<int> q;
q.push(start);
while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int v : g[u])
        if (!vis[v]) { vis[v] = 1; q.push(v); }
}
```

# 二、priority_queue：堆

```cpp
priority_queue<int> pq;              // 默认大根堆，top 是最大值
pq.push(3); pq.push(9); pq.push(1);
pq.top();                            // 9
pq.pop();                            // 弹掉 9
```

小根堆要写全模板参数：

```cpp
#include <functional>
priority_queue<int, vector<int>, greater<int>> pq;   // 小根堆
```

自定义结构体（重载 `<`，注意大根堆是反着的）：

```cpp
struct Node {
    int d, id;
    bool operator<(const Node& o) const {
        return d > o.d;          // 写 > 得到小根堆
    }
};
priority_queue<Node> pq;
```

# 三、常见坑

1. `pop()` **不返回值**，要取值先 `top()` / `front()` 再 `pop()`。
2. 对空队列用 `top()` / `front()` 是未定义行为，先 `empty()` 判断。
3. `queue` 不能遍历、不能下标访问，只能一头进一头出。
4. 清空没有 `clear()`，只能循环 `pop()` 或者重新声明一个。

# 四、一句话总结

`queue` 管先进先出（BFS），`priority_queue` 管取最值（Dijkstra、堆排序）；`pop()` 只删不给值。
