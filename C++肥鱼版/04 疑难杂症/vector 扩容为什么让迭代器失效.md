---
title: vector 扩容为什么让迭代器失效
type: 疑难
topic: STL
tags: [C++, 疑难/STL, 类型/Q&A, 难度/进阶]
source: ["C++/系统/细节/头文件/vector.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: vector 扩容为什么让迭代器失效.md -->

## 现象

`push_back` 之后，之前保存的迭代器/指针/引用全乱了。

## 最小复现

```cpp
vector<int> v{1,2,3};
int* p = &v[0];
v.push_back(4);      // 可能扩容
cout << *p;          // 悬空
```

## 原因

扩容会重新分配内存，旧地址全部失效。

## 结论

扩容后旧迭代器、指针、引用都不能再用。

## 预防

提前 `reserve`，或扩容后重新获取。

## 相关

- [[01-07 STL 容器]]
