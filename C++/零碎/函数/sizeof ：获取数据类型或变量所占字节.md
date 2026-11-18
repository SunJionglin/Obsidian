# sizeof [[运算符]]笔记

## 一、基本概念

`sizeof` 是 C++ 中的一个[[运算符]]，用于获取数据类型或变量在内存中所占的字节数。它的作用类似于函数，但实际上是一个编译时[[运算符]]，即在编译阶段就确定了结果，而不是在运行时计算。
==而用「（变量名）.size」的方式查询的是容器中元素的个数。==

## 二、语法形式

1. **获取数据类型的大小**

cpp

```cpp
sizeof(type);
```

例如，获取 `int` 类型的大小：

cpp

```cpp
int sizeOfInt = sizeof(int); 
// sizeOfInt 将存储 int 类型在当前系统下所占的字节数
```

2. **获取变量的大小**

cpp

```cpp
sizeof(variable);
```

例如：

cpp

```cpp
int num = 10;
int sizeOfNum = sizeof(num); 
// sizeOfNum 将存储变量 num 所占的字节数，由于 num 是 int 类型，结果和 sizeof(int) 通常相同
```

## 三、原理

在不同的操作系统和编译器环境下，数据类型的大小可能会有所不同。例如，在 32 位系统中，`int` 类型通常占 4 个字节；而在 64 位系统中，`int` 类型同样可能占 4 个字节，但指针类型在 32 位系统占 4 个字节，在 64 位系统占 8 个字节。`sizeof` [[运算符]]会根据当前编译环境准确地返回数据类型或变量所占的字节数。

## 四、应用场景

1. **内存分配**：在动态内存分配时，知道数据类型的大小有助于准确分配内存。例如，使用 `malloc` 或 `new` 分配内存时，需要知道要分配的字节数。

cpp

```cpp
int* arr = new int[10]; 
// 这里实际上是分配了 sizeof(int) * 10 个字节的内存空间
```

2. **[[数组]]操作**：可以通过 `sizeof` 计算[[数组]]的总大小，进而确定[[数组]]元素个数。

cpp

```cpp
int arr[] = {1, 2, 3, 4, 5};
int numElements = sizeof(arr) / sizeof(arr[0]); 
// numElements 为[[数组]] arr 的元素个数，5
```

## 五、注意事项

1. **函数参数**：在函数参数中使用 `sizeof` 无法获取实际传递数组的大小。因为数组作为函数参数传递时会退化为指针。

cpp

```cpp
void printSize(int arr[]) {
    int size = sizeof(arr); 
    // size 在 32 位系统通常为 4（指针大小），在 64 位系统通常为 8，而不是[[数组]]实际大小
}
```

2. **自定义类型**：对于自定义的结构体或类，`sizeof` 计算的大小包含成员变量的大小以及可能的内存对齐填充字节。

cpp

```cpp
struct MyStruct {
    char c; 
    int i; 
};
// sizeof(MyStruct) 通常大于 sizeof(char) + sizeof(int)，因为存在内存对齐
```

## 六、示例

cpp

```cpp
#include <iostream>

int main() {
    // 获取基本数据类型大小
    std::cout << "Size of char: " << sizeof(char) << " bytes" << std::endl;
    std::cout << "Size of int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Size of double: " << sizeof(double) << " bytes" << std::endl;

    // 获取变量大小
    char ch = 'a';
    std::cout << "Size of ch: " << sizeof(ch) << " bytes" << std::endl;

    // 获取[[数组]]大小及元素个数
    int arr[] = {1, 2, 3, 4, 5};
    int sizeOfArr = sizeof(arr);
    int numOfElements = sizeOfArr / sizeof(arr[0]);
    std::cout << "Size of arr: " << sizeOfArr << " bytes" << std::endl;
    std::cout << "Number of elements in arr: " << numOfElements << std::endl;

    return 0;
}
```

上述代码展示了如何使用 `sizeof` 获取不同数据类型、变量以及[[数组]]的大小。