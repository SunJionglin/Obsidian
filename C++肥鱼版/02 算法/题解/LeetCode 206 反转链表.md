---
title: LeetCode 206 反转链表
type: 题解
topic: 递推与递归
tags: [C++, 算法/递归, 类型/题解, 难度/进阶]
from: "[[03 递推与递归]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [206, Reverse Linked List]
---

<!-- filename: LeetCode 206 反转链表.md -->

专题：[[03 递推与递归]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 206](https://leetcode.cn/problems/reverse-linked-list/) |
| 专题 | [[03 递推与递归]] |
| 难度 | ⭐⭐ |
| 一句话 | 反转单链表，返回新头节点 |

## 1. 题意与输入输出

给单链表头节点 `head`，反转后返回新头。

- 输入：`1 -> 2 -> 3 -> 4 -> 5`
- 输出：`5 -> 4 -> 3 -> 2 -> 1`
- 节点数范围：`[0, 5000]`

## 2. 思路

递归三步：

1. **终止条件**：空链表或只有一个节点，直接返回。
2. **信任下一层**：先把 `head->next` 之后的部分反转好，得到 `newHead`。
3. **处理当前层**：让 `head->next` 的 `next` 指回 `head`，再把 `head->next` 置空。

关键代码只有两行：

```text
head->next->next = head;
head->next = nullptr;
```

## 3. 代码

```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* newHead = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return newHead;
    }
};
```

## 4. 复杂度

- 时间：`O(n)`，每个节点访问一次。
- 空间：`O(n)`，递归栈。

## 5. 边界与坑

> [!warning] 坑 1：空链表
> `!head` 直接返回，别访问 `head->next`。

> [!warning] 坑 2：只有一个节点
> `!head->next` 直接返回，否则会自己指自己。

> [!warning] 坑 3：忘记置空
> 新尾巴的 `next` 必须设 `nullptr`，否则成环。

> [!warning] 坑 4：返回错节点
> 要返回 `newHead`，不是 `head`——`head` 已经是尾巴了。

> [!warning] 坑 5：递归深度
> 节点 5000 时递归没问题；10 万节点要改迭代。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 92 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) | 只反转一段，先找前驱 |
| [LeetCode 24 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 递归处理相邻节点 |
| [LeetCode 234 回文链表](https://leetcode.cn/problems/palindrome-linked-list/) | 反转后半段再比较 |

## 7. 关联

- 专题：[[03 递推与递归]]
- Python 版：[[01-反转链表]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 509 斐波那契数]]
- 下一题：[[LeetCode 118 杨辉三角]]

---

哼，这题的精髓就两行：让下一个指回来，再把自己断开。
