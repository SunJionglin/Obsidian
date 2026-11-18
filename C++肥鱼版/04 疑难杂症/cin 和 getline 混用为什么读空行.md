---
title: cin 和 getline 混用为什么读空行
type: 疑难
topic: 输入输出
tags: [C++, 疑难/输入输出, 类型/Q&A, 难度/入门]
source: ["C++/零碎/函数/getline处理多行输入.md"]
status: 已整理
created: 2026-10-22
---

<!-- filename: cin 和 getline 混用为什么读空行.md -->

## 现象

`cin >> n` 之后 `getline` 读到空字符串。

## 最小复现

```cpp
int n; cin >> n;
string s; getline(cin, s);   // 空行
```

## 原因

`cin >> n` 把换行符留在缓冲区，`getline` 读到它立刻返回。

## 结论

混用前先 `cin.ignore()` 吃掉换行。

## 预防

统一用 `getline` + `stoi`，或读完后 `cin.ignore(numeric_limits<streamsize>::max(), '\n');`。

## 相关

- [[getline 读一整行，cin 遇空格就停]]
