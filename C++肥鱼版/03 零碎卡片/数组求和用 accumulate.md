---
title: 数组求和用 accumulate
type: 卡片
topic: STL
tags: [C++, 零碎/STL, 类型/卡片, 难度/入门]
source: ["C++/零碎/数组求和.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 数组求和用 accumulate.md -->

## 结论

`accumulate(begin, end, 0)` 一行求和；初值类型决定结果类型，防溢出用 `0LL`。

## 语法 / 签名

`accumulate(v.begin(), v.end(), 0);`

## 最小示例

```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    vector<int> v{1, 2, 3, 4};
    cout << accumulate(v.begin(), v.end(), 0) << '\n';   // 10
    cout << accumulate(v.begin(), v.end(), 0LL) << '\n'; // 10
}
```

## 坑

1. 初值写 `0` 是 int，累加超 21 亿会溢出。
2. 空区间返回初值。
3. 需要 `<numeric>`。

## 相关

- [[01-07 STL 容器]]
- [[01-08 头文件速查]]
