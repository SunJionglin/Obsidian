---
title: 特训题解 · E 搜索 / F DP背包 / G 并查集图遍历
tags: [特训, 蓝桥杯, 题解, BFS, DFS, DP, 背包, 并查集]
created: 2026-11-11
---

# 题解 · E 块（搜索）+ F 块（DP 背包）+ G 块（并查集图遍历）

---

## E1 · P1443 马的遍历

[题目](https://www.luogu.com.cn/problem/P1443)

**思路**

棋盘上「最少几步」就是无权图最短路 → BFS。八个方向的走法，从起点扩散，`dist` 初始化为 -1，起点为 0。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, sx, sy;
    cin >> n >> m >> sx >> sy;

    vector<vector<int>> dist(n + 1, vector<int>(m + 1, -1));
    int dx[8] = {-2,-1,1,2,2,1,-1,-2};
    int dy[8] = {1,2,2,1,-1,-2,-2,-1};

    queue<pair<int,int>> q;
    dist[sx][sy] = 0;
    q.push({sx, sy});

    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int k = 0; k < 8; ++k) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
            if (dist[nx][ny] != -1) continue;
            dist[nx][ny] = dist[x][y] + 1;
            q.push({nx, ny});
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            printf("%-5d", dist[i][j]);      // 宽度 5、左对齐
        putchar('\n');
    }
    return 0;
}
```

**坑**

- **输出格式**：每个数占 5 个字符、**左对齐**（`%-5d`），用 `cout` 默认会 WA。
- 八个方向别写错（马走日，共 8 种）。
- 起点可能到不了的地方保持 -1。

---

## E2 · P1605 迷宫

[题目](https://www.luogu.com.cn/problem/P1605)

**思路**

求「从起点到终点的路径条数」→ DFS 计数。走过就标记，回溯时**必须撤销**，否则会漏掉别的路径。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m, t, sx, sy, ex, ey, ans = 0;
bool blocked[10][10], vis[10][10];
int dx[4] = {1,-1,0,0}, dy[4] = {0,0,1,-1};

void dfs(int x, int y) {
    if (x == ex && y == ey) { ++ans; return; }
    for (int k = 0; k < 4; ++k) {
        int nx = x + dx[k], ny = y + dy[k];
        if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
        if (blocked[nx][ny] || vis[nx][ny]) continue;
        vis[nx][ny] = true;
        dfs(nx, ny);
        vis[nx][ny] = false;          // 回溯：撤销标记
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> t >> sx >> sy >> ex >> ey;
    while (t--) {
        int x, y;
        cin >> x >> y;
        blocked[x][y] = true;
    }
    vis[sx][sy] = true;
    dfs(sx, sy);
    cout << ans << '\n';
    return 0;
}
```

**坑**

- 起点要先标记 `vis`，否则可能从终点绕回起点重复计数。
- 回溯不撤销 = 只找到一条路。
- 障碍与已访问要分别判断。

---

## E3 · P1135 奇怪的电梯

