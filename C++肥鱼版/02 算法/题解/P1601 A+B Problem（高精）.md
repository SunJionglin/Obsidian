---
title: P1601 A+B Problem（高精）
type: 题解
topic: 高精度
tags: [C++, 算法/高精度, 类型/题解, 难度/入门]
from: "[[06 高精度]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [P1601, 高精度加法]
---

<!-- filename: P1601 A+B Problem（高精）.md -->

专题：[[06 高精度]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [洛谷 P1601](https://www.luogu.com.cn/problem/P1601) |
| 专题 | [[06 高精度]] |
| 难度 | ⭐⭐ |
| 一句话 | 两个大整数相加，位数超过 long long |

## 1. 题意与输入输出

输入两个非负大整数 `a`、`b`，输出它们的和。

- 输入：`1 2`
- 输出：`3`
- 数据范围：位数可达 `10^500` 级别（以题目为准）

## 2. 思路

倒着存、逐位加、进位 `carry`。

从个位开始，两个数对应位相加再加进位，当前位是 `sum % 10`，新进位是 `sum / 10`。

## 3. 代码

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string add(string a, string b) {
    string res;
    int i = (int)a.size() - 1, j = (int)b.size() - 1, carry = 0;

    while (i >= 0 || j >= 0 || carry) {
        int x = (i >= 0) ? a[i--] - '0' : 0;
        int y = (j >= 0) ? b[j--] - '0' : 0;
        int s = x + y + carry;
        res.push_back(char('0' + s % 10));
        carry = s / 10;
    }

    reverse(res.begin(), res.end());
    return res;
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << add(a, b) << '\n';
    return 0;
}
```

## 4. 复杂度

- 时间：`O(n)`，n 为较大位数。
- 空间：`O(n)`。

## 5. 边界与坑

> [!warning] 坑 1：`carry` 最后忘了加
> `while` 条件要带 `|| carry`，否则最高位进位丢失。

> [!warning] 坑 2：字符串长度不同
> 短的那个用完就按 0 算，别直接越界访问。

> [!warning] 坑 3：前导零
> 输入可能有前导零，输出时最好去掉（`0` 本身保留）。

> [!warning] 坑 4：`char` 转换
> `res.push_back('0' + s % 10)`，别直接 push 整数。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 415 字符串相加](https://leetcode.cn/problems/add-strings/) | 同样的逐位加 |
| [LeetCode 2 两数相加](https://leetcode.cn/problems/add-two-numbers/) | 链表版 |
| [LeetCode 67 二进制求和](https://leetcode.cn/problems/add-binary/) | 二进制进位 |

## 7. 关联

- 专题：[[06 高精度]]
- 原始笔记：无（生成例题）
- 下一题：[[P1303 A*B Problem]]

---

哼，加法是高精度里最乖的，进位别忘了就行。
