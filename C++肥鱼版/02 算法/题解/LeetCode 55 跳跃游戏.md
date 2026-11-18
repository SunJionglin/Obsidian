---
title: LeetCode 55 跳跃游戏
type: 题解
topic: 贪心
tags: [C++, 算法/贪心, 类型/题解, 难度/进阶]
from: "[[02 贪心]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [55, Jump Game]
---

<!-- filename: LeetCode 55 跳跃游戏.md -->

专题：[[02 贪心]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 55](https://leetcode.cn/problems/jump-game/) |
| 专题 | [[02 贪心]] |
| 难度 | ⭐⭐ |
| 一句话 | 每个格子能跳 nums[i] 步，能不能到终点 |

## 1. 题意与输入输出

给非负整数数组 `nums`，从下标 0 出发，`nums[i]` 表示从 i 最多能跳多远。判断能否到达最后一个下标。

- 输入：`nums = [2,3,1,1,4]`
- 输出：`true`
- 输入：`nums = [3,2,1,0,4]`
- 输出：`false`
- 数据范围：`1 <= nums.length <= 10^4`

## 2. 思路

维护「当前能到达的最远位置」`reach`：

- 遍历每个位置 `i`，如果 `i > reach`，说明这个位置根本到不了，直接返回 `false`。
- 否则更新 `reach = max(reach, i + nums[i])`。
- 遍历完都没断，返回 `true`。

**贪心点**：不用关心具体怎么跳，只关心「最远能到哪」。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (i > reach) return false;
            reach = max(reach, i + nums[i]);
        }
        return true;
    }
};
```

## 4. 复杂度

- 时间：`O(n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：只有一个元素
> `nums[0]` 就是终点，直接返回 `true`，循环里也不会断。

> [!warning] 坑 2：开头就是 0
> `[0,1]` 从 0 出发只能停在 0，`i = 1 > reach = 0`，返回 `false`。

> [!warning] 坑 3：`i > reach` 写成 `i >= reach`
> `i == reach` 是能到达的，写 `>=` 会误判。

> [!warning] 坑 4：更新 reach 放错位置
> 必须先判 `i > reach`，再更新；顺序反了会把不可达的位置当成可达。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 45 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) | 求最少步数，需要记录「当前层最远」和「下一层最远」 |
| [LeetCode 1306 跳跃游戏 III](https://leetcode.cn/problems/jump-game-iii/) | 有向图可达性，BFS/DFS |
| [[LeetCode 122 买卖股票的最佳时机 II]] | 都是「维护一个全局最优」的贪心 |

## 7. 关联

- 专题：[[02 贪心]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 56 合并区间]]

---

嘿嘿，这题的本鱼心得：别想着每一步怎么跳，先看最远能飘到哪。
