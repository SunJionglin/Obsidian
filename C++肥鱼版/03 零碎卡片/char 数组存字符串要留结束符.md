---
title: char 数组存字符串要留结束符
type: 卡片
topic: 字符串
tags: [C++, 零碎/字符串, 类型/卡片, 难度/入门]
source: ["C++/零碎/char在数组中储存多个字符.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: char 数组存字符串要留结束符.md -->

## 结论

C 字符串以 `'\0'` 结尾，数组长度至少是「字符数 + 1」。

## 语法 / 签名

`char s[6] = "hello";`

## 最小示例

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char s[6] = "hello";      // 5 个字符 + '\0'
    cout << strlen(s) << '\n';   // 5
}
```

## 坑

1. 不留 `'\0'`，`strlen` 会一直往后读。
2. 中文字符占多个字节，别按「字的个数」开数组。
3. 现代 C++ 用 `std::string`。

## 相关

- [[01-08 头文件速查]]
- [[01-02 数组与结构体]]
