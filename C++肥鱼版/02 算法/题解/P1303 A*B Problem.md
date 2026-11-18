---
title: P1303 A*B Problem
type: 题解
topic: 高精度
tags: [C++, 算法/高精度, 类型/题解, 难度/进阶]
from: "[[06 高精度]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [P1303, 高精度乘法]
---

<!-- filename: P1303 A*B Problem.md -->

专题：[[06 高精度]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [洛谷 P1303](https://www.luogu.com.cn/problem/P1303) |
| 专题 | [[06 高精度]] |
| 难度 | ⭐⭐⭐ |
| 一句话 | 两个大整数相乘 |

## 1. 题意与输入输出

输入两个非负大整数，输出乘积。

- 输入：`2 3`
- 输出：`6`
- 数据范围：位数较大，`long long` 存不下

## 2. 思路

竖式乘法：

- `a[i] * b[j]` 的结果累加到 `c[i+j+1]`。
- 全部乘完后，从低位到高位统一进位。
- 去掉前导零。

答案最多 `n + m` 位，数组开 `n + m`。

## 3. 代码

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string mul(string a, string b) {
    if (a == "0" || b == "0") return "0";

    vector<int> c(a.size() + b.size(), 0);

    for (int i = (int)a.size() - 1; i >= 0; --i)
        for (int j = (int)b.size() - 1; j >= 0; --j)
            c[i + j + 1] += (a[i] - '0') * (b[j] - '0');

    for (int i = (int)c.size() - 1; i > 0; --i) {
        c[i - 1] += c[i] / 10;
        c[i] %= 10;
    }

    int k = 0;
    while (k < (int)c.size() - 1 && c[k] == 0) ++k;

    string res;
    for (; k < (int)c.size(); ++k) res.push_back(char('0' + c[k]));
    return res;
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << mul(a, b) << '\n';
    return 0;
}
```

## 4. 复杂度

- 时间：`O(n*m)`。
- 空间：`O(n+m)`。

## 5. 边界与坑

> [!warning] 坑 1：数组开成 `n + m - 1`
> 结果最多 `n + m` 位，少开一位会越界。

> [!warning] 坑 2：没统一进位
> 只算 `c[i+j+1]` 不处理进位，输出会出现大于 9 的数字。

> [!warning] 坑 3：前导零
> 最高位可能是 0，要从第一个非零位开始输出。

> [!warning] 坑 4：乘 0
> 直接返回 `"0"`，否则会输出一串 0。

> [!warning] 坑 5：`char` 与 `int` 混用
> `c` 是 `vector<int>`，最后输出时再转 `char`。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 43 字符串相乘](https://leetcode.cn/problems/multiply-strings/) | 同一套竖式乘法 |
| [LeetCode 2 两数相加](https://leetcode.cn/problems/add-two-numbers/) | 加法版 |
| [[P1601 A+B Problem（高精）]] | 先练加法再练乘法 |

## 7. 关联

- 专题：[[06 高精度]]
- 原始笔记：无（生成例题）
- 上一题：[[P1601 A+B Problem（高精）]]

---

呜……本鱼第一次写乘法，数组少开一位，最后一个测试点直接炸。
