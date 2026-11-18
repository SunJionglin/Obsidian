---
title: LeetCode 70 爬楼梯
type: 题解
topic: 递推与递归
tags: [C++, 算法/递推, 类型/题解, 难度/入门]
from: "[[03 递推与递归]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [70, Climbing Stairs]
---

<!-- filename: LeetCode 70 爬楼梯.md -->

专题：[[03 递推与递归]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 70](https://leetcode.cn/problems/climbing-stairs/) |
| 专题 | [[03 递推与递归]] |
| 难度 | ⭐ |
| 一句话 | 每次走 1 或 2 阶，走到第 n 阶有几种走法 |

## 1. 题意与输入输出

爬 `n` 阶楼梯，每次只能走 1 阶或 2 阶，求不同走法数。

- 输入：`n = 3`
- 输出：`3`（1+1+1、1+2、2+1）
- 数据范围：`1 <= n <= 45`

## 2. 思路

最后一步要么从 `n-1` 走 1 阶，要么从 `n-2` 走 2 阶，所以：

`dp[n] = dp[n-1] + dp[n-2]`

边界：`dp[1] = 1`，`dp[2] = 2`。

只要前两项，所以用两个变量滚动，空间 `O(1)`。

## 3. 代码

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```

## 4. 复杂度

- 时间：`O(n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：`n = 1` 或 `2`
> 直接返回 `n`，别让循环从 3 开始时越界。

> [!warning] 坑 2：用递归不加记忆化
> `n = 45` 会重复计算到爆炸，老老实实递推。

> [!warning] 坑 3：数组开成 `n`
> 如果写 `dp[n+1]`，下标从 1 到 n，别少开一位。

> [!warning] 坑 4：结果溢出
> `n = 45` 时答案约 18 亿，刚好在 `int` 边缘，开 `long long` 更稳。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 509 斐波那契数]] | 同一个递推式，换个说法 |
| [LeetCode 746 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/) | 递推式变成取 min |
| [LeetCode 198 打家劫舍](https://leetcode.cn/problems/house-robber/) | 隔一个取，递推思想一致 |

## 7. 关联

- 专题：[[03 递推与递归]]
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 509 斐波那契数]]

---

哼，爬楼梯就是斐波那契穿了件马甲，别认不出来。
