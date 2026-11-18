---
title: LeetCode 50 Pow(x, n)
type: 题解
topic: 倍增
tags: [C++, 算法/倍增, 类型/题解, 难度/进阶]
from: "[[05 倍增]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [50, Pow(x,n), 快速幂]
---

<!-- filename: LeetCode 50 Pow(x, n).md -->

专题：[[05 倍增]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 50](https://leetcode.cn/problems/powx-n/) |
| 专题 | [[05 倍增]] |
| 难度 | ⭐⭐ |
| 一句话 | 快速幂，O(log n) 求 x^n |

## 1. 题意与输入输出

实现 `pow(x, n)`，即 `x` 的 `n` 次幂。

- 输入：`x = 2.0`，`n = 10`
- 输出：`1024.0`
- 数据范围：`-100 < x < 100`，`-2^31 <= n <= 2^31 - 1`

## 2. 思路

把指数拆成二进制：

`x^13 = x^8 * x^4 * x^1`

从低位到高位：

- 当前位是 1：把当前的 `x^(2^k)` 乘进答案。
- 每轮 `x = x * x`，指数右移一位。

这样只用 `O(log n)` 次乘法。

## 3. 代码

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double ans = 1;
        while (N) {
            if (N & 1) ans *= x;
            x *= x;
            N >>= 1;
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(log |n|)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：`n = INT_MIN`
> `-n` 会溢出，先把 `n` 转成 `long long`。

> [!warning] 坑 2：`x = 0` 且 `n < 0`
> 数学上无意义，题目保证不会出现，但工程代码要判。

> [!warning] 坑 3：`n = 0`
> 返回 1，循环不进。

> [!warning] 坑 4：负数底数
> 照常算，奇偶次幂决定符号，不用特判。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 372 超级次方](https://leetcode.cn/problems/super-pow/) | 快速幂 + 取模 |
| [LeetCode 29 两数相除](https://leetcode.cn/problems/divide-two-integers/) | 倍增减法 |
| [[P3865 ST 表]] | 同样用「2^k 预处理」的思想 |

## 7. 关联

- 专题：[[05 倍增]]
- 原始笔记：无（生成例题）
- 下一题：[[P3865 ST 表]]

---

哼，快速幂就是「指数减半、底数翻倍」——跟本鱼吃白饭一样，一口顶两口。
