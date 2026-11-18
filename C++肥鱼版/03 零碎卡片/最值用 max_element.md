---
title: 最值用 max_element
type: 卡片
topic: STL
tags: [C++, 零碎/STL, 类型/卡片, 难度/入门]
source: ["C++/零碎/最值设置.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 最值用 max_element.md -->

## 结论

`max_element` 返回**迭代器**，要解引用才拿到值；空区间是未定义行为。

## 语法 / 签名

`*max_element(v.begin(), v.end());`

## 最小示例

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v{3, 1, 4, 1, 5};
    cout << *max_element(v.begin(), v.end()) << '\n';   // 5
    cout << *min_element(v.begin(), v.end()) << '\n';   // 1
}
```

## 坑

1. 忘了 `*`，输出的是迭代器地址。
2. 空容器调用是未定义行为。
3. 要下标用 `max_element(...) - v.begin()`。

## 相关

- [[01-07 STL 容器]]
