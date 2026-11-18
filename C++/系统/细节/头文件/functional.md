`<functional>` 里装着**函数对象**（仿函数）和函数包装器，日常最常用的只有两个：`greater` 和 `less`。

---

# 一、greater / less：给排序换方向

```cpp
#include <functional>
#include <algorithm>
using namespace std;

int a[5] = {3, 1, 4, 2, 5};
sort(a, a + 5);                    // 升序：1 2 3 4 5
sort(a, a + 5, greater<int>());    // 降序：5 4 3 2 1
```

`less<T>` 是默认的升序比较器，`greater<T>` 是降序。

# 二、小根堆必须用它

```cpp
#include <queue>
priority_queue<int> pq1;                              // 大根堆（默认）
priority_queue<int, vector<int>, greater<int>> pq2;   // 小根堆
```

模板里的三个参数分别是：元素类型、底层容器、**比较器**。这是 `<functional>` 最实在的用处。

# 三、排序结构体

```cpp
struct Node { int x, y; };

sort(v.begin(), v.end(), [](const Node& a, const Node& b) {
    if (a.x != b.x) return a.x < b.x;
    return a.y > b.y;            // x 升序，x 相同则 y 降序
});
```

比较器就是个“返回 bool 的函数”，lambda 写起来最快，不必非用 `<functional>`。

# 四、function：把函数当变量存

```cpp
#include <functional>
function<int(int, int)> f;
f = [](int a, int b) { return a + b; };
cout << f(2, 3);        // 5
```

用于回调、递归 lambda（`function<void(int)> dfs = [&](int u){ ... };`）。**每次调用有额外开销，算法题里少用**。

# 五、注意

1. `greater<int>` 要写清类型，写成 `greater()` 会报错。
2. 比较器必须满足**严格弱序**：不能出现 `a < b` 和 `b < a` 同时为真，否则 `sort` 可能越界崩溃。
3. 比较器写成 `return a <= b;` 是经典错误 → 用 `<`。

# 六、一句话总结

`<functional>` 最常用来写 `greater<int>()` 降序排序和小根堆；比较器必须是严格 `<`。
