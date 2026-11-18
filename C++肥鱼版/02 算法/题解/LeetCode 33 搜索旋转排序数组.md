---
title: LeetCode 33 搜索旋转排序数组
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/进阶]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [33, 旋转数组查找]
---

<!-- filename: LeetCode 33 搜索旋转排序数组.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 33](https://leetcode.cn/problems/search-in-rotated-sorted-array/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐⭐⭐ |
| 一句话 | 旋转过的升序数组里找 target |

## 1. 题意与输入输出

原本升序的数组在某个下标处旋转（如 `[0,1,2,4,5,6,7]` → `[4,5,6,7,0,1,2]`），值互不相同，找 `target` 返回下标，否则 `-1`。

- 输入：`nums = [4,5,6,7,0,1,2]`，`target = 0`
- 输出：`4`
- 数据范围：`1 <= nums.length <= 5000`
- 要求：`O(log n)`

## 2. 思路

旋转后，`mid` 把数组分成两半，**至少有一半是有序的**。

1. 若 `nums[l] <= nums[mid]`：左半 `[l, mid]` 有序。
   - target 落在 `[nums[l], nums[mid])` 里 → 去左边；否则去右边。
2. 否则：右半 `[mid, r]` 有序。
   - target 落在 `(nums[mid], nums[r]]` 里 → 去右边；否则去左边。

关键是**先判有序的那一半**，再判 target 在不在里面。

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

            if (nums[l] <= nums[mid]) {                 // 左半有序
                if (nums[l] <= target && target < nums[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            } else {                                    // 右半有序
                if (nums[mid] < target && target <= nums[r])
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }
        return -1;
    }
};
```

## 4. 复杂度

- 时间：`O(log n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：没先判有序半边
> 直接比较 `nums[mid]` 和 target，会把无序的一半当成有序，答案跑偏。

> [!warning] 坑 2：区间开闭写错
> 左半是 `[nums[l], nums[mid])`，右半是 `(nums[mid], nums[r]]`；等号位置差一个就会漏解。

> [!warning] 坑 3：`nums[l] <= nums[mid]` 写成 `<`
> 只剩两个元素时 `l == mid`，用 `<` 会误判成右半有序。

> [!warning] 坑 4：有重复元素
> 本题保证互不相同；有重复时（LeetCode 81）需要额外处理 `nums[l] == nums[mid]`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 81 搜索旋转排序数组 II](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/) | 有重复元素，多一步去重 |
| [LeetCode 153 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) | 同样的「哪半边有序」判断 |
| [[LeetCode 162 寻找峰值]] | 都是局部有序也能二分 |

## 7. 关联

- 专题：[[04 二分]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 162 寻找峰值]]
- 下一题：[[LeetCode 278 第一个错误的版本]]

---

哼，这题像在迷宫里找路：先看哪半边是直的，再决定往哪拐。
