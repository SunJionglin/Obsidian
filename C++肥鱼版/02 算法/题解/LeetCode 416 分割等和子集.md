---
title: LeetCode 416 分割等和子集
type: 题解
topic: 动态规划
tags: [C++, 算法/DP, 类型/题解, 难度/进阶]
from: "[[09 动态规划]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [416, Partition Equal Subset Sum, 01背包]
---

<!-- filename: LeetCode 416 分割等和子集.md -->

专题：[[09 动态规划]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 416](https://leetcode.cn/problems/partition-equal-subset-sum/) |
| 专题 | [[09 动态规划]] |
| 难度 | ⭐⭐ |
| 一句话 | 能不能分成两个和相等的子集 |

## 1. 题意与输入输出

给正整数数组，判断能否分成两个元素和相等的子集。

- 输入：`nums = [1,5,11,5]`
- 输出：`true`（`[1,5,5]` 和 `[11]`）
- 数据范围：`1 <= nums.length <= 200`，`1 <= nums[i] <= 100`

## 2. 思路

转化为 01 背包：

- 总和是奇数，直接 `false`。
- 目标和 `target = sum / 2`。
- `dp[j]` 表示「能否凑出和 j」。
- 每个数选或不选，倒序遍历容量。

`dp[j] = dp[j] || dp[j - x]`

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int x : nums) sum += x;
        if (sum % 2) return false;

        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int x : nums) {
            for (int j = target; j >= x; --j) {
                dp[j] = dp[j] || dp[j - x];
            }
        }
        return dp[target];
    }
};
```

## 4. 复杂度

- 时间：`O(n * target)`。
- 空间：`O(target)`。

## 5. 边界与坑

> [!warning] 坑 1：总和奇数
> 直接返回 `false`，不用进 DP。

> [!warning] 坑 2：正序遍历
> 一维 01 背包必须倒序，正序会变成完全背包。

> [!warning] 坑 3：`dp[0] = true`
> 和为 0 一定可以（什么都不选），漏了整张表全 false。

> [!warning] 坑 4：`j >= x` 的下界
> 写 `j >= 0` 会访问负下标。

> [!warning] 坑 5：元素有 0
> 本题元素为正；有 0 时要注意状态不变，但不影响结果。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 494 目标和](https://leetcode.cn/problems/target-sum/) | 01 背包求方案数 |
| [LeetCode 322 零钱兑换](https://leetcode.cn/problems/coin-change/) | 完全背包求最小值 |
| [LeetCode 1049 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/) | 尽量平分，01 背包 |

## 7. 关联

- 专题：[[09 动态规划]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 198 打家劫舍]]
- 下一题：[[LeetCode 300 最长上升子序列]]

---

嘿嘿，这题就是「把背包塞到一半」，塞满就赢。
