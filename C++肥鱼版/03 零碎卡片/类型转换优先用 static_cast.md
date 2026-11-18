---
title: 类型转换优先用 static_cast
type: 卡片
topic: 语法
tags: [C++, 零碎/语法, 类型/卡片, 难度/入门]
source: ["C++/零碎/关于数据类型的转换.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 类型转换优先用 static_cast.md -->

## 结论

C++ 风格转换更明确：`static_cast` 管普通转换，`reinterpret_cast` 管指针，`dynamic_cast` 管多态向下转型。

## 语法 / 签名

`static_cast<int>(d)`

## 最小示例

```cpp
#include <iostream>
using namespace std;

int main() {
    double d = 3.9;
    int n = static_cast<int>(d);   // 3
    cout << n << '\n';
}
```

## 坑

1. C 风格 `(int)d` 不检查，别用。
2. `dynamic_cast` 失败返回 `nullptr`（指针）或抛异常（引用）。
3. 指针之间乱转用 `reinterpret_cast`，风险自负。

## 相关

- [[01-01 基础语法与运算符]]
