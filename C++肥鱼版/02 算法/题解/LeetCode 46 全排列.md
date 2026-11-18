---
title: LeetCode 46 全排列
type: 题解
topic: 搜索
tags: [C++, 算法/搜索, 类型/题解, 难度/进阶]
from: "[[08 搜索]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [46, Permutations, 回溯]
---

<!-- filename: LeetCode 46 全排列.md -->

专题：[[08 搜索]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 46](https://leetcode.cn/problems/permutations/) |
| 专题 | [[08 搜索]] |
| 难度 | ⭐⭐ |
| 一句话 | 输出数组的所有排列 |

## 1. 题意与输入输出

给不含重复数字的数组，返回所有全排列。

- 输入：`nums = [1,2,3]`
- 输出：`[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`
- 数据范围：`1 <= nums.length <= 6`

## 2. 思路

回溯三件套：

1. **选择**：从没用过的数里挑一个。
2. **递归**：把它加入 `path`，继续填下一位。
3. **撤销**：`path.pop_back()`、`used[i] = false`。

当 `path.size() == n` 时，收集答案。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
    void dfs(vector<int>& nums, vector<bool>& used,
             vector<int>& path, vector<vector<int>>& ans) {
        if (path.size() == nums.size()) {
            ans.push_back(path);
            return;
        }

        for (int i = 0; i < (int)nums.size(); ++i) {
            if (used[i]) continue;

            used[i] = true;
            path.push_back(nums[i]);

            dfs(nums, used, path, ans);

            path.pop_back();       // 撤销
            used[i] = false;
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        dfs(nums, used, path, ans);
        return ans;
    }
};
```

## 4. 复杂度

- 时间：`O(n * n!)`，共 `n!` 个排列，每个复制 `O(n)`。
- 空间：`O(n)` 递归栈，不算答案。

## 5. 边界与坑

> [!warning] 坑 1：忘记撤销
> `path.pop_back()` 和 `used[i] = false` 少一个，后面的排列就乱了。

> [!warning] 坑 2：答案重复
> 本题元素不重复；有重复元素（47 题）要先排序再跳过同层重复。

> [!warning] 坑 3：递归终止条件
> 是 `path.size() == n`，不是 `start == n`。

> [!warning] 坑 4：传参拷贝
> `path` 用引用传，`ans.push_back(path)` 时才复制。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 47 全排列 II](https://leetcode.cn/problems/permutations-ii/) | 有重复元素，要剪枝 |
| [LeetCode 78 子集](https://leetcode.cn/problems/subsets/) | 回溯选/不选 |
| [LeetCode 79 单词搜索](https://leetcode.cn/problems/word-search/) | 网格回溯 |

## 7. 关联

- 专题：[[08 搜索]]
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 733 图像渲染]]
- 下一题：[[LeetCode 198 打家劫舍]]

---

呜……本鱼第一次写回溯，忘了撤销 `used`，输出里全是重复排列。
