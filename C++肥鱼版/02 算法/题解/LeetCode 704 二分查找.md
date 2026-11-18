---
title: LeetCode 704 二分查找
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/入门]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [704, Binary Search]
---

<!-- filename: LeetCode 704 二分查找.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 704](https://leetcode.cn/problems/binary-search/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐ |
| 一句话 | 有序无重复数组里找目标下标 |

## 1. 题意与输入输出

给定一个升序、无重复的整数数组 `nums` 和目标值 `target`，找到返回下标，找不到返回 `-1`。

- 输入：`nums = [-1,0,3,5,9,12]`，`target = 9`
- 输出：`4`
- 数据范围：`1 <= nums.length <= 10^4`，`-10^4 < nums[i], target < 10^4`
- 要求：`O(log n)`

## 2. 思路

哼，这题是二分里的 1+1，但 1+1 也有人写错。

闭区间 `[l, r]`，每轮看 `mid`：

- `nums[mid] == target`：直接返回。
- `nums[mid] < target`：答案在右半边，`l = mid + 1`。
- `nums[mid] > target`：答案在左半边，`r = mid - 1`。

每轮排除一半，所以 `O(log n)`。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = (int)nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid + 1;
            else                    r = mid - 1;
        }
        return -1;
    }
};
```

## 4. 复杂度

- 时间：`O(log n)`，每轮区间减半。
- 空间：`O(1)`，只用了三个变量。

## 5. 边界与坑

> [!warning] 坑 1：`while (l < r)` 漏掉最后一个元素
> 闭区间必须写 `l <= r`；写成 `<` 时，区间只剩一个元素会直接退出。

> [!warning] 坑 2：`mid = (l + r) / 2` 溢出
> `l + r` 可能超过 `int`。写 `l + (r - l) / 2`。

> [!warning] 坑 3：`l = mid` 而不是 `mid + 1`
> `mid` 已经判断过，不排除会死循环。

> [!warning] 坑 4：数组为空
> 本题约束 `n >= 1`，但工程代码要判 `nums.empty()`，否则 `r = -1` 后逻辑仍能跑，别的地方可能越界。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 34 在排序数组中查找元素的第一个和最后一个位置]] | 同样的二分，但要做两次找边界 |
| [LeetCode 35 搜索插入位置](https://leetcode.cn/problems/search-insert-position/) | 找不到时返回插入位置，等价于 `lower_bound` |
| [[LeetCode 69 x 的平方根]] | 二分答案，`check` 换成 `mid * mid <= x` |

## 7. 关联

- 专题：[[04 二分]]
- Python 版：[[15-二分查找]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 34 在排序数组中查找元素的第一个和最后一个位置]]

---

嘿嘿，704 要是还写错，本鱼就把这条尾巴打成蝴蝶结。
