---
title: find 找不到返回 string npos
type: 卡片
topic: 字符串
tags: [C++, 零碎/字符串, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/判断是否找到元素：npos.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: find 找不到返回 string npos.md -->

## 结论

`string::find` 找不到时返回 `string::npos`，判断必须拿它比，不能拿 `-1` 当字符串下标用。

## 语法 / 签名

```cpp
size_t find(const string& sub, size_t pos = 0) const;
static const size_t npos = -1;   // 实际是 size_t 的最大值
```

## 最小示例

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hello world";

    size_t p = s.find("world");
    if (p != string::npos) cout << p << '\n';   // 6
    else cout << "not found\n";
}
```

## 坑

1. `npos` 是 `size_t` 类型，`p == -1` 会触发警告，写 `p == string::npos`。
2. `find` 返回的是首次出现位置，要找全部得循环 + `pos + 1`。
3. 别把 `npos` 直接当 `int` 用，转来转去容易溢出。

## 相关

- [[01-08 头文件速查]]
- [[01-07 STL 容器]]
