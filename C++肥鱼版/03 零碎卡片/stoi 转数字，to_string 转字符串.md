---
title: stoi 转数字，to_string 转字符串
type: 卡片
topic: 字符串
tags: [C++, 零碎/字符串, 类型/卡片, 难度/入门]
source: ["C++/零碎/函数/字符串转数字.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: stoi 转数字，to_string 转字符串.md -->

## 结论

字符串转数字用 `stoi` / `stod`，数字转字符串用 `to_string`。

## 语法 / 签名

```cpp
int    stoi(const string& s);
double stod(const string& s);
string to_string(int / double / ...);
```

## 最小示例

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n = stoi("42");
    double d = stod("3.14");
    string s = to_string(42);

    cout << n << ' ' << d << ' ' << s << '\n';   // 42 3.14 42
}
```

## 坑

1. `stoi("3.14")` 只读到 `3`，不报错——要小数用 `stod`。
2. 越界抛 `out_of_range`，非法字符抛 `invalid_argument`，该 `try/catch` 就包。
3. 需要 `#include <string>`。

## 相关

- [[01-08 头文件速查]]
- [[01-01 基础语法与运算符]]
