


在编程和计算机科学中，"vector"（向量）通常有两种主要含义：

### 1. 数学 / 线性代数中的向量

指具有大小和方向的量，在编程中常用来表示多维数据（如 2D/3D 坐标、特征向量等）。例如：

- 2D 向量：`(x, y)` 可表示平面上的点或方向
- 3D 向量：`(x, y, z)` 可表示空间中的点

### 2. 编程中的动态数组（以 C++ 为例）

在 C++ 标准库中，`std::vector` 是一种动态数组容器，属于 STL（标准模板库），具有以下特点：

- 大小可动态调整（自动管理内存）
- 元素在内存中连续存储，支持随机访问
- 提供丰富的成员函数（添加、删除、查找等）

#### C++ 中`std::vector`的基本用法示例：

cpp

运行

```cpp
#include <iostream>
#include <vector> // 需包含头文件

int main() {
    // 1. 创建vector
    std::vector<int> numbers; // 空向量
    std::vector<std::string> fruits = {"apple", "banana"}; // 初始化

    // 2. 添加元素
    numbers.push_back(10); // 在末尾添加
    numbers.push_back(20);
    numbers.push_back(30);

    // 3. 访问元素（支持[]和at()）
    std::cout << "第一个元素: " << numbers[0] << std::endl;
    std::cout << "第二个元素: " << numbers.at(1) << std::endl;

    // 4. 遍历元素
    std::cout << "所有元素: ";
    for (int num : numbers) { // 范围for循环
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 5. 其他常用操作
    std::cout << "元素数量: " << numbers.size() << std::endl; // 元素个数
    numbers.pop_back(); // 删除最后一个元素
    std::cout << "删除后数量: " << numbers.size() << std::endl;

    return 0;
}
```

### 其他语言中的类似概念

- Java：`java.util.Vector`（线程安全的动态数组）
- Python：列表（list）可视为动态数组，功能类似 vector
- C#：`List<T>` 泛型集合

`std::vector` 因其高效性和灵活性，在 C++ 中被广泛用于需要动态存储数据的场景，如存储动态大小的数据集、实现动态列表等。
# C++ 中 `<vector>` 头文件详解

`<vector>` 是 C++ 标准模板库（STL）中的核心头文件之一，它定义了 `std::vector` 模板类（动态数组容器）。`std::vector` 提供了**动态大小的数组功能**，能够自动管理内存，支持高效的随机访问，是日常开发中最常用的容器之一。

## 一、核心作用

`<vector>` 头文件的核心是 `std::vector` 模板类，其本质是 “动态数组的封装”。与 C 语言的静态数组（如 `int arr[10]`）相比，`std::vector` 具有以下核心特性：

- 大小可动态调整（无需预先指定固定长度）；
- 自动管理内存（无需手动分配 / 释放，避免内存泄漏）；
- 支持高效的随机访问（通过索引访问元素，时间复杂度 O (1)）；
- 提供丰富的成员函数，简化元素的添加、删除、查找等操作。

## 二、包含与使用方式

使用 `std::vector` 前必须包含 `<vector>` 头文件，并通过 `std` 命名空间访问（或使用 `using` 声明）：

cpp

运行

```cpp
#include <vector>  // 必须包含
using namespace std;  // 可选，简化代码（否则需写 std::vector）
```

## 三、`std::vector` 的创建与初始化

`std::vector` 是模板类，需指定元素类型（如 `int`、`string` 等）。它提供了多种初始化方式，满足不同场景需求：

### 1. 默认构造（空容器）

创建一个不含任何元素的空 vector：

cpp

运行

```cpp
vector<int> v1;  // 空的 int 类型 vector
vector<string> v2;  // 空的 string 类型 vector
```

### 2. 填充构造（指定大小和初始值）

创建包含 `n` 个相同元素的 vector，语法：`vector<类型> v(n, 初始值)`：

cpp

运行

```cpp
vector<int> v(5, 0);  // 包含 5 个元素，每个元素都是 0 → [0,0,0,0,0]
vector<char> v(3, 'a');  // 包含 3 个 'a' → ['a','a','a']
```

若省略初始值，基本类型（如 `int`）会被初始化为 0，自定义类型会调用默认构造函数。

### 3. 初始化列表构造

