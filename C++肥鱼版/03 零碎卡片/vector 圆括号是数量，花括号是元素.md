---
title: vector 圆括号是数量，花括号是元素
type: 卡片
topic: STL
tags: [C++, 零碎/容器, 类型/卡片, 难度/入门]
source: ["C++/零碎/动态数组初始化.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: vector 圆括号是数量，花括号是元素.md -->

## 结论

`vector<int> v(n)` 是 **n 个 0**；`vector<int> v{n}` 是 **1 个 n**。括号不同，结果天差地别。

## 语法 / 签名

```cpp
vector<int> a(3);        // {0, 0, 0}
vector<int> b{3};        // {3}
vector<int> c(3, 7);     // {7, 7, 7}
vector<int> d{3, 7};     // {3, 7}
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a(3);
    vector<int> b{3};

    cout << a.size() << ' ' << b.size() << '\n';   // 3 1
    cout << b[0] << '\n';                          // 3
}
```

## 坑

1. `vector<int> v{10}` 只有一个元素 10，不是 10 个 0。
2. 二维初始化：`vector<vector<int>> g(n, vector<int>(m, 0));`
3. `vector<int> v(n, 0)` 和 `v(n)` 等价，但写清楚更好。

## 相关

- [[01-07 STL 容器]]
- [[01-02 数组与结构体]]
