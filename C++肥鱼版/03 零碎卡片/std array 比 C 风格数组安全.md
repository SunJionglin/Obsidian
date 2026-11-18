---
title: std array 比 C 风格数组安全
type: 卡片
topic: 数组
tags: [C++, 零碎/数组, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/C 风格数组与 `std ：：array` 对照笔记.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: std array 比 C 风格数组安全.md -->

## 结论

`std::array` 定长、能赋值、有 `size()`、不退化；C 风格数组一传参就变指针。

## 语法 / 签名

```cpp
array<int, 4> a{1, 2, 3, 4};
a.size();          // 4
a[0]; a.at(0);     // at 会检查越界
```

## 最小示例

```cpp
#include <iostream>
#include <array>
using namespace std;

int main() {
    array<int, 4> a{1, 2, 3, 4};

    cout << a.size() << '\n';       // 4
    for (int x : a) cout << x << ' ';
}
```

## 坑

1. `array` 在栈上，开太大（比如几百万元素）会爆栈。
2. 传参要写 `array<int, 4>&`，长度是类型的一部分。
3. 别忘了 `#include <array>`。

## 相关

- [[01-02 数组与结构体]]
- [[01-07 STL 容器]]
