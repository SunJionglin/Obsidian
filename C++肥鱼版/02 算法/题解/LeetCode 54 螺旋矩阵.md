---
title: LeetCode 54 螺旋矩阵
type: 题解
topic: 枚举与模拟
tags: [C++, 算法/模拟, 类型/题解, 难度/进阶]
from: "[[01 枚举与模拟]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [54, Spiral Matrix]
---

<!-- filename: LeetCode 54 螺旋矩阵.md -->

专题：[[01 枚举与模拟]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 54](https://leetcode.cn/problems/spiral-matrix/) |
| 专题 | [[01 枚举与模拟]] |
| 难度 | ⭐⭐ |
| 一句话 | 按顺时针螺旋顺序读出矩阵 |

## 1. 题意与输入输出

给 `m×n` 矩阵，按顺时针螺旋顺序返回所有元素。

- 输入：`matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- 输出：`[1,2,3,6,9,8,7,4,5]`
- 数据范围：`1 <= m, n <= 10`

## 2. 思路

维护四条边界：`top`、`bottom`、`left`、`right`。

每一轮走四条边：

1. 上边：从左到右，`top++`。
2. 右边：从上到下，`right--`。
3. 下边：从右到左（**要先判 `top <= bottom`**），`bottom--`。
4. 左边：从下到上（**要先判 `left <= right`**），`left++`。

后面两条边必须判，否则单行/单列会重复输出。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if (matrix.empty() || matrix[0].empty()) return ans;

        int top = 0, bottom = (int)matrix.size() - 1;
        int left = 0, right = (int)matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; ++j) ans.push_back(matrix[top][j]);
            ++top;

            for (int i = top; i <= bottom; ++i) ans.push_back(matrix[i][right]);
            --right;

            if (top <= bottom) {
                for (int j = right; j >= left; --j) ans.push_back(matrix[bottom][j]);
                --bottom;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; --i) ans.push_back(matrix[i][left]);
                ++left;
            }
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(m*n)`，每个元素访问一次。
- 空间：`O(1)`（不算返回值）。

## 5. 边界与坑

> [!warning] 坑 1：单行矩阵
> `[[1,2,3]]` 走完上边后 `top > bottom`，下边不能再走，否则重复。

> [!warning] 坑 2：单列矩阵
> 同理，走完右边后 `left > right`，左边不能走。

> [!warning] 坑 3：空矩阵
> `matrix.empty()` 和 `matrix[0].empty()` 都要判。

> [!warning] 坑 4：边界更新顺序
> 每走完一条边立刻收缩，不要等四条边都走完再统一改。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 59 螺旋矩阵 II]] | 反向操作：按螺旋填数 |
| [LeetCode 498 对角线遍历](https://leetcode.cn/problems/diagonal-traverse/) | 方向切换 + 边界判断 |
| 蛇形方阵 | 你的原笔记，同一类模拟 |

## 7. 关联

- 专题：[[01 枚举与模拟]]
- 原始笔记：`C++/算法/算法题/（重点）蛇形方阵两种实现方式笔记.md`
- 上一题：[[LeetCode 204 计数质数]]

---

呜……本鱼第一次写这题，单行矩阵被本鱼读了两遍，输出直接翻倍。
