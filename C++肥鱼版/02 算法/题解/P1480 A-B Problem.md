---
title: P1480 A/B Problem
type: 题解
topic: 高精度
tags: [C++, 算法/高精度, 类型/题解, 难度/进阶]
from: "[[06 高精度]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [P1480, 高精度除法]
---

<!-- filename: P1480 A/B Problem.md -->

专题：[[06 高精度]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [洛谷 P1480](https://www.luogu.com.cn/problem/P1480) |
| 专题 | [[06 高精度]] |
| 难度 | ⭐⭐⭐ |
| 一句话 | 大整数除以大整数，求整数商 |

## 1. 题意与输入输出

输入两个正整数 `a`、`b`，输出 `a / b` 的整数部分。

- 输入：`10 3`
- 输出：`3`
- 数据范围：`a` 位数较多，`long long` 存不下

## 2. 思路

模拟竖式长除法：

1. 从高位到低位，每次把一位接到余数 `rem` 后面。
2. 用 `rem` 反复减 `b`，减几次商就是几（最多 9 次）。
3. 余数留到下一轮。

如果除数是单精度（`int`），直接用 `06 高精度` 里的 2.4 模板，`O(n)` 更快。

## 3. 代码

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool ge(string a, string b) {
    if (a.size() != b.size()) return a.size() > b.size();
    return a >= b;
}

string sub(string a, string b) {
    string res;
    int i = (int)a.size() - 1, j = (int)b.size() - 1, borrow = 0;
    while (i >= 0) {
        int x = a[i--] - '0' - borrow;
        int y = (j >= 0) ? b[j--] - '0' : 0;
        if (x < y) { x += 10; borrow = 1; }
        else borrow = 0;
        res.push_back(char('0' + x - y));
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

string divBig(string a, string b) {
    string res, rem;

    for (char ch : a) {
        rem += ch;

        int k = 0;
        while (k + 1 < (int)rem.size() && rem[k] == '0') ++k;
        rem = rem.substr(k);

        int q = 0;
        while (ge(rem, b)) {
            rem = sub(rem, b);
            ++q;
        }
        res.push_back(char('0' + q));
    }

    int k = 0;
    while (k + 1 < (int)res.size() && res[k] == '0') ++k;
    return res.substr(k);
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << divBig(a, b) << '\n';
    return 0;
}
```

## 4. 复杂度

- 时间：`O(n * 9 * m)`，n 为被除数位数，m 为除数位数。
- 空间：`O(n + m)`。

## 5. 边界与坑

> [!warning] 坑 1：除数为 0
> 题目保证 `b > 0`；工程代码要特判。

> [!warning] 坑 2：被除数小于除数
> 商是 `0`，去前导零后只剩一个 `0`。

> [!warning] 坑 3：余数前导零
> 每轮拼接后要去掉前导零，否则 `ge` 比较会出错。

> [!warning] 坑 4：商的前导零
> 最后统一去掉，但 `0` 本身要保留。

> [!warning] 坑 5：单精度除法
> 如果 `b` 能用 `int` 存，别用这个 `O(n*m)` 版本，改用 2.4 模板。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [[P2142 高精度减法]] | 除法内部的「反复减」 |
| [[P1601 A+B Problem（高精）]] | 加减乘除四件套 |
| [LeetCode 29 两数相除](https://leetcode.cn/problems/divide-two-integers/) | 倍增减法 |

## 7. 关联

- 专题：[[06 高精度]]
- 原始笔记：无（生成例题）
- 上一题：[[P2142 高精度减法]]

---

哼，除法就是「能减就减，减不动就换下一位」。
