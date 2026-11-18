---
title: LeetCode 59 螺旋矩阵 II
type: 题解
topic: 枚举与模拟
tags: [C++, 算法/模拟, 类型/题解, 难度/入门]
from: "[[01 枚举与模拟]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [59, Spiral Matrix II, 蛇形方阵]
---

<!-- filename: LeetCode 59 螺旋矩阵 II.md -->

专题：[[01 枚举与模拟]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 59](https://leetcode.cn/problems/spiral-matrix-ii/) |
| 专题 | [[01 枚举与模拟]] |
| 难度 | ⭐⭐ |
| 一句话 | 把 1 到 n² 按顺时针螺旋填进 n×n 矩阵 |

## 1. 题意与输入输出

给正整数 `n`，生成 `n×n` 矩阵，按顺时针螺旋顺序填入 `1..n²`。

- 输入：`n = 3`
- 输出：
  ```text
  1 2 3
  8 9 4
  7 6 5
  ```
- 数据范围：`1 <= n <= 20`

## 2. 思路

维护当前位置 `(x, y)` 和方向 `d`，每步：

1. 填当前格。
2. 算下一步 `(nx, ny)`。
3. 如果越界或已填过，顺时针转 90°，重新算下一步。
4. 走过去。

方向数组：右、下、左、上。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> a(n, vector<int>(n, 0));
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};

        int x = 0, y = 0, d = 0;
        for (int k = 1; k <= n * n; ++k) {
            a[x][y] = k;

            int nx = x + dx[d], ny = y + dy[d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || a[nx][ny]) {
                d = (d + 1) % 4;
                nx = x + dx[d];
                ny = y + dy[d];
            }
            x = nx;
            y = ny;
        }
        return a;
    }
};
```

## 4. 复杂度

- 时间：`O(n²)`，每格填一次。
- 空间：`O(n²)`，答案矩阵本身。

## 5. 边界与坑

> [!warning] 坑 1：先转向再判断
> 必须「先算下一步，撞墙才转」，不能每步都转，否则画出来是锯齿。

> [!warning] 坑 2：忘记判断已填
> 只判越界不够，走回内圈会覆盖旧值。条件是 `a[nx][ny] != 0`。

> [!warning] 坑 3：n = 1
> 循环只跑一次，方向转了也没用，答案就是 `[[1]]`。

> [!warning] 坑 4：方向数组顺序
> 顺时针是「右、下、左、上」，写成别的顺序会得到镜像或乱序。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 54 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) | 反过来：读螺旋顺序，不是填 |
| [LeetCode 498 对角线遍历](https://leetcode.cn/problems/diagonal-traverse/) | 同样是方向切换 + 边界判断 |
| 蛇形方阵 | 你的原笔记，方向数组经典题 |

## 7. 关联

- 专题：[[01 枚举与模拟]]
- 原始笔记：`C++/算法/算法题/（重点）蛇形方阵两种实现方式笔记.md`
- 上一题：[[LeetCode 1 两数之和]]
- 下一题：[[LeetCode 66 加一]]

---

嘿嘿，这题本鱼喜欢：方向数组一摆，剩下的就是看着它自己转圈。