[题目](https://www.luogu.com.cn/problem/P1135)

**思路**

每层楼只有两条边（上 k 层、下 k 层）→ 建图 + BFS 最短路。`dist` 初始 -1，到不了输出 -1。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b;
    cin >> n >> a >> b;
    vector<int> k(n + 1), dist(n + 1, -1);
    for (int i = 1; i <= n; ++i) cin >> k[i];

    queue<int> q;
    dist[a] = 0;
    q.push(a);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (u == b) break;
        for (int v : {u + k[u], u - k[u]}) {
            if (v < 1 || v > n || dist[v] != -1) continue;
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    cout << dist[b] << '\n';
    return 0;
}
```

**坑**

- 电梯不能原地不动，`k[i]` 为 0 时两条边都是自己，BFS 会自动跳过。
- 起点等于终点输出 0。

---

## E4 · P2404 自然数的拆分

[题目](https://www.luogu.com.cn/problem/P2404)

**思路**

把 n 拆成若干正整数之和，要求**不下降**（避免 1+2 与 2+1 重复）。DFS 时传「上一项的最小值」，下一项从它开始枚举，天然去重。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> path;

void dfs(int rest, int start) {
    if (rest == 0) {
        for (int i = 0; i < (int)path.size(); ++i) {
            if (i) cout << '+';
            cout << path[i];
        }
        cout << '\n';
        return;
    }
    for (int x = start; x <= rest; ++x) {     // 保证不下降
        path.push_back(x);
        dfs(rest - x, x);
        path.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    dfs(n, 1);
    return 0;
}
```

**坑**

- `start` 传 `x` 而不是 `x+1`（允许重复用同一个数）。
- 只输出至少两项的拆分（本题 n≥2，从 start=1 自然满足）。

---

## F1 · P1216 数字三角形

[题目](https://www.luogu.com.cn/problem/P1216)

**思路**

从底部往上推：`dp[i][j] = a[i][j] + max(dp[i+1][j], dp[i+1][j+1])`。倒推省掉边界判断，最后 `dp[1][1]` 就是答案。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> a(n + 2, vector<int>(n + 2, 0));
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= i; ++j) cin >> a[i][j];

    for (int i = n - 1; i >= 1; --i)
        for (int j = 1; j <= i; ++j)
            a[i][j] += max(a[i + 1][j], a[i + 1][j + 1]);

    cout << a[1][1] << '\n';
    return 0;
}
```

**坑**

- 正推也能做，但要处理边界（越界设 -inf），倒推更省事。
- 直接复用 `a` 数组当 `dp`，不用再开一份。

---

## F2 · P1048 采药

[题目](https://www.luogu.com.cn/problem/P1048)

**思路**

0/1 背包：每株药只能采一次。`dp[j]` 表示容量 j 时最大价值，**容量倒序**保证每件只用一次。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, M;
    cin >> T >> M;
    vector<int> dp(T + 1, 0);
    for (int i = 0; i < M; ++i) {
        int t, v;
        cin >> t >> v;
        for (int j = T; j >= t; --j)      // 倒序！
            dp[j] = max(dp[j], dp[j - t] + v);
    }
    cout << dp[T] << '\n';
    return 0;
}
```

**坑**

- 容量循环必须倒序，正序就变成完全背包（每件可重复采）。
- `dp` 大小 `T+1`。

---

## F3 · P1616 疯狂的采药

[题目](https://www.luogu.com.cn/problem/P1616)

**思路**

完全背包：每种药可以无限采。容量**正序**即可。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, M;
    cin >> T >> M;
    vector<ll> dp(T + 1, 0);
    for (int i = 0; i < M; ++i) {
        ll t, v;
        cin >> t >> v;
        for (ll j = t; j <= T; ++j)       // 正序
            dp[j] = max(dp[j], dp[j - t] + v);
    }
    cout << dp[T] << '\n';
    return 0;
}
```

**坑**

- 本题数据大（T、v 到 1e7），**必须 `long long`**，否则溢出。
- 正序 vs 倒序：这是 0/1 与完全背包唯一区别。

---

## F4 · P1049 装箱问题

[题目](https://www.luogu.com.cn/problem/P1049)

**思路**

求「剩余空间最小」= 求「能装下的最大体积」。把体积同时当容量和价值，做 0/1 背包，答案是 `V - dp[V]`。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, n;
    cin >> V >> n;
    vector<int> dp(V + 1, 0);
    for (int i = 0; i < n; ++i) {
        int v;
        cin >> v;
        for (int j = V; j >= v; --j)
            dp[j] = max(dp[j], dp[j - v] + v);
    }
    cout << V - dp[V] << '\n';
    return 0;
}
```

**坑**

- 输出的是**剩余体积**，不是装进去的体积。
- 每件只能用一次 → 倒序。

---

## F5 · P1164 小 A 点菜

