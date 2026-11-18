---
title: LeetCode 56 合并区间
type: 题解
topic: 贪心
tags: [C++, 算法/贪心, 类型/题解, 难度/进阶]
from: "[[02 贪心]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [56, Merge Intervals]
---

<!-- filename: LeetCode 56 合并区间.md -->

专题：[[02 贪心]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 56](https://leetcode.cn/problems/merge-intervals/) |
| 专题 | [[02 贪心]] |
| 难度 | ⭐⭐ |
| 一句话 | 把所有重叠区间合并成不重叠的 |

## 1. 题意与输入输出

给一组区间，合并所有重叠的区间，返回不重叠的结果（按起点升序）。

- 输入：`intervals = [[1,3],[2,6],[8,10],[15,18]]`
- 输出：`[[1,6],[8,10],[15,18]]`
- 数据范围：`1 <= intervals.length <= 10^4`

## 2. 思路

按**起点**升序排序，然后一次扫描：

- 结果为空，或当前区间起点 `>` 结果最后一个区间的终点：不相交，直接加入。
- 否则相交（端点相接也算相交）：把最后一个区间的终点更新为两者最大值。

**为什么按起点**：合并区间关心的是「当前覆盖到哪」，起点排序能保证后面的区间起点不小于当前。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> ans;
        for (auto& seg : intervals) {
            if (ans.empty() || seg[0] > ans.back()[1]) {
                ans.push_back(seg);
            } else {
                ans.back()[1] = max(ans.back()[1], seg[1]);
            }
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n log n)`，排序。
- 空间：`O(1)`（不算返回值）。

## 5. 边界与坑

> [!warning] 坑 1：按终点排序
> 合并区间要按**起点**排；按终点排会出现「后面的区间起点更小」的情况。

> [!warning] 坑 2：`>=` 写成 `>`
> `[1,4]` 和 `[4,5]` 端点相接，应该合并；判断是 `seg[0] > ans.back()[1]` 才不相交。

> [!warning] 坑 3：忘记取 max
> `[1,10]` 和 `[2,3]` 合并后是 `[1,10]`，不能直接覆盖成 `[1,3]`。

> [!warning] 坑 4：原地修改输入
> `ans.push_back(seg)` 存的是副本；如果要原地合并，记得先备份。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 435 无重叠区间]] | 反过来：删最少让区间不重叠 |
| [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) | 区间选点，按右端排序 |
| [LeetCode 57 插入区间](https://leetcode.cn/problems/insert-interval/) | 合并的变体，先找插入位置 |

## 7. 关联

- 专题：[[02 贪心]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 122 买卖股票的最佳时机 II]]
- 下一题：[[LeetCode 55 跳跃游戏]]

---

哼，合并区间和删区间是亲兄弟：一个按起点、一个按终点，别搞反。
