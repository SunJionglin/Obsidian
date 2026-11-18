---
title: LeetCode 200 岛屿数量
type: 题解
topic: 搜索
tags: [C++, 算法/搜索, 类型/题解, 难度/进阶]
from: "[[08 搜索]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [200, Number of Islands, 泛洪]
---

<!-- filename: LeetCode 200 岛屿数量.md -->

专题：[[08 搜索]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 200](https://leetcode.cn/problems/number-of-islands/) |
| 专题 | [[08 搜索]] |
| 难度 | ⭐⭐ |
| 一句话 | 数网格里有多少个连通的 1 |

## 1. 题意与输入输出

`'1'` 是陆地，`'0'` 是水，上下左右连通算一个岛，求岛屿数量。

- 输入：`[["1","1","0"],["1","1","0"],["0","0","1"]]`
- 输出：`2`
- 数据范围：`1 <= m, n <= 300`

## 2. 思路

遍历每个格子：

- 遇到 `'1'`，岛屿数 +1。
- 从这个格子开始 DFS，把整个连通块的 `'1'` 改成 `'0'`（标记已访问）。

这样每个岛只会被数一次。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    void dfs(vector<vector<char>>& g, int x, int y) {
        int n = (int)g.size(), m = (int)g[0].size();
        if (x < 0 || x >= n || y < 0 || y >= m || g[x][y] != '1') return;

        g[x][y] = '0';                    // 标记
        for (int d = 0; d < 4; ++d)
            dfs(g, x + dx[d], y + dy[d]);
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int n = (int)grid.size(), m = (int)grid[0].size(), ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == '1') {
                    ++ans;
                    dfs(grid, i, j);
                }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(m*n)`，每格最多访问一次。
- 空间：`O(m*n)`，递归栈最坏情况。

## 5. 边界与坑

> [!warning] 坑 1：忘了标记
> 不把 `'1'` 改成 `'0'`，同一个岛会被反复数。

> [!warning] 坑 2：越界判断顺序
> 先判 `x < 0 || ...`，再访问 `g[x][y]`。

> [!warning] 坑 3：递归太深
> `300×300` 全 1 时递归约 9 万层，可能爆栈；改 BFS 或手动栈。

> [!warning] 坑 4：空网格
> 本题保证 `m,n >= 1`；工程代码要判空。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 695 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 泛洪时累加面积 |
| [LeetCode 733 图像渲染](https://leetcode.cn/problems/flood-fill/) | 同一个泛洪模板 |
| [[LeetCode 733 图像渲染]] | 先写简单的染色 |

## 7. 关联

- 专题：[[08 搜索]]
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 733 图像渲染]]

---

哼，数岛就像数本鱼碗里的饭粒：连在一起才算一口。
