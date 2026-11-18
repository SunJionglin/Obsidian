---
title: LeetCode 118 杨辉三角
type: 题解
topic: 递推与递归
tags: [C++, 算法/递推, 类型/题解, 难度/入门]
from: "[[03 递推与递归]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [118, Pascal's Triangle]
---

<!-- filename: LeetCode 118 杨辉三角.md -->

专题：[[03 递推与递归]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 118](https://leetcode.cn/problems/pascals-triangle/) |
| 专题 | [[03 递推与递归]] |
| 难度 | ⭐ |
| 一句话 | 生成杨辉三角的前 numRows 行 |

## 1. 题意与输入输出

生成杨辉三角前 `numRows` 行，每行两端是 1，中间等于上一行相邻两数之和。

- 输入：`numRows = 5`
- 输出：
  ```text
  [[1],
   [1,1],
   [1,2,1],
   [1,3,3,1],
   [1,4,6,4,1]]
  ```
- 数据范围：`1 <= numRows <= 30`

## 2. 思路

逐行生成：

- 第 `i` 行长度 `i+1`，先全填 1。
- 中间位置 `j`（`1 <= j < i`）用上一行递推：
  `row[j] = ans[i-1][j-1] + ans[i-1][j]`

边界天然是 1，不用特判。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for (int i = 0; i < numRows; ++i) {
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; ++j) {
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j];
            }
            ans.push_back(row);
        }
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(numRows²)`，元素总数。
- 空间：`O(numRows²)`，答案本身。

## 5. 边界与坑

> [!warning] 坑 1：`numRows = 1`
> 只生成 `[[1]]`，内层循环不进，正确。

> [!warning] 坑 2：`j` 的范围
> 从 1 到 `i-1`，两端保持 1；写成 `0..i` 会越界或覆盖边界。

> [!warning] 坑 3：先 push 再算
> 第 `i` 行要用 `ans[i-1]`，必须等上一行已经进 `ans`。

> [!warning] 坑 4：结果溢出
> `numRows = 30` 时中间值很大，`int` 可能不够，按题目范围一般没事。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 119 杨辉三角 II](https://leetcode.cn/problems/pascals-triangle-ii/) | 只要第 k 行，可倒序原地更新 |
| [LeetCode 120 三角形最小路径和](https://leetcode.cn/problems/triangle/) | 二维递推求最小和 |
| [[LeetCode 70 爬楼梯]] | 都是「上一行/前一项推当前」 |

## 7. 关联

- 专题：[[03 递推与递归]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 206 反转链表]]

---

嘿嘿，杨辉三角是本鱼见过最乖的递推：边界全是 1，中间自己加自己。
