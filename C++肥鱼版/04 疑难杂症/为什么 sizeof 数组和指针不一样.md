---
title: 为什么 sizeof 数组和指针不一样
type: 疑难
topic: 类型
tags: [C++, 疑难/类型, 类型/Q&A, 难度/入门]
source: ["C++/疑难杂症/关于.size和sizeof()的区别.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 为什么 sizeof 数组和指针不一样.md -->

## 现象

同一个数组，在 main 里 `sizeof` 是 40，在函数里是 8。

## 最小复现

```cpp
int a[10];
cout << sizeof(a) << '\n';        // 40
cout << sizeof(&a[0]) << '\n';    // 8
```

## 原因

`sizeof` 看的是静态类型；数组名在函数参数位置退化成指针。

## 结论

`sizeof(数组)` 和 `sizeof(指针)` 不是一回事。

## 预防

用 `size()` / `sizeof(a)/sizeof(a[0])`（仅限本作用域数组）。

## 相关

- [[sizeof 是字节数，size 是元素个数]]
