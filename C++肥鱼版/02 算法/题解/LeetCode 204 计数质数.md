---
title: LeetCode 204 计数质数
type: 题解
topic: 枚举与模拟
tags: [C++, 算法/枚举, 类型/题解, 难度/进阶]
from: "[[01 枚举与模拟]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [204, Count Primes, 埃氏筛]
---

<!-- filename: LeetCode 204 计数质数.md -->

专题：[[01 枚举与模拟]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 204](https://leetcode.cn/problems/count-primes/) |
| 专题 | [[01 枚举与模拟]] |
| 难度 | ⭐⭐ |
| 一句话 | 统计小于 n 的质数个数 |

## 1. 题意与输入输出

给整数 `n`，返回所有小于 `n` 的质数数量。

- 输入：`n = 10`
- 输出：`4`（2、3、5、7）
- 数据范围：`0 <= n <= 5*10^6`

## 2. 思路

一个一个判质数是 `O(n√n)`，太慢。用**埃氏筛**：

1. 开一个 `isPrime[0..n-1]`，先全标 `true`。
2. 0 和 1 不是质数，标 `false`。
3. 从 2 开始，如果 `i` 是质数，就把 `i², i²+i, i²+2i, ...` 全标 `false`。
4. 最后数 `true` 的个数。

从 `i²` 开始标，是因为比 `i²` 小的倍数已经被更小的质数筛过了。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if (n < 3) return 0;

        vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;

        for (long long i = 2; i * i < n; ++i) {
            if (!isPrime[i]) continue;
            for (long long j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }

        int ans = 0;
        for (bool b : isPrime) if (b) ++ans;
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n log log n)`。
- 空间：`O(n)`。

## 5. 边界与坑

> [!warning] 坑 1：n = 0 或 1
> 直接返回 0，不然 `isPrime[1]` 可能越界。

> [!warning] 坑 2：`i * i` 溢出
> `i` 接近 `n` 时平方会超 `int`，循环变量用 `long long`。

> [!warning] 坑 3：从 2 开始筛
> 应该从 `i * i` 开始，标更小的倍数纯属浪费。

> [!warning] 坑 4：把 1 当质数
> 1 不是质数，初始化时就要标 `false`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 762 二进制表示中质数个计算置位](https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/) | 小范围质数判断 |
| [[LeetCode 1 两数之和]] | 同为「枚举 + 优化」的思路 |

## 7. 关联

- 专题：[[01 枚举与模拟]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 66 加一]]

---

哼，筛法就是「一人得道，倍数升天」——哦不对，是倍数全灭。
