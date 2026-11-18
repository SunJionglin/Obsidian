---
title: 字符运算依赖 ASCII 码
type: 卡片
topic: 字符串
tags: [C++, 零碎/字符串, 类型/卡片, 难度/入门]
source: ["C++/零碎/利用ASCLL码，使6+‘0’实现整形6向字符6的转变.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 字符运算依赖 ASCII 码.md -->

## 结论

`'0'` 是 48；数字转字符 `'0' + n`，字符转数字 `c - '0'`。

## 语法 / 签名

`char c = '0' + 6; int n = c - '0';`

## 最小示例

```cpp
#include <iostream>
using namespace std;

int main() {
    char c = '0' + 6;
    int n = c - '0';
    cout << c << ' ' << n << '\n';   // 6 6
}
```

## 坑

1. 只对 `'0'..'9'` 有效。
2. 大小写差 32：`'a' - 'A'`。
3. 别依赖非 ASCII 编码（如 EBCDIC）。

## 相关

- [[01-01 基础语法与运算符]]
