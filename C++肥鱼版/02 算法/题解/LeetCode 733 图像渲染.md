---
title: LeetCode 733 图像渲染
type: 题解
topic: 搜索
tags: [C++, 算法/搜索, 类型/题解, 难度/入门]
from: "[[08 搜索]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [733, Flood Fill]
---

<!-- filename: LeetCode 733 图像渲染.md -->

专题：[[08 搜索]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 733](https://leetcode.cn/problems/flood-fill/) |
| 专题 | [[08 搜索]] |
| 难度 | ⭐ |
| 一句话 | 从起点把同色连通块染成新颜色 |

## 1. 题意与输入输出

给 `image`、起点 `(sr, sc)`、新颜色 `color`，把起点所在的同色连通块全部染色。

- 输入：`image = [[1,1,1],[1,1,0],[1,0,1]]`，`sr=1, sc=1, color=2`
- 输出：`[[2,2,2],[2,2,0],[2,0,1]]`
- 数据范围：`1 <= m, n <= 50`

## 2. 思路

BFS 泛洪：

1. 记下起点的旧颜色 `old`。
2. 如果 `old == color`，直接返回（否则死循环）。
3. 起点入队并染色。
4. 每次出队，检查四个邻居，颜色等于 `old` 就染色并入队。

## 3. 代码

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int old = image[sr][sc];
        if (old == color) return image;

        int n = (int)image.size(), m = (int)image[0].size();
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};

        queue<pair<int, int>> q;
        q.push({sr, sc});
        image[sr][sc] = color;

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            for (int d = 0; d < 4; ++d) {
                int nx = x + dx[d], ny = y + dy[d];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (image[nx][ny] != old) continue;

                image[nx][ny] = color;
                q.push({nx, ny});
            }
        }
        return image;
    }
};
```

## 4. 复杂度

- 时间：`O(m*n)`。
- 空间：`O(m*n)`，队列。

## 5. 边界与坑

> [!warning] 坑 1：新旧颜色相同
> 不判 `old == color` 会无限入队。

> [!warning] 坑 2：入队前染色
> 先染色再入队，否则同一个点会被重复加入。

> [!warning] 坑 3：只染起点
> 忘了向四邻扩散，结果只改了一个像素。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 200 岛屿数量]] | 同样的四方向泛洪 |
| [LeetCode 695 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | 泛洪 + 计数 |

## 7. 关联

- 专题：[[08 搜索]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 200 岛屿数量]]
- 下一题：[[LeetCode 46 全排列]]

---

嘿嘿，这题就是「油漆桶」，点一下染一片。
