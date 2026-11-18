---
title: LeetCode 278 第一个错误的版本
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/入门]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [278, First Bad Version]
---

<!-- filename: LeetCode 278 第一个错误的版本.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 278](https://leetcode.cn/problems/first-bad-version/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐⭐ |
| 一句话 | 在 true/true/false 序列里找第一个 false |

## 1. 题意与输入输出

有 `n` 个版本，从某个版本开始全部出错。题目提供 `bool isBadVersion(version)`，找出**第一个**错误版本，要求调用次数尽量少。

- 输入：`n = 5`，`bad = 4`
- 输出：`4`
- 数据范围：`1 <= bad <= n <= 2^31 - 1`
- 要求：`O(log n)` 次调用

## 2. 思路

序列长这样：`good good good bad bad bad`，是单调的。

找「第一个 true」：

- `isBadVersion(mid)` 为真：答案在 `[l, mid]`，`r = mid`。
- 为假：答案在 `[mid+1, r]`，`l = mid + 1`。

循环用 `l < r`，最后 `l == r` 就是第一个坏版本。

## 3. 代码

```cpp
// bool isBadVersion(int version);  // 题目提供，不用自己实现

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isBadVersion(mid)) r = mid;
            else                   l = mid + 1;
        }
        return l;
    }
};
```

## 4. 复杂度

- 时间：`O(log n)` 次 `isBadVersion` 调用。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：`mid = (l + r) / 2` 溢出
> `n` 可达 `2^31 - 1`，`l + r` 直接爆 `int`。用 `l + (r - l) / 2`。

> [!warning] 坑 2：`r = mid + 1`
> 第一个坏版本可能就是 mid，写成 `mid + 1` 会跳过答案。

> [!warning] 坑 3：循环写 `l <= r`
> 这题用 `l < r`；写 `<=` 时 `r = mid` 会死循环。

> [!warning] 坑 4：n = 1
> 不进循环，直接返回 1，正确。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 704 二分查找]] | 基础模板，先把这个写熟 |
| [[LeetCode 34 在排序数组中查找元素的第一个和最后一个位置]] | 同样是找第一个满足条件的位置 |
| [LeetCode 374 猜数字大小](https://leetcode.cn/problems/guess-number-higher-or-lower/) | 三分支比较，本质也是二分 |

## 7. 关联

- 专题：[[04 二分]]
- Python 版：[[17-第一个错误的版本]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 33 搜索旋转排序数组]]
- 下一题：[[砍树]]

---

嘿嘿，这题最舒服的地方是：不用自己写数组，只负责折半。
