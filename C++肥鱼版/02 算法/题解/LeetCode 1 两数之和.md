---
title: LeetCode 1 两数之和
type: 题解
topic: 枚举与模拟
tags: [C++, 算法/枚举, 类型/题解, 难度/入门]
from: "[[01 枚举与模拟]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [1, Two Sum]
---

<!-- filename: LeetCode 1 两数之和.md -->

专题：[[01 枚举与模拟]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 1](https://leetcode.cn/problems/two-sum/) |
| 专题 | [[01 枚举与模拟]] |
| 难度 | ⭐ |
| 一句话 | 找两个数，和为 target |

## 1. 题意与输入输出

给定整数数组 `nums` 和 `target`，找出**两个**下标 `i != j`，使 `nums[i] + nums[j] == target`。保证恰好一个答案。

- 输入：`nums = [2,7,11,15]`，`target = 9`
- 输出：`[0,1]`
- 数据范围：`2 <= nums.length <= 10^4`

## 2. 思路

**暴力枚举**：枚举 `i`，再枚举 `j > i`，检查和。`O(n²)`，本题能过。

**优化**：边遍历边用哈希表存「值 → 下标」，查 `target - nums[i]` 是否出现过，`O(n)`。

先写对暴力，再想优化——这是枚举题的正确顺序。

## 3. 代码

### 3.1 暴力枚举

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = (int)nums.size();
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (nums[i] + nums[j] == target)
                    return {i, j};
        return {};
    }
};
```

### 3.2 哈希优化

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pos;
        for (int i = 0; i < (int)nums.size(); ++i) {
            auto it = pos.find(target - nums[i]);
            if (it != pos.end()) return {it->second, i};
            pos[nums[i]] = i;
        }
        return {};
    }
};
```

## 4. 复杂度

| 做法 | 时间 | 空间 |
|---|---|---|
| 暴力枚举 | `O(n²)` | `O(1)` |
| 哈希 | `O(n)` | `O(n)` |

## 5. 边界与坑

> [!warning] 坑 1：同一个元素用两次
> `nums = [3,3]`，`target = 6` 时答案 `[0,1]`；内层从 `i+1` 开始就不会重复用同一个下标。

> [!warning] 坑 2：先存后查
> 哈希法必须**先查再存**，否则 `[3,3]` 会把同一个下标查两次。

> [!warning] 坑 3：负数
> 题目有负数，哈希表照样能用，别假设都是正数。

> [!warning] 坑 4：返回顺序
> 题目接受任意顺序，一般返回 `{i, j}` 即可。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 167 两数之和 II](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | 数组有序，双指针 `O(n)` |
| [LeetCode 15 三数之和](https://leetcode.cn/problems/3sum/) | 排序 + 双指针，注意去重 |
| [LeetCode 454 四数相加 II](https://leetcode.cn/problems/4sum-ii/) | 分组 + 哈希计数 |

## 7. 关联

- 专题：[[01 枚举与模拟]]
- Python 版：[[01-两数之和]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 下一题：[[LeetCode 59 螺旋矩阵 II]]

---

哼，两数之和是枚举界的「Hello World」——写不对它，后面别谈了。
