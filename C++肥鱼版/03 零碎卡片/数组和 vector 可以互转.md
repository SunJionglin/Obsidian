---
title: 数组和 vector 可以互转
type: 卡片
topic: STL
tags: [C++, 零碎/STL, 类型/卡片, 难度/入门]
source: ["C++/零碎/转换数据结构的两种方式.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: 数组和 vector 可以互转.md -->

## 结论

数组转 vector 用区间构造；vector 转数组用 `data()`。

## 语法 / 签名

`vector<int> v(a, a + n); v.data();`

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a[3] = {1, 2, 3};
    vector<int> v(a, a + 3);

    int* p = v.data();
    cout << p[0] << '\n';   // 1
}
```

## 坑

1. `data()` 在空 vector 上可能返回空指针。
2. 区间 `[a, a+n)` 必须合法。
3. vector 扩容后 `data()` 失效。

## 相关

- [[01-07 STL 容器]]
- [[01-02 数组与结构体]]
