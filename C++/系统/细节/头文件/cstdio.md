# C++ 中的 `<cstdio>` 库：C 风格输入输出的接口

`<cstdio>` 是 C++ 标准库中兼容 C 语言输入输出功能的头文件，它源自 C 语言的 `<stdio.h>`，提供了一系列用于**格式化输入输出**和**文件操作**的函数。在 C++ 中，它保留了 C 语言的输入输出风格，同时将函数纳入 `std` 命名空间，是连接 C 和 C++ 输入输出机制的重要接口。

## 与 `<stdio.h>` 的关系

- `<stdio.h>` 是 C 语言的标准输入输出头文件，所有函数位于**全局命名空间**。
- `<cstdio>` 是 C++ 对 `<stdio.h>` 的兼容版本，函数逻辑完全相同，但被封装在 **`std` 命名空间 ** 中（部分编译器可能同时在全局命名空间保留一份以兼容旧代码）。

在 C++ 程序中，推荐使用 `<cstdio>` 而非 `<stdio.h>`，以遵循 C++ 的命名空间规范。

## 核心功能：输入输出与文件操作

`<cstdio>` 提供的函数可分为两大类：**标准输入输出**（控制台操作）和**文件操作**（磁盘文件读写）。

### 一、标准输入输出函数（控制台）

用于与用户交互（键盘输入、屏幕输出），最常用的包括：

|函数|功能|示例|
|---|---|---|
|`printf(const char* format, ...)`|格式化输出到屏幕|`printf("年龄：%d\n", 20);`|
|`scanf(const char* format, ...)`|格式化从键盘输入|`scanf("%d", &age);`|
|`puts(const char* str)`|输出字符串并自动换行|`puts("Hello World");`|
|`gets(char* str)`|从键盘读取一行字符串（已过时，不安全）|-|
|`fgets(char* str, int n, FILE* stream)`|读取一行（可指定输入源，更安全）|`fgets(buf, 100, stdin);`|
|`putchar(int c)`|输出单个字符|`putchar('A');`|
|`getchar()`|从键盘读取单个字符|`char c = getchar();`|

#### `printf` 与 `scanf` 详解

这两个函数是 `<cstdio>` 的核心，通过**格式控制字符串**指定输入输出的格式。

- **`printf` 格式控制符**（常用）：
    
    - `%d`：整数（十进制）
    - `%f`：浮点数
    - `%c`：字符
    - `%s`：字符串
    - `%x`：十六进制整数
    - `%.2f`：保留 2 位小数的浮点数
    
    示例：
    
    cpp
    
    运行
    
    ```cpp
    #include <cstdio>
    int main() {
        int a = 10;
        float b = 3.1415;
        char c = 'A';
        std::printf("整数：%d，浮点数：%.2f，字符：%c\n", a, b, c);
        // 输出：整数：10，浮点数：3.14，字符：A
        return 0;
    }
    ```
    
- **`scanf` 格式控制符**（与 `printf` 类似，但需要传递变量地址）：
    
    示例：
    
    cpp
    
    运行
    
    ```cpp
    #include <cstdio>
    int main() {
        int age;
        std::printf("请输入年龄：");
        std::scanf("%d", &age); // 注意 & 取地址符
        std::printf("你输入的年龄是：%d\n", age);
        return 0;
    }
    ```
    

### 二、文件操作函数

用于读写磁盘文件，核心函数包括：

|函数|功能|示例|
|---|---|---|
|`FILE* fopen(const char* filename, const char* mode)`|打开文件（返回文件指针）|`FILE* fp = fopen("test.txt", "r");`|
|`int fclose(FILE* stream)`|关闭文件|`fclose(fp);`|
|`fprintf(FILE* stream, const char* format, ...)`|格式化写入文件|`fprintf(fp, "分数：%d", 90);`|
|`fscanf(FILE* stream, const char* format, ...)`|格式化从文件读取|`fscanf(fp, "%d", &score);`|
|`size_t fread(void* ptr, size_t size, size_t count, FILE* stream)`|二进制读取文件|`fread(buf, 1, 100, fp);`|
|`size_t fwrite(const void* ptr, size_t size, size_t count, FILE* stream)`|二进制写入文件|`fwrite(buf, 1, 100, fp);`|
|`int feof(FILE* stream)`|判断是否到达文件末尾|`while (!feof(fp)) { ... }`|

#### 文件操作示例：写入并读取文件

cpp

运行

```cpp
#include <cstdio>
int main() {
    // 打开文件（"w" 表示写入模式，若文件不存在则创建）
    FILE* fp = std::fopen("data.txt", "w");
    if (fp == nullptr) { // 判断文件是否打开成功
        std::printf("文件打开失败！\n");
        return 1;
    }
    
    // 写入内容
    std::fprintf(fp, "姓名：%s，年龄：%d\n", "Alice", 25);
    std::fclose(fp); // 关闭文件
    
    // 重新打开文件（"r" 表示读取模式）
    fp = std::fopen("data.txt", "r");
    char name[20];
    int age;
    std::fscanf(fp, "姓名：%s，年龄：%d", name, &age); // 按格式读取
    std::printf("从文件读取：%s，%d岁\n", name, age); // 输出：Alice，25岁
    std::fclose(fp);
    
    return 0;
}
```

### 三、注意事项

1. **命名空间**：`<cstdio>` 的函数位于 `std` 命名空间，使用时需加 `std::` 前缀（如 `std::printf`），或通过 `using namespace std;` 省略。
    
2. **安全性问题**：
    
    - `gets()` 因无法限制输入长度，可能导致缓冲区溢出，已被 C++11 弃用，建议用 `fgets()` 替代。
    - `scanf()` 若输入格式与预期不符，可能导致未定义行为，使用时需确保输入格式正确（或考虑 C++ 的 `cin` 更安全）。
3. **与 C++ 风格 I/O 的对比**：
    
    - `<cstdio>` 是 C 风格，依赖格式字符串，效率较高，适合简单场景。
    - C++ 风格的 `<iostream>`（`cout`/`cin`）类型安全，无需格式字符串，但性能略低（优化后差距不大）。
4. **文件打开模式**：`fopen` 的 `mode` 参数需正确设置，常用模式：
    
    - `"r"`：只读（文件必须存在）
    - `"w"`：只写（文件不存在则创建，存在则清空）
    - `"a"`：追加（在文件末尾写入）
    - `"rb"`/`"wb"`：二进制读写（用于非文本文件，如图片、音频）

## 总结

`<cstdio>` 是 C++ 中兼容 C 语言输入输出的重要头文件，提供了简洁高效的格式化 I/O 和文件操作功能。它适合需要兼容 C 代码、追求简单高效的场景，但在安全性和类型检查上不如 C++ 原生的 `<iostream>`。实际开发中，可根据需求选择合适的 I/O 方式。