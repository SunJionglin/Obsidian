---
title: LeetCode 69 x 的平方根
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/入门]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [69, Sqrt(x)]
---

<!-- filename: LeetCode 69 x 的平方根.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 69](https://leetcode.cn/problems/sqrtx/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐⭐ |
| 一句话 | 找最大的 k，使 k² ≤ x |

## 1. 题意与输入输出

给一个非负整数 `x`，返回 `x` 算术平方根的整数部分（向下取整）。

- 输入：`x = 8`
- 输出：`2`（2²=4 ≤ 8，3²=9 > 8）
- 数据范围：`0 <= x <= 2^31 - 1`
- 要求：不能用 `sqrt`，用二分。

## 2. 思路

答案区间是 `[0, x]`，`check(mid) = mid * mid <= x` 是**单调**的：mid 越大越容易不成立。

要找的是「最后一个满足 check 的位置」，套右边界模板：

- `check(mid)` 成立：`ans = mid`，往右试。
- 不成立：往左缩。

## 3. 代码

```cpp
class Solution {
public:
    int mySqrt(int x) {
        long long l = 0, r = x, ans = 0;
        while (l <= r) {
            long long mid = l + (r - l) / 2;
            if (mid * mid <= x) { ans = mid; l = mid + 1; }
            else                  r = mid - 1;
        }
        return (int)ans;
    }
};
```

## 4. 复杂度

- 时间：`O(log x)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：`mid * mid` 用 int
> `x = 2^31 - 1` 时 `mid` 接近 46340，平方约 `2.1e9`，已经超 `int`。必须 `long long`。

> [!warning] 坑 2：x = 0
> 区间 `[0,0]`，`ans` 初始 0，返回 0，不要特判也行；但 `r = x` 不能写成 `r = x/2`。

> [!warning] 坑 3：把 `<=` 写成 `<`
> `x = 1` 时 `mid = 0`，`0*0 < 1` 成立但会错过 1。用 `<=`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 367 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/) | 同样的 `mid * mid` 判断，只是返回 bool |
| [[LeetCode 704 二分查找]] | 同为「有序区间找值」，但这里是找边界 |
| [[LeetCode 162 寻找峰值]] | 都是「答案具有单调性」的二分 |

## 7. 关联

- 专题：[[04 二分]]
- Python 版：[[18-x的平方根]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 34 在排序数组中查找元素的第一个和最后一个位置]]
- 下一题：[[LeetCode 162 寻找峰值]]

---

哼，这题看着人畜无害，`mid * mid` 一溢出就原形毕露——本鱼当年就是这么交了个 WA。
