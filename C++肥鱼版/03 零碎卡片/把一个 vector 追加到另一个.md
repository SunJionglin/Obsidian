---
title: 把一个 vector 追加到另一个
type: 卡片
topic: STL
tags: [C++, 零碎/STL, 类型/卡片, 难度/入门]
source: ["C++/零碎/将另一个 `vector<int>` 中的所有元素添加到当前 `vector` 中.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 把一个 vector 追加到另一个.md -->

## 结论

用 `insert` 的区间版本；C++23 起有 `append_range`。

## 语法 / 签名

`v.insert(v.end(), w.begin(), w.end());`

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2}, w{3, 4};
    v.insert(v.end(), w.begin(), w.end());

    for (int x : v) cout << x << ' ';   // 1 2 3 4
}
```

## 坑

1. 自己追加自己会迭代器失效。
2. 频繁追加先 `reserve`。
3. `v = v + w` 也能写，但会多一次拷贝。

## 相关

- [[01-07 STL 容器]]
