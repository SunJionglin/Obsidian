---
title: LeetCode 122 买卖股票的最佳时机 II
type: 题解
topic: 贪心
tags: [C++, 算法/贪心, 类型/题解, 难度/入门]
from: "[[02 贪心]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [122, Best Time to Buy and Sell Stock II]
---

<!-- filename: LeetCode 122 买卖股票的最佳时机 II.md -->

专题：[[02 贪心]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 122](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) |
| 专题 | [[02 贪心]] |
| 难度 | ⭐⭐ |
| 一句话 | 可以交易多次，求最大收益 |

## 1. 题意与输入输出

`prices[i]` 是第 i 天股价。每天可以买或卖，但同一时间最多持有一股，求最大总利润。

- 输入：`prices = [7,1,5,3,6,4]`
- 输出：`7`（1 买 5 卖赚 4，3 买 6 卖赚 3）
- 数据范围：`1 <= prices.length <= 3*10^4`

## 2. 思路

把每一天和前一天比：

- 今天比昨天贵：`prices[i] - prices[i-1]` 就是能赚的，累加。
- 今天比昨天便宜：不交易。

等价于「所有上涨段之和」。因为可以无限次交易，每一小段上涨都能吃到。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        for (int i = 1; i < (int)prices.size(); ++i) {
            if (prices[i] > prices[i - 1]) {
                ans += prices[i] - prices[i - 1];
            }
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：只能交易一次
> 那是 LeetCode 121，不是这题。这题可以无限次，所以累加所有上涨。

> [!warning] 坑 2：连续上涨段
> `[1,2,3]` 累加 `1+1=2`，等于 3 买 1 卖，正确。

> [!warning] 坑 3：一直下跌
> 循环里一次都不加，返回 0。

> [!warning] 坑 4：只有一天
> 循环从 1 开始，不进，返回 0。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 121 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | 只能交易一次，维护最小价格 |
| [LeetCode 123 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) | 最多两次，需要 DP |
| [LeetCode 309 最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 状态机 DP |

## 7. 关联

- 专题：[[02 贪心]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 435 无重叠区间]]
- 下一题：[[LeetCode 56 合并区间]]

---

嘿嘿，这题是贪心里的送分题：涨了就吃，跌了就等。
