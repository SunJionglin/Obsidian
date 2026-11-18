---
title: char 是否有符号由实现决定
type: 卡片
topic: 类型
tags: [C++, 零碎/类型, 类型/卡片, 难度/进阶]
source: ["C++/零碎/char.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: char 是否有符号由实现决定.md -->

## 结论

`char` 的符号性由编译器决定；需要明确就写 `signed char` / `unsigned char`。

## 语法 / 签名

`signed char` / `unsigned char`

## 最小示例

```cpp
#include <iostream>
using namespace std;

int main() {
    char c = 200;                 // 可能是 -56，也可能是 200
    unsigned char u = 200;        // 一定是 200
    cout << (int)c << ' ' << (int)u << '\n';
}
```

## 坑

1. 把 UTF-8 中文塞进 `char` 会变负数。
2. 比较/哈希前转 `unsigned char`。
3. `char`、`int8_t`、`uint8_t` 别混用。

## 相关

- [[01-01 基础语法与运算符]]
