---
title: 浮点字面量默认是 double
type: 卡片
topic: 类型
tags: [C++, 零碎/类型, 类型/卡片, 难度/入门]
source: ["C++/零碎/关于默认为double类型的更改.md", "C++/零碎/科学记数法.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 浮点字面量默认是 double.md -->

## 结论

`3.14`、`1e3` 默认都是 `double`；要 `float` 必须加后缀 `f`，否则可能窄化。

## 语法 / 签名

```cpp
float  f = 3.14f;
double d = 3.14;
long double ld = 3.14L;
```

## 最小示例

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float f = 3.14f;
    double d = 1e-3;

    cout << fixed << setprecision(10) << d << '\n';   // 0.0010000000
    cout << f << '\n';                                 // 3.14
}
```

## 坑

1. `float f = 3.14;` 会有窄化警告，加 `f`。
2. `cout` 默认只输出 6 位有效数字，要更多用 `setprecision`。
3. 科学计数法 `1e3` 是 `double` 的 1000，不是整数。

## 相关

- [[01-01 基础语法与运算符]]
- [[浮点数不能直接用等号比较]]
