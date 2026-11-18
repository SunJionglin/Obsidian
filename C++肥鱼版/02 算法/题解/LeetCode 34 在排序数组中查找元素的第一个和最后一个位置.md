---
title: LeetCode 34 在排序数组中查找元素的第一个和最后一个位置
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/进阶]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [34, 查找元素范围]
---

<!-- filename: LeetCode 34 在排序数组中查找元素的第一个和最后一个位置.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 34](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐⭐ |
| 一句话 | 非递减数组里找 target 的左右边界 |

## 1. 题意与输入输出

给定非递减数组 `nums` 和 `target`，返回 `target` 第一次和最后一次出现的下标；不存在返回 `[-1, -1]`。

- 输入：`nums = [5,7,7,8,8,10]`，`target = 8`
- 输出：`[3, 4]`
- 数据范围：`0 <= nums.length <= 10^5`
- 要求：`O(log n)`

## 2. 思路

精确查找命中就返回，但重复元素里它可能停在中间——所以要两次二分：

1. **左边界**：找第一个 `>= target` 的位置。
2. **右边界**：找最后一个 `<= target` 的位置。
3. 最后校验 `nums[first] == target`，否则说明 target 不存在。

为什么要校验？因为 `first` 可能指向一个比 target 大的数，`last` 可能指向一个比 target 小的数。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = (int)nums.size();
        int first = -1, last = -1;

        int l = 0, r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) { first = mid; r = mid - 1; }
            else                       l = mid + 1;
        }

        if (first == -1 || nums[first] != target) return {-1, -1};

        l = 0; r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] <= target) { last = mid; l = mid + 1; }
            else                       r = mid - 1;
        }

        return {first, last};
    }
};
```

## 4. 复杂度

- 时间：`O(log n)`，两次二分。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：空数组
> `n = 0` 时 `first` 保持 `-1`，校验直接返回 `[-1,-1]`，不会越界。

> [!warning] 坑 2：target 不存在
> `first` 可能指向比 target 大的元素，必须 `nums[first] != target` 再判一次。

> [!warning] 坑 3：全数组都是 target
> 左边界停在 0，右边界停在 `n-1`，两次二分都要从完整区间开始。

> [!warning] 坑 4：只做一次二分
> 找到任意一个 8 就返回，范围会缩成 `[3,3]` 或 `[4,4]`，不是 `[3,4]`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 704 二分查找]] | 单次精确查找，34 是它的加强版 |
| [LeetCode 35 搜索插入位置](https://leetcode.cn/problems/search-insert-position/) | 左边界，找不到时返回插入点 |
| [LeetCode 278 第一个错误的版本](https://leetcode.cn/problems/first-bad-version/) | 找第一个满足条件的位置，同左边界 |

## 7. 关联

- 专题：[[04 二分]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 704 二分查找]]
- 下一题：[[LeetCode 69 x 的平方根]]

---

哼，一次二分不够就两次——本鱼当年就是只做一次，结果范围永远只有一格。
