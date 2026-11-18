---
title: LeetCode 300 最长上升子序列
type: 题解
topic: 动态规划
tags: [C++, 算法/DP, 类型/题解, 难度/进阶]
from: "[[09 动态规划]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [300, LIS, 最长上升子序列]
---

<!-- filename: LeetCode 300 最长上升子序列.md -->

专题：[[09 动态规划]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 300](https://leetcode.cn/problems/longest-increasing-subsequence/) |
| 专题 | [[09 动态规划]] |
| 难度 | ⭐⭐ |
| 一句话 | 求最长严格上升子序列的长度 |

## 1. 题意与输入输出

子序列不要求连续，但顺序不能变，求最长严格上升子序列长度。

- 输入：`nums = [10,9,2,5,3,7,101,18]`
- 输出：`4`（`[2,3,7,101]`）
- 数据范围：`1 <= nums.length <= 2500`

## 2. 思路

`dp[i]`：**以 i 结尾**的最长上升子序列长度。

- 初始 `dp[i] = 1`。
- 对每个 `j < i`，若 `nums[j] < nums[i]`，`dp[i] = max(dp[i], dp[j] + 1)`。
- 答案是 `max(dp)`，不是 `dp[n-1]`。

优化版用「耐心排序 + 二分」，`O(n log n)`；本笔记先给 `O(n²)` 版。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> dp(n, 1);
        int ans = 1;

        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n²)`。
- 空间：`O(n)`。

## 5. 边界与坑

> [!warning] 坑 1：答案是 `max(dp)`
> `dp[n-1]` 只是以最后一个元素结尾的答案，不一定最长。

> [!warning] 坑 2：状态定义写成「前 i 个」
> 那样无法接续，必须定义成「以 i 结尾」。

> [!warning] 坑 3：严格上升
> 判断是 `nums[j] < nums[i]`；非严格用 `<=`。

> [!warning] 坑 4：`n = 1`
> 返回 1，初始化 `ans = 1` 兜住。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 354 俄罗斯套娃信封](https://leetcode.cn/problems/russian-doll-envelopes/) | 二维 LIS，排序后降维 |
| [LeetCode 1143 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | 二维 DP |
| [LeetCode 674 最长连续递增序列](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/) | 连续版，更简单 |

## 7. 关联

- 专题：[[09 动态规划]]
- 原始笔记：`C++/算法/算法题/最长上升子序列.md`
- 上一题：[[LeetCode 416 分割等和子集]]

---

哼，LIS 的 `dp[i]` 必须「以 i 结尾」，写成「前 i 个」就等着 WA 吧。
