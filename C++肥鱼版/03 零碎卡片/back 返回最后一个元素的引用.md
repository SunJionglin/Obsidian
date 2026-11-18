---
title: back 返回最后一个元素的引用
type: 卡片
topic: STL
tags: [C++, 零碎/STL, 类型/卡片, 难度/入门]
source: ["C++/零碎/返回容器中最后一个元素的引用.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: back 返回最后一个元素的引用.md -->

## 结论

`v.back()` 返回引用，可读可改；空容器调用是未定义行为。

## 语法 / 签名

`v.back(); v.front();`

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2, 3};
    v.back() = 9;
    cout << v.back() << '\n';   // 9
}
```

## 坑

1. 空容器调 `back()` 是未定义行为。
2. `v.end()` 是尾后迭代器，`*(v.end()-1)` 才是最后一个。
3. `vector<bool>` 是特化，`back()` 返回代理对象。

## 相关

- [[01-07 STL 容器]]
