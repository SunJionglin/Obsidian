---
title: LeetCode 162 寻找峰值
type: 题解
topic: 二分
tags: [C++, 算法/二分, 类型/题解, 难度/进阶]
from: "[[04 二分]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [162, Find Peak Element]
---

<!-- filename: LeetCode 162 寻找峰值.md -->

专题：[[04 二分]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 162](https://leetcode.cn/problems/find-peak-element/) |
| 专题 | [[04 二分]] |
| 难度 | ⭐⭐⭐ |
| 一句话 | 无序数组里找任意一个峰值，要求 O(log n) |

## 1. 题意与输入输出

峰值元素：严格大于左右相邻元素。数组两端视为 `-∞`。返回**任意一个**峰值下标。

- 输入：`nums = [1,2,3,1]`
- 输出：`2`（`nums[2] = 3`）
- 数据范围：`1 <= nums.length <= 1000`
- 要求：`O(log n)`

## 2. 思路

数组整体无序，但有**局部单调性**：如果 `nums[mid] < nums[mid+1]`，那么 mid 右侧一定存在峰值（一直往右走，要么上升要么下降，总会停在一个峰）。反之左侧一定有峰。

所以：

- `nums[mid] < nums[mid+1]`：峰值在右，`l = mid + 1`。
- 否则：峰值在左（含 mid），`r = mid`。

注意这里用 `l < r`，最后 `l == r` 就是峰值。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = (int)nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[mid + 1]) l = mid + 1;
            else                           r = mid;
        }
        return l;
    }
};
```

## 4. 复杂度

- 时间：`O(log n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：用 `l <= r` 加 `mid + 1` 越界
> 这题是 `l < r` 的写法，`mid + 1` 一定在范围内；混用闭区间模板会越界。

> [!warning] 坑 2：`r = mid - 1`
> 会把可能的峰值排除掉。峰值在左侧时是 `r = mid`，不是 `mid - 1`。

> [!warning] 坑 3：数组只有一个元素
> `l = r = 0`，循环不进，直接返回 0，正确。

> [!warning] 坑 4：以为数组必须有序
> 这题恰恰是无序的，靠的是「相邻比较」的局部单调性。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 852 山脉数组的峰顶索引](https://leetcode.cn/problems/peak-index-in-a-mountain-array/) | 先升后降，峰值唯一，同样 `l < r` |
| [LeetCode 153 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) | 局部有序，比较 `mid` 与右端点 |
| [[LeetCode 33 搜索旋转排序数组]] | 同样利用「哪半边有序」 |

## 7. 关联

- 专题：[[04 二分]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 69 x 的平方根]]
- 下一题：[[LeetCode 33 搜索旋转排序数组]]

---

呜……本鱼第一次写这题，`r = mid - 1` 把答案亲手排除了，还纳闷为什么返回的不是峰。
