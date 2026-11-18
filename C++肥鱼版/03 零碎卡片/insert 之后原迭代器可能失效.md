---
title: insert 之后原迭代器可能失效
type: 卡片
topic: STL
tags: [C++, 零碎/容器, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/insert.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: insert 之后原迭代器可能失效.md -->

## 结论

`insert` 在指定位置插入元素，返回**新元素**的迭代器；`vector` 插入后，插入点及之后的迭代器都可能失效。

## 语法 / 签名

```cpp
iterator insert(iterator pos, const T& value);
iterator insert(iterator pos, InputIt first, InputIt last);
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2, 3};
    auto it = v.insert(v.begin() + 1, 9);   // 1 9 2 3

    cout << *it << '\n';                    // 9
    for (int x : v) cout << x << ' ';
}
```

## 坑

1. 插入后原来的 `it`、`end()` 可能失效，别接着用。
2. `insert` 是 `O(n)`，频繁中间插入用 `list`。
3. 批量插入用区间版本，别循环单插。

## 相关

- [[erase 返回被删元素的下一个迭代器]]
- [[01-07 STL 容器]]
