`<cstring>` 是 **C++ 里专门用来操作「C 风格字符串」的工具头文件**

它提供了一堆现成的函数，帮你快速处理**字符数组（char*）**

---

# 二、先分清两个极易搞混的头文件

表格

|头文件|作用|操作对象|
|---|---|---|
|`<string>`|C++ 官方 `string` 类|`std::string` 字符串|
|`<cstring>`|C 语言字符串工具函数库|**`char*` / `char[]`**（纯字符数组）|

---

# 三、`<cstring>` 里有什么？

它提供了**4 个最常用的字符串操作函数**，背会这 4 个就够了：

## 1. `strlen(字符串)` → 求长度

计算字符串有多少个字符（不算结尾的 `\0`）

cpp

运行

```
char str[] = "hello";
int len = strlen(str); 
// len = 5
```

## 2. `strcpy(目标, 源)` → 拷贝字符串

把一个字符串**完整复制**到另一个里

cpp

运行

```
char a[10];
char b[] = "hi";
strcpy(a, b); 
// a 变成 "hi"
```

## 3. `strcat(目标, 源)` → 拼接字符串

把两个字符串粘在一起

cpp

运行

```
char a[20] = "hello";
char b[] = " world";
strcat(a, b); 
// a 变成 "hello world"
```

## 4. `strcmp(字符串1, 字符串2)` → 比较字符串

- 返回 `0` → 两个字符串**相等**
- 返回非 0 → 不相等

cpp

运行

```
char a[] = "abc";
char b[] = "abc";
int res = strcmp(a, b); 
// res = 0
```

---

# 四、为什么要用它？

如果没有 `<cstring>`，你想算字符串长度、拷贝、拼接，**必须自己写循环遍历字符**，超级麻烦！

有了它，**一行函数搞定**。

---

# 五、终极总结

1. `<cstring>` = **C 风格字符串工具包**
2. 专门操作 `char*` / `char[]`
3. 核心 4 函数：`strlen` / `strcpy` / `strcat` / `strcmp`
4. **和 `<string>` 不是一个东西！**