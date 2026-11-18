---
title: auto 会丢引用，要引用写 auto&
type: 卡片
topic: 类型
tags: [C++, 零碎/语法, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/auto& n.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: auto 会丢引用，要引用写 auto&.md -->

## 结论

`auto x = ...` 是**拷贝**；要改原对象写 `auto&`，只读遍历写 `const auto&`。

## 语法 / 签名

```cpp
auto x = v[0];          // 拷贝
auto& r = v[0];         // 引用
const auto& c = v[0];   // 常引用，不拷贝也不能改
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2, 3};

    for (auto& x : v) x *= 2;            // 改原元素
    for (const auto& x : v) cout << x << ' ';   // 2 4 6
}
```

## 坑

1. `for (auto x : v) x *= 2;` 改的是副本，原容器不变。
2. `auto&` 不能绑定临时量；`const auto&` 可以。
3. `auto` 会丢掉顶层 `const`，需要保留就写 `const auto`。

## 相关

- [[01-07 STL 容器]]
- [[01-10 模板与泛型]]
