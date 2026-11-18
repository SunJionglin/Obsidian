---
title: LeetCode 455 分发饼干
type: 题解
topic: 贪心
tags: [C++, 算法/贪心, 类型/题解, 难度/入门]
from: "[[02 贪心]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [455, Assign Cookies]
---

<!-- filename: LeetCode 455 分发饼干.md -->

专题：[[02 贪心]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 455](https://leetcode.cn/problems/assign-cookies/) |
| 专题 | [[02 贪心]] |
| 难度 | ⭐ |
| 一句话 | 小饼干先满足小胃口，最多喂饱几个 |

## 1. 题意与输入输出

`g[i]` 是第 i 个孩子的胃口，`s[j]` 是第 j 块饼干的大小。饼干 `j` 能满足孩子 `i` 当且仅当 `s[j] >= g[i]`。每块饼干最多给一个孩子，求最多满足几个。

- 输入：`g = [1,2,3]`，`s = [1,1]`
- 输出：`1`
- 数据范围：`1 <= g.length <= 3*10^4`，`0 <= s.length <= 3*10^4`

## 2. 思路

排序后双指针：

- 胃口和饼干都从小到大。
- 当前饼干能满足当前孩子，就喂，两个指针都后移。
- 不能满足，换一块更大的饼干（饼干指针后移）。

**为什么这样贪心对**：最小的饼干喂给能喂饱的最小胃口，不会浪费大饼干。

## 3. 代码

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int i = 0, j = 0, ans = 0;
        while (i < (int)g.size() && j < (int)s.size()) {
            if (s[j] >= g[i]) {
                ++ans;
                ++i;
                ++j;
            } else {
                ++j;
            }
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n log n + m log m)`，排序占大头。
- 空间：`O(1)`（不算排序栈）。

## 5. 边界与坑

> [!warning] 坑 1：饼干数组为空
> `s` 可以为空，循环直接不进，返回 0，正确。

> [!warning] 坑 2：用大饼干喂小胃口
> 也能过，但会浪费大饼干；双指针从最小开始，保证不浪费。

> [!warning] 坑 3：排序方向反了
> 从大到小也能写，但判断条件和指针移动方向要跟着反过来。

> [!warning] 坑 4：`s[j] >= g[i]` 写成 `>`
> 饼干等于胃口是能满足的，必须 `>=`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 435 无重叠区间]] | 都是排序 + 贪心选择 |
| [LeetCode 452 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) | 区间选点，按右端排序 |
| [LeetCode 881 救生艇](https://leetcode.cn/problems/boats-to-save-people/) | 双指针，重的配轻的 |

## 7. 关联

- 专题：[[02 贪心]]
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 435 无重叠区间]]

---

哼，这题告诉本鱼一个道理：别拿大饼干去哄小胃口，浪费。
