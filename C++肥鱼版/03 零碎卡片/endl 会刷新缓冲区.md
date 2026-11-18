---
title: endl 会刷新缓冲区
type: 卡片
topic: 输入输出
tags: [C++, 零碎/输入输出, 类型/卡片, 难度/入门]
source: ["C++/零碎/换行.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: endl 会刷新缓冲区.md -->

## 结论

`endl` 等于 `'\n'` 加刷新缓冲区；大量输出用 `'\n'` 更快。

## 语法 / 签名

`cout << x << '\n';` / `cout << x << endl;`

## 最小示例

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "a" << '\n';
    cout << "b" << endl;
}
```

## 坑

1. 循环里用 `endl` 会频繁 flush，拖慢输出。
2. 调试卡死时 `endl` 能帮你看到日志。
3. 文件输出同理，`'\n'` 更省。

## 相关

- [[01-08 头文件速查]]
