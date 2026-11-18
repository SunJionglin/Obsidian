---
title: nullptr 比 NULL 更安全
type: 卡片
topic: 类型
tags: [C++, 零碎/语法, 类型/卡片, 难度/入门]
source: ["C++/零碎/C++ 中nullptr详解.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: nullptr 比 NULL 更安全.md -->

## 结论

`nullptr` 有独立类型 `std::nullptr_t`，不会和整数 `0` 混淆；`NULL` 本质是 `0`。

## 语法 / 签名

```cpp
int* p = nullptr;
if (p == nullptr) { /* 空 */ }
```

## 最小示例

```cpp
#include <iostream>
using namespace std;

void f(int)    { cout << "int\n"; }
void f(char*)  { cout << "ptr\n"; }

int main() {
    // f(NULL);      // 可能二义，或被当成 int
    f(nullptr);      // 一定匹配 char*，输出 ptr
}
```

## 坑

1. 重载函数里 `NULL` 可能匹配到 `int` 版本，`nullptr` 不会。
2. `NULL` 需要 `<cstddef>`，`nullptr` 是关键字。
3. 删除后置空：`delete p; p = nullptr;`。

## 相关

- [[01-03 指针与引用]]
- [[01-05 内存分区]]
