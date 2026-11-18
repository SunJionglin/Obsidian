---
title: enum class 比普通 enum 更安全
type: 卡片
topic: 语法
tags: [C++, 零碎/语法, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/enum.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: enum class 比普通 enum 更安全.md -->

## 结论

普通 `enum` 会隐式转 `int`、名字泄漏到外层作用域；`enum class` 有作用域、不隐式转换。

## 语法 / 签名

```cpp
enum Color { RED, GREEN };              // 普通
enum class Fruit { APPLE, BANANA };     // 强类型
```

## 最小示例

```cpp
#include <iostream>
using namespace std;

enum class Fruit { APPLE, BANANA };

int main() {
    Fruit f = Fruit::APPLE;

    if (f == Fruit::APPLE) cout << "apple\n";

    // int x = f;   // 错误：不隐式转换
    int x = static_cast<int>(f);
    cout << x << '\n';   // 0
}
```

## 坑

1. 普通 `enum` 的两个枚举名不能重复（同一作用域）。
2. `enum class` 取值要写 `Fruit::APPLE`。
3. 需要转 `int` 时用 `static_cast`，别 C 风格强转。

## 相关

- [[01-01 基础语法与运算符]]
- [[01-06 类与对象]]