通过初始化列表 `{}` 直接指定元素：

cpp

运行

```cpp
vector<int> v = {1, 2, 3, 4};  // 元素为 1,2,3,4 → [1,2,3,4]
vector<string> v{"a", "b", "c"};  // 元素为 "a","b","c"
```

### 4. 拷贝构造

通过另一个 vector 初始化（复制所有元素）：

cpp

运行

```cpp
vector<int> v1 = {1,2,3};
vector<int> v2(v1);  // v2 是 v1 的副本 → [1,2,3]
vector<int> v3 = v1;  // 等价于 v3(v1)
```

### 5. 范围构造

通过迭代器范围初始化（复制另一个容器的部分元素）：

cpp

运行

```cpp
vector<int> v1 = {1,2,3,4,5};
// 复制 v1 中从第 2 个元素（索引 1）到末尾的元素 → [2,3,4,5]
vector<int> v2(v1.begin() + 1, v1.end());
```

## 四、元素访问与遍历

`std::vector` 支持多种方式访问元素，且支持高效的随机访问（类似数组）。

### 1. 直接索引访问

- `operator[]`：通过索引访问元素（无越界检查，速度快）；
- `at(index)`：通过索引访问元素（有越界检查，越界会抛出 `out_of_range` 异常）。

cpp

运行

```cpp
vector<int> v = {10, 20, 30};
cout << v[0];    // 输出 10（无越界检查）
cout << v.at(1); // 输出 20（有越界检查）

v[2] = 300;      // 修改元素 → [10,20,300]
v.at(0) = 100;   // 修改元素 → [100,20,300]
```

### 2. 访问首尾元素

- `front()`：返回第一个元素的引用；
- `back()`：返回最后一个元素的引用。

cpp

运行

```cpp
vector<int> v = {1,2,3};
cout << v.front();  // 输出 1
cout << v.back();   // 输出 3

v.front() = 10;     // 修改第一个元素 → [10,2,3]
v.back() = 30;      // 修改最后一个元素 → [10,2,30]
```

### 3. 遍历元素

常用遍历方式：

- **范围 for 循环**（C++11 及以上，简洁直观）；
- **迭代器遍历**（兼容 STL 算法）；
- **普通 for 循环**（通过索引访问）。

cpp

运行

```cpp
vector<int> v = {1,2,3,4};

// 1. 范围 for 循环（推荐，最简洁）
for (int num : v) {
    cout << num << " ";  // 输出：1 2 3 4
}

// 2. 迭代器遍历
for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";  // 输出：1 2 3 4（*it 访问元素）
}

// 3. 普通 for 循环（通过索引）
for (int i = 0; i < v.size(); ++i) {
    cout << v[i] << " ";  // 输出：1 2 3 4
}
```

## 五、元素修改（添加 / 删除 / 清空）

`std::vector` 提供了丰富的成员函数用于修改元素，无需手动管理内存。

### 1. 添加元素

- **`push_back(elem)`**：在容器末尾添加一个元素（常用）；
- **`emplace_back(Args...)`**：在末尾直接构造一个元素（效率比 `push_back` 高，避免拷贝）；
- **`insert(pos, elem)`**：在指定位置 `pos`（迭代器）插入元素。

cpp

运行

```cpp
vector<int> v;

v.push_back(1);    // 末尾添加 1 → [1]
v.push_back(2);    // 末尾添加 2 → [1,2]
v.emplace_back(3); // 末尾构造 3 → [1,2,3]（效果同 push_back，但更高效）

// 在第一个元素（索引 0）位置插入 0
v.insert(v.begin(), 0);  // → [0,1,2,3]
```

### 2. 删除元素

- **`pop_back()`**：删除最后一个元素；
- **`erase(pos)`**：删除指定位置 `pos`（迭代器）的元素；
- **`erase(begin, end)`**：删除迭代器范围 `[begin, end)` 内的所有元素。

cpp

运行

```cpp
vector<int> v = {0,1,2,3};

v.pop_back();  // 删除最后一个元素 → [0,1,2]

// 删除第一个元素（迭代器 v.begin() 指向的位置）
v.erase(v.begin());  // → [1,2]

// 删除从第一个元素到末尾的所有元素（清空容器）
v.erase(v.begin(), v.end());  // → []
```

