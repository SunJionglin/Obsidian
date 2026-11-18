---
title: size_t 是无符号，倒序遍历会翻车
type: 卡片
topic: 类型
tags: [C++, 零碎/类型, 类型/卡片, 难度/进阶]
source: ["C++/零碎/函数/size_t.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: size_t 是无符号，倒序遍历会翻车.md -->

## 结论

`size_t` 是**无符号整数**，`sizeof`、`size()`、`strlen` 都返回它；拿它做倒序下标，减到 0 再减就变成巨大值。

## 语法 / 签名

```cpp
size_t n = v.size();
for (size_t i = 0; i < n; ++i) ...
```

## 最小示例

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v{1, 2, 3};

    // 正确：倒序用 int 或反向迭代器
    for (int i = (int)v.size() - 1; i >= 0; --i)
        cout << v[i] << ' ';          // 3 2 1

    // 错误示范（别跑）：
    // for (size_t i = v.size() - 1; i >= 0; --i)  // 死循环
}
```

## 坑

1. `size_t` 永远 `>= 0`，`i >= 0` 恒真，循环停不下来。
2. `int` 和 `size_t` 比较时，`int` 会转成无符号，`-1 > 0u` 为真。
3. 打印用 `%zu`，别用 `%d`。

## 相关

- [[sizeof 是字节数，size 是元素个数]]
- [[01-07 STL 容器]]
