---
title: LeetCode 1483 树节点的第 K 个祖先
type: 题解
topic: 倍增
tags: [C++, 算法/倍增, 类型/题解, 难度/进阶]
from: "[[05 倍增]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [1483, Kth Ancestor of a Tree Node]
---

<!-- filename: LeetCode 1483 树节点的第 K 个祖先.md -->

专题：[[05 倍增]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 1483](https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/) |
| 专题 | [[05 倍增]] |
| 难度 | ⭐⭐⭐ |
| 一句话 | 多次查询「节点 node 的第 k 个祖先」 |

## 1. 题意与输入输出

给 `n` 个节点的树，`parent[i]` 是节点 i 的父节点（根为 -1）。多次查询 `(node, k)`，返回第 k 个祖先，不存在返回 -1。

- 输入：`parent = [-1,0,0,1,1,2,2]`，查询 `(3,1)`、`(5,2)`、`(6,3)`
- 输出：`1`、`0`、`-1`
- 数据范围：`n <= 5*10^4`，查询次数 `<= 5*10^4`

## 2. 思路

暴力往上跳 `k` 步是 `O(k)`，查询多了就超时。

**倍增表**：`up[i][j]` 表示节点 i 的第 `2^j` 个祖先。

- `up[i][0] = parent[i]`
- `up[i][j] = up[ up[i][j-1] ][j-1]`

查询时把 `k` 二进制拆分，哪一位是 1 就跳 `2^j` 步。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class TreeAncestor {
    vector<vector<int>> up;
    int LOG;

public:
    TreeAncestor(int n, vector<int>& parent) {
        LOG = 1;
        while ((1 << LOG) <= n) ++LOG;

        up.assign(n, vector<int>(LOG, -1));
        for (int i = 0; i < n; ++i) up[i][0] = parent[i];

        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                int mid = up[i][j - 1];
                up[i][j] = (mid == -1) ? -1 : up[mid][j - 1];
            }
        }
    }

    int getKthAncestor(int node, int k) {
        for (int j = 0; j < LOG && node != -1; ++j) {
            if (k & (1 << j)) {
                node = up[node][j];
            }
        }
        return node;
    }
};
```

## 4. 复杂度

- 预处理：`O(n log n)`。
- 单次查询：`O(log n)`。
- 空间：`O(n log n)`。

## 5. 边界与坑

> [!warning] 坑 1：`k = 0`
> 返回节点自己，循环里没有位是 1，自然返回 `node`。

> [!warning] 坑 2：祖先不够
> 跳到 -1 后要停，不能再查 `up[-1]`。

> [!warning] 坑 3：`LOG` 开小
> `n = 5e4` 时 `LOG` 至少 16；用 `while ((1 << LOG) <= n)` 自动算。

> [!warning] 坑 4：根节点
> `parent[root] = -1`，`up[root][0] = -1`，正常。

> [!warning] 坑 5：查询次数多
> 每次 `O(log n)`，5 万次也就 80 万步，没问题。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| LCA 最近公共祖先 | 倍增表 + 深度对齐 |
| [[P3865 ST 表]] | 同为 2^k 预处理 |
| [LeetCode 235/236 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 树上的祖先问题 |

## 7. 关联

- 专题：[[05 倍增]]
- 原始笔记：无（生成例题）
- 上一题：[[P3865 ST 表]]

---

嘿嘿，倍增表一建，查祖先就像坐电梯：按二进制楼层停。