### 3. 清空容器

- **`clear()`**：删除所有元素（容器大小变为 0，但容量可能不变）。

cpp

运行

```cpp
vector<int> v = {1,2,3};
v.clear();  // 容器变为空 → size() = 0
```

## 六、容量与大小管理

`std::vector` 区分 “大小” 和 “容量” 两个概念，理解它们的区别对高效使用 vector 至关重要。

### 1. 核心概念

- **大小（size）**：容器中当前元素的数量（通过 `size()` 获取）；
- **容量（capacity）**：容器在不重新分配内存的情况下，最多可容纳的元素数量（通过 `capacity()` 获取）。

cpp

运行

```cpp
vector<int> v;
v.push_back(1);
v.push_back(2);

cout << v.size();     // 输出 2（当前有 2 个元素）
cout << v.capacity(); // 输出 ≥2（不同编译器可能为 2、4 等，取决于扩容策略）
```

### 2. 常用容量管理函数

- **`reserve(n)`**：预分配至少能容纳 `n` 个元素的内存（仅修改容量，不改变大小）；
    
    作用：避免频繁扩容（扩容会导致元素拷贝，影响性能）。
- **`resize(n, val)`**：调整容器大小为 `n`（若 `n` 大于原大小，新增元素用 `val` 初始化；若 `n` 小于原大小，删除多余元素）。

cpp

运行

```cpp
vector<int> v;

v.reserve(100);  // 预分配 100 个元素的空间，capacity() ≥100，size() 仍为 0

v.resize(5, 0);  // 调整大小为 5，元素为 [0,0,0,0,0]，size()=5，capacity()≥100
v.resize(3);     // 调整大小为 3，删除后 2 个元素 → [0,0,0]
```

### 3. 检查容器是否为空

- **`empty()`**：若容器大小为 0，返回 `true`；否则返回 `false`（比 `size() == 0` 更高效）。

cpp

运行

```cpp
vector<int> v;
cout << v.empty();  // 输出 true（空容器）
v.push_back(1);
cout << v.empty();  // 输出 false（非空容器）
```

## 七、其他常用功能

- **`swap(v2)`**：交换当前 vector 与 `v2` 的内容（元素、大小、容量均交换，效率高）；
- **`data()`**：返回指向底层数组的指针（可用于兼容 C 语言函数，如 `memcpy`）。

cpp

运行

```cpp
vector<int> v1 = {1,2,3};
vector<int> v2 = {4,5};

v1.swap(v2);  // 交换后：v1 = [4,5]，v2 = [1,2,3]

int* ptr = v1.data();  // 指向底层数组的指针，ptr[0] = 4，ptr[1] = 5
```

## 八、`std::vector` 的优势与适用场景

### 优势：

1. **动态大小**：无需预先指定长度，可根据需求自动扩容；
2. **随机访问高效**：通过索引访问元素的时间复杂度为 O (1)，与数组相同；
3. **内存安全**：自动管理内存，避免手动分配 / 释放导致的内存泄漏或越界；
4. **兼容 STL 算法**：可与 `sort`、`find` 等 STL 算法无缝配合。

### 适用场景：

- 需要动态调整大小的数组；
- 频繁访问元素（随机访问）；
- 尾部添加 / 删除元素（`push_back`/`pop_back` 效率高，时间复杂度 O (1)）。

## 九、在压缩码转矩阵程序中的应用

在之前的 “压缩码转 01 矩阵” 程序中，`vector` 的核心应用是：

cpp

运行

```cpp
vector<int> codes;  // 存储压缩码数据（除 N 外的所有数字）
int num;
while (cin >> num) {
    codes.push_back(num);  // 收集输入的压缩码数字
}
```

- 用 `vector<int> codes` 动态存储压缩码数据（数量未知，无法用静态数组）；
- 用 `push_back(num)` 依次添加输入的数字，自动扩容，确保所有数据被正确收集。

## 总结

`<vector>` 头文件定义的 `std::vector` 是 C++ 中最常用的动态数组容器，它结合了数组的高效访问和动态大小的灵活性，几乎可以替代所有需要动态调整大小的场景。掌握 `vector` 的创建、访问、修改和容量管理，是 C++ 入门的核心技能之一。