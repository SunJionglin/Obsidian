---
title: LeetCode 75 颜色分类
type: 题解
topic: 排序
tags: [C++, 算法/排序, 类型/题解, 难度/入门]
from: "[[07 排序]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [75, Sort Colors, 荷兰国旗]
---

<!-- filename: LeetCode 75 颜色分类.md -->

专题：[[07 排序]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 75](https://leetcode.cn/problems/sort-colors/) |
| 专题 | [[07 排序]] |
| 难度 | ⭐⭐ |
| 一句话 | 只有 0/1/2 的数组原地排序 |

## 1. 题意与输入输出

数组只含 0、1、2，原地排序，不能依赖库函数。

- 输入：`nums = [2,0,2,1,1,0]`
- 输出：`[0,0,1,1,2,2]`
- 数据范围：`1 <= nums.length <= 300`

## 2. 思路

两种写法：

1. **计数排序**：数出 0/1/2 的个数，再按顺序写回。`O(n)`，两趟。
2. **三指针（荷兰国旗）**：一趟扫描，`0` 换到左边，`2` 换到右边，`1` 留在中间。

面试一般期待三指针，但计数排序更稳、更好写。

## 3. 代码

### 3.1 计数排序

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int cnt[3] = {0, 0, 0};
        for (int x : nums) ++cnt[x];

        int k = 0;
        for (int v = 0; v < 3; ++v)
            while (cnt[v]--) nums[k++] = v;
    }
};
```

### 3.2 三指针

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0, i = 0, r = (int)nums.size() - 1;

        while (i <= r) {
            if (nums[i] == 0)      swap(nums[l++], nums[i++]);
            else if (nums[i] == 2) swap(nums[i], nums[r--]);
            else                   ++i;
        }
    }
};
```

## 4. 复杂度

- 时间：`O(n)`。
- 空间：`O(1)`。

## 5. 边界与坑

> [!warning] 坑 1：三指针里 `i` 和 `r` 交换后不能 `++i`
> 换过来的数还没检查，要停在原地再判一次。

> [!warning] 坑 2：计数数组开小
> 只有 0/1/2，开 3 就够；别按最大值开。

> [!warning] 坑 3：原地要求
> 题目要求原地修改，不能返回新数组。

> [!warning] 坑 4：全是同一种颜色
> 循环仍能正常结束，不用特判。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[P1177 排序]] | 通用排序 |
| [LeetCode 912 排序数组](https://leetcode.cn/problems/sort-an-array/) | 手写排序 |
| [LeetCode 1122 数组的相对排序](https://leetcode.cn/problems/relative-sort-array/) | 自定义顺序 + 计数 |

## 7. 关联

- 专题：[[07 排序]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 912 排序数组]]

---

嘿嘿，三个颜色而已，数一数再写回去，比荷兰国旗省脑子。
