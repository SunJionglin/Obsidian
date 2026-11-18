---
title: sizeof 是字节数，size 是元素个数
type: 卡片
topic: 类型
tags: [C++, 零碎/类型, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/sizeof ：获取数据类型或变量所占字节.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: sizeof 是字节数，size 是元素个数.md -->

## 结论

`sizeof` 算**字节数**（编译期），`size()` 算**元素个数**（运行期）。

## 语法 / 签名

```cpp
sizeof(类型);
sizeof(变量);
容器.size();
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a[10];
    cout << sizeof(a) / sizeof(a[0]) << '\n';   // 10

    vector<int> v(10);
    cout << v.size() << '\n';                   // 10
    cout << sizeof(v) << '\n';                  // 24（对象本身大小，不是 40）
}
```

## 坑

1. 数组传参后退化成指针，函数里 `sizeof(a)` 变成 8。
2. `sizeof` 是运算符，不是函数，括号可省（类型名不行）。
3. `size()` 返回无符号数，`size() - 1` 在空容器上会溢出。

## 相关

- [[01-02 数组与结构体]]
- [[01-07 STL 容器]]
