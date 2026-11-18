---
title: LeetCode 435 无重叠区间
type: 题解
topic: 贪心
tags: [C++, 算法/贪心, 类型/题解, 难度/进阶]
from: "[[02 贪心]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [435, Non-overlapping Intervals]
---

<!-- filename: LeetCode 435 无重叠区间.md -->

专题：[[02 贪心]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 435](https://leetcode.cn/problems/non-overlapping-intervals/) |
| 专题 | [[02 贪心]] |
| 难度 | ⭐⭐ |
| 一句话 | 最少删几个区间，让剩下的互不重叠 |

## 1. 题意与输入输出

给一组区间 `[start, end]`，移除最少数量的区间，使剩下的区间两两不重叠（端点相接不算重叠）。

- 输入：`intervals = [[1,2],[2,3],[3,4],[1,3]]`
- 输出：`1`（删 `[1,3]`）
- 数据范围：`1 <= intervals.length <= 10^5`

## 2. 思路

反过来想：**最多能保留几个不重叠区间**，答案 = 总数 - 保留数。

按**结束时间**升序排序，然后：

- 当前区间的起点 `>=` 上一个保留区间的终点，就保留它，更新终点。
- 否则跳过（删掉）。

**为什么按结束时间**：结束越早，给后面留的空间越大。按起点排序会先选到长区间。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int keep = 0;
        int lastEnd = INT_MIN;
        for (auto& seg : intervals) {
            if (seg[0] >= lastEnd) {
                ++keep;
                lastEnd = seg[1];
            }
        }
        return (int)intervals.size() - keep;
    }
};
```

## 4. 复杂度

- 时间：`O(n log n)`，排序。
- 空间：`O(1)`（不算排序栈）。

## 5. 边界与坑

> [!warning] 坑 1：按起点排序
> 会先选一个超长区间，后面全被挡住。必须按右端点排。

> [!warning] 坑 2：`>` 和 `>=`
> `[1,2]` 和 `[2,3]` 不算重叠，判断是 `seg[0] >= lastEnd`。

> [!warning] 坑 3：返回删除数而不是保留数
> 题目要「移除几个」，记得 `n - keep`。

> [!warning] 坑 4：`lastEnd` 初始化
> 用 `INT_MIN`，第一个区间一定能选上。

> [!warning] 坑 5：区间是 `vector<vector<int>>`
> 排序比较器要按 `a[1]`，别写成 `a[0]`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) | 同样按右端排序，区间选点 |
| [[LeetCode 455 分发饼干]] | 排序 + 能选就选 |
| [LeetCode 56 合并区间](https://leetcode.cn/problems/merge-intervals/) | 按起点排序，维护当前右端 |

## 7. 关联

- 专题：[[02 贪心]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 455 分发饼干]]
- 下一题：[[LeetCode 122 买卖股票的最佳时机 II]]

---

呜……本鱼第一次按起点排序，删了半个数组才发现不对劲。记住：区间调度看右端。