[题目](https://www.luogu.com.cn/problem/P1164)

**思路**

求「恰好花完 m 元」的方案数。`dp[j]` 表示花 j 元的方案数，`dp[0] = 1`（不点菜是一种方案），转移 `dp[j] += dp[j-a[i]]`。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> dp(m + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        for (int j = m; j >= a; --j)       // 倒序：每道菜只点一次
            dp[j] += dp[j - a];
    }
    cout << dp[m] << '\n';
    return 0;
}
```

**坑**

- `dp[0] = 1` 是初值的关键，缺了就全 0。
- 方案数可能很大，但本题数据在 `int` 范围内；保险起见可用 `long long`。

---

## G1 · P3367 【模板】并查集

[题目](https://www.luogu.com.cn/problem/P3367)

**思路**

并查集三件事：初始化（每个点自己是根）、`find`（带路径压缩）、`union`（按大小/秩合并）。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> fa, sz;

int find(int x) {
    return fa[x] == x ? x : fa[x] = find(fa[x]);   // 路径压缩
}

void uni(int a, int b) {
    a = find(a); b = find(b);
    if (a == b) return;
    if (sz[a] < sz[b]) swap(a, b);
    fa[b] = a;
    sz[a] += sz[b];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    fa.resize(n + 1); sz.assign(n + 1, 1);
    for (int i = 1; i <= n; ++i) fa[i] = i;

    while (m--) {
        int z, x, y;
        cin >> z >> x >> y;
        if (z == 1) uni(x, y);
        else cout << (find(x) == find(y) ? 'Y' : 'N') << '\n';
    }
    return 0;
}
```

**坑**

- `find` 里要写 `fa[x] = find(fa[x])`（路径压缩），只写 `find(fa[x])` 也能过但慢。
- 初始化 `fa[i] = i` 不能漏。

---

## G2 · P1551 亲戚

[题目](https://www.luogu.com.cn/problem/P1551)

**思路**

纯并查集应用：亲戚关系连通，问两人是否同集合。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int fa[5005];

int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, p;
    cin >> n >> m >> p;
    for (int i = 1; i <= n; ++i) fa[i] = i;

    while (m--) {
        int a, b;
        cin >> a >> b;
        fa[find(a)] = find(b);
    }
    while (p--) {
        int a, b;
        cin >> a >> b;
        cout << (find(a) == find(b) ? "Yes" : "No") << '\n';
    }
    return 0;
}
```

**坑**

- 输出是 `Yes`/`No`（首字母大写），不是 `Y`/`N`。
- 合并时先 `find` 再赋值。

---

## G3 · P5318 查找文献

[题目](https://www.luogu.com.cn/problem/P5318)

**思路**

建邻接表，**每个点的邻居要按编号升序**（题目要求「优先看编号小的」），然后 DFS 求一条遍历序列、BFS 求一条遍历序列。

**代码**

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> g;
vector<bool> vis;

void dfs(int u) {
    vis[u] = true;
    cout << u << ' ';
    for (int v : g[u]) if (!vis[v]) dfs(v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    g.assign(n + 1, {});
    vis.assign(n + 1, false);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }
    for (int i = 1; i <= n; ++i) sort(g[i].begin(), g[i].end());  // 编号小优先

    dfs(1);
    cout << '\n';

    fill(vis.begin(), vis.end(), false);
    queue<int> q;
    vis[1] = true; q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << ' ';
        for (int v : g[u]) if (!vis[v]) { vis[v] = true; q.push(v); }
    }
    cout << '\n';
    return 0;
}
```

**坑**

- 邻接表必须排序，否则遍历顺序不符合题目要求。
- DFS 用递归时注意深度（n 到 1e5 可能爆栈，可改迭代）。
- BFS 前要清空 `vis`。

---

## 关联

- 上一份：[[C-D-二分与前缀差分]]｜总览：[[00-特训总览]]
- 题目：[[01-题目清单]]｜模板：[[03-模板速查]]
