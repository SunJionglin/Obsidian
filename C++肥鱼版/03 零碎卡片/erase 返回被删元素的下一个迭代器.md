---
title: erase 返回被删元素的下一个迭代器
type: 卡片
topic: STL
tags: [C++, 零碎/容器, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/erase.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: erase 返回被删元素的下一个迭代器.md -->

## 结论

`erase` 删除后返回**下一个有效迭代器**；循环删除时必须接住它，不能再 `it++`。

## 语法 / 签名

```cpp
iterator erase(iterator pos);
iterator erase(iterator first, iterator last);   // 左闭右开
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2, 3, 4, 5};

    for (auto it = v.begin(); it != v.end(); ) {
        if (*it % 2 == 0) it = v.erase(it);   // 接住返回值
        else ++it;
    }

    for (int x : v) cout << x << ' ';          // 1 3 5
}
```

## 坑

1. `erase` 后原迭代器失效，继续用是未定义行为。
2. 写成 `v.erase(it); ++it;` 会跳过下一个元素。

## 相关

- [[01-07 STL 容器]]
- [[01-08 头文件速查]]
