---
title: LeetCode 912 排序数组
type: 题解
topic: 排序
tags: [C++, 算法/排序, 类型/题解, 难度/进阶]
from: "[[07 排序]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [912, Sort an Array]
---

<!-- filename: LeetCode 912 排序数组.md -->

专题：[[07 排序]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 912](https://leetcode.cn/problems/sort-an-array/) |
| 专题 | [[07 排序]] |
| 难度 | ⭐⭐ |
| 一句话 | 手写排序，把数组升序排好 |

## 1. 题意与输入输出

给整数数组 `nums`，升序排序并返回。

- 输入：`nums = [5,2,3,1]`
- 输出：`[1,2,3,5]`
- 数据范围：`1 <= nums.length <= 5*10^4`，`-5*10^4 <= nums[i] <= 5*10^4`
- 要求：`O(n log n)`，不能直接用库函数（面试口径）

## 2. 思路

面试让手写时，优先写**归并排序**：

- 稳定，最坏 `O(n log n)`。
- 分治：排左半、排右半、合并两个有序数组。

如果允许库函数，`sort` 一行解决；但面试官通常想看你写 `merge`。

## 3. 代码

### 3.1 归并排序

```cpp
#include <vector>
using namespace std;

class Solution {
    void mergeSort(vector<int>& a, vector<int>& tmp, int l, int r) {
        if (l >= r) return;

        int mid = l + (r - l) / 2;
        mergeSort(a, tmp, l, mid);
        mergeSort(a, tmp, mid + 1, r);

        int i = l, j = mid + 1, k = l;
        while (i <= mid && j <= r)
            tmp[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
        while (i <= mid) tmp[k++] = a[i++];
        while (j <= r) tmp[k++] = a[j++];

        for (int p = l; p <= r; ++p) a[p] = tmp[p];
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> tmp(nums.size());
        mergeSort(nums, tmp, 0, (int)nums.size() - 1);
        return nums;
    }
};
```

### 3.2 库函数版

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
};
```

## 4. 复杂度

- 归并：时间 `O(n log n)`，空间 `O(n)`。
- `sort`：时间 `O(n log n)`，空间 `O(log n)` 栈。

## 5. 边界与坑

> [!warning] 坑 1：归并的临时数组
> 每层都新建 `vector` 会拖慢；开一个全局 `tmp` 复用。

> [!warning] 坑 2：合并时 `<=`
> 用 `<=` 才能保证稳定；`<` 会打乱相等元素的相对顺序。

> [!warning] 坑 3：递归边界
> `l >= r` 返回，别写成 `l > r` 导致死递归。

> [!warning] 坑 4：只写 `sort`
> 面试要求手写时，`sort` 会被判「不合格」。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[P1177 排序]] | 同样的排序，洛谷版 |
| [LeetCode 148 排序链表](https://leetcode.cn/problems/sort-list/) | 归并排序链表版 |
| [LeetCode 75 颜色分类](https://leetcode.cn/problems/sort-colors/) | 计数/三指针 |

## 7. 关联

- 专题：[[07 排序]]
- 原始笔记：`C++/零碎/冒泡排序.md`
- 上一题：[[P1177 排序]]

---

哼，归并排序就是「先分家，再合并」——跟本鱼分白饭一个道理。
