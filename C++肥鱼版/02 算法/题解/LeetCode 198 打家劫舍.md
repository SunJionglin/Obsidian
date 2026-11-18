---
title: LeetCode 198 打家劫舍
type: 题解
topic: 动态规划
tags: [C++, 算法/DP, 类型/题解, 难度/入门]
from: "[[09 动态规划]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [198, House Robber]
---

<!-- filename: LeetCode 198 打家劫舍.md -->

专题：[[09 动态规划]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 198](https://leetcode.cn/problems/house-robber/) |
| 专题 | [[09 动态规划]] |
| 难度 | ⭐⭐ |
| 一句话 | 不能偷相邻两家，求最大金额 |

## 1. 题意与输入输出

每个房子有金额 `nums[i]`，相邻的房子不能同时偷，求最大收益。

- 输入：`nums = [2,7,9,3,1]`
- 输出：`12`（偷 2、9、1）
- 数据范围：`1 <= nums.length <= 100`

## 2. 思路

`dp[i]`：考虑前 `i` 家能偷到的最大金额。

- 不偷第 i 家：`dp[i-1]`
- 偷第 i 家：`dp[i-2] + nums[i]`

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

只需要前两项，用两个变量滚动。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = (int)nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        int a = nums[0];
        int b = max(nums[0], nums[1]);

        for (int i = 2; i < n; ++i) {
            int c = max(b, a + nums[i]);
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

> [!warning] 坑 1：`n = 1`
> 直接返回 `nums[0]`，别让 `dp[1]` 越界。

> [!warning] 坑 2：`n = 0`
> 返回 0，空数组也要处理。

> [!warning] 坑 3：状态定义写错
> `dp[i]` 是「前 i 家」，不是「一定要偷第 i 家」；后者还要多一步取 max。

> [!warning] 坑 4：环形房屋
> 那是 213 题，要分「偷第一家」和「不偷第一家」两种情况。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 213 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) | 环形，拆成两段 |
| [LeetCode 337 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/) | 树形 DP |
| [LeetCode 70 爬楼梯](https://leetcode.cn/problems/climbing-stairs/) | 同样是前两项递推 |

## 7. 关联

- 专题：[[09 动态规划]]
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 416 分割等和子集]]

---

哼，打家劫舍是本鱼最爱的 DP：偷与不偷，一念之间。
