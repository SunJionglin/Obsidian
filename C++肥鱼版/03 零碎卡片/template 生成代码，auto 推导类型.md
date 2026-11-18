---
title: template 生成代码，auto 推导类型
type: 卡片
topic: 模板
tags: [C++, 零碎/模板, 类型/卡片, 难度/进阶]
source: ["C++/零碎/函数/template与auto区别.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: template 生成代码，auto 推导类型.md -->

## 结论

`template` 在编译期为不同类型生成函数/类；`auto` 只推导变量类型，不生成代码。

## 语法 / 签名

`template <typename T> ...` / `auto x = ...;`

## 最小示例

```cpp
#include <iostream>
using namespace std;

template <typename T>
T add(T a, T b) { return a + b; }

int main() {
    auto x = add(1, 2);       // int
    auto y = add(1.5, 2.5);   // double
    cout << x << ' ' << y << '\n';
}
```

## 坑

1. `auto` 会丢引用和 `const`。
2. 模板定义要放头文件。
3. `auto` 推导不出「想要」的类型时，显式写出来。

## 相关

- [[01-10 模板与泛型]]
