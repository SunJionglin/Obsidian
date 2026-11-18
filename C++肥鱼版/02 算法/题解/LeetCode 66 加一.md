---
title: LeetCode 66 加一
type: 题解
topic: 枚举与模拟
tags: [C++, 算法/模拟, 类型/题解, 难度/入门]
from: "[[01 枚举与模拟]]"
source: "生成例题"
status: 已整理
created: 2026-10-22
aliases: [66, Plus One]
---

<!-- filename: LeetCode 66 加一.md -->

专题：[[01 枚举与模拟]]

## 0. 题目信息

| 项 | 内容 |
|---|---|
| 来源 | [LeetCode 66](https://leetcode.cn/problems/plus-one/) |
| 专题 | [[01 枚举与模拟]] |
| 难度 | ⭐ |
| 一句话 | 用数组表示的大整数加一 |

## 1. 题意与输入输出

非空数组 `digits` 表示一个非负整数（高位在前），给它加一，返回新数组。

- 输入：`digits = [1,2,3]`
- 输出：`[1,2,4]`
- 输入：`digits = [9,9,9]`
- 输出：`[1,0,0,0]`
- 数据范围：`1 <= digits.length <= 100`，无前导零（`0` 本身除外）

## 2. 思路

从最后一位往前处理：

- 小于 9：直接加一，返回。
- 等于 9：变 0，继续往前进位。
- 全部都是 9：循环结束，最高位插入 1。

## 3. 代码

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = (int)digits.size() - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                ++digits[i];
                return digits;
            }
            digits[i] = 0;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

## 4. 复杂度

- 时间：`O(n)`，最坏全 9 时遍历一遍 + 插入。
- 空间：`O(1)`（不算返回值）；`insert` 可能触发扩容。

## 5. 边界与坑

> [!warning] 坑 1：`[9,9,9]`
> 循环把每一位都置 0，最后要在开头插 1，得到 `[1,0,0,0]`。

> [!warning] 坑 2：只处理最后一位
> `[1,9,9]` 只加最后一位会变成 `[1,9,0]`，必须连续进位。

> [!warning] 坑 3：`digits` 为空
> 本题保证非空；工程代码要判空。

> [!warning] 坑 4：`insert` 的迭代器
> `digits.insert(digits.begin(), 1)`，别写成 `digits[0] = 1` 覆盖原值。

## 6. 同类题

| 题目 | 像在哪 |
|---|---|
| [LeetCode 67 二进制求和](https://leetcode.cn/problems/add-binary/) | 逐位进位，只是进制不同 |
| [LeetCode 415 字符串相加](https://leetcode.cn/problems/add-strings/) | 大整数加法，处理进位 |
| [LeetCode 2 两数相加](https://leetcode.cn/problems/add-two-numbers/) | 链表版大整数加法 |

## 7. 关联

- 专题：[[01 枚举与模拟]]
- Python 版：[[06-加一]]（Python 题解与套路）
- 原始笔记：无（生成例题）
- 上一题：[[LeetCode 59 螺旋矩阵 II]]
- 下一题：[[LeetCode 204 计数质数]]

---

哼，全 9 是这题唯一的尊严，其他情况都一秒下班。
