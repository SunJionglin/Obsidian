---
title: LeetCode 509 斐波那契数
type: 题解
topic: 递推与递归
tags: [C++, 算法/递归, 类型/题解, 难度/入门]
from: "[[03 递推与递归]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [509, Fibonacci Number]
---

<!-- filename: LeetCode 509 斐波那契数.md -->

专题：[[03 递推与递归]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 509](https://leetcode.cn/problems/fibonacci-number/) |
| 专题 | [[03 递推与递归]] |
| 难度 | ⭐ |
| 一句话 | 求第 n 个斐波那契数 |

## 1. 题意与输入输出

`F(0) = 0`，`F(1) = 1`，`F(n) = F(n-1) + F(n-2)`，求 `F(n)`。

- 输入：`n = 4`
- 输出：`3`
- 数据范围：`0 <= n <= 30`

## 2. 思路

三种写法：

1. **朴素递归**：直接翻译定义，但重复计算严重，`O(2^n)`。
2. **记忆化**：递归 + 数组缓存，`O(n)`。
3. **递推**：从小到大算，`O(n)`，空间可压到 `O(1)`。

`n <= 30` 时朴素递归也能过，但这是练「记忆化」的最好例子。

## 3. 代码

### 3.1 朴素递归

```cpp
class Solution {
public:
    int fib(int n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
};
```

### 3.2 记忆化

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int fib(int n) {
        vector<int> memo(n + 1, -1);
        return dfs(n, memo);
    }

    int dfs(int n, vector<int>& memo) {
        if (n <= 1) return n;
        if (memo[n] != -1) return memo[n];
        return memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo);
    }
};
```

### 3.3 递推（滚动变量）

```cpp
class Solution {
public:
    int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; ++i) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```

## 4. 复杂度

| 写法 | 时间 | 空间 |
|---|---|---|
| 朴素递归 | `O(2^n)` | `O(n)` 栈 |
| 记忆化 | `O(n)` | `O(n)` |
| 递推 | `O(n)` | `O(1)` |

## 5. 边界与坑

> [!warning] 坑 1：`n = 0`
> 返回 0，别让数组开成 `memo[0]` 后越界。

> [!warning] 坑 2：记忆化数组初始化
> 用 `-1` 表示没算过；如果结果可能是 -1，就换个标记。

> [!warning] 坑 3：递归深度
> `n = 30` 没问题；`n = 1e5` 会栈溢出，必须改递推。

> [!warning] 坑 4：重复计算
> 朴素递归算 `fib(30)` 要调用约 270 万次，别在生产里这么写。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[LeetCode 70 爬楼梯]] | 同一个递推式 |
| [LeetCode 1137 第 N 个泰波那契数](https://leetcode.cn/problems/n-th-tribonacci-number/) | 三项递推 |
| [LeetCode 746 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/) | 递推 + 取 min |

## 7. 关联

- 专题：[[03 递推与递归]]
- 原始笔记：`C++/算法/算法题/（重点）斐波那契数列计算常见错误笔记.md`
- 上一题：[[LeetCode 70 爬楼梯]]
- 下一题：[[LeetCode 206 反转链表]]

---

呜……本鱼当年用朴素递归算 fib(40)，电脑风扇转得像要起飞。
