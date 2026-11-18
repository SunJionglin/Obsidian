在 C++ 中，`<map>`是标准库提供的头文件，主要用于定义**关联容器**`map`和`multimap`。这些容器用于存储**键值对（key-value）**，并通过键（key）快速检索对应的值（value），核心特点是**自动按键排序**。

### 核心容器：`map` 和 `multimap`

`<map>`头文件中定义的两个主要容器：

- `map`：键（key）唯一，每个键对应一个值；自动按键的大小排序（默认升序）。
- `multimap`：允许键重复，多个键可以对应不同的值；同样按键排序。

### 基本用法（以`map`为例）

#### 1. 包含头文件和命名空间

使用`map`需先包含头文件，并通常使用`std`命名空间：

cpp

运行

```cpp
#include <map>       // 包含map头文件
using namespace std; // 简化代码（可选，也可显式使用std::map）
```

#### 2. 定义`map`

`map`是模板类，需指定**键类型**和**值类型**，格式为：

`map<键类型, 值类型> 容器名;`

示例：定义一个 “整数键→字符串值” 的 map：

cpp

运行

```cpp
map<int, string> student; // 键是学号（int），值是姓名（string）
```

#### 3. 插入元素

`map`插入元素的常用方式：

- **`insert()`函数**：插入键值对（若键已存在，插入失败）。
- **下标操作符`[]`**：通过`map[键] = 值`插入（若键已存在，会覆盖原有值）。

示例：

cpp

运行

```cpp
// 方式1：insert()插入（键不存在时生效）
student.insert(pair<int, string>(101, "Alice")); // pair是键值对类型
student.insert(make_pair(102, "Bob"));          // make_pair简化pair创建

// 方式2：[]插入（键存在时会覆盖）
student[103] = "Charlie"; // 插入新键值对
student[101] = "Alicia";  // 覆盖原有键101的值（从"Alice"→"Alicia"）
```

#### 4. 查找元素

通过`find(键)`查找元素，返回指向该键值对的迭代器；若未找到，返回`end()`。

示例：

cpp

运行

```cpp
// 查找键为102的元素
auto it = student.find(102); 
if (it != student.end()) { // 找到元素
    cout << "找到：" << it->first << " → " << it->second << endl; 
    // it->first 是键，it->second 是值
} else {
    cout << "未找到" << endl;
}
```

#### 5. 遍历元素

`map`是有序的（默认按键升序），可通过迭代器遍历所有键值对：

cpp

运行

```cpp
// 遍历所有元素
for (auto it = student.begin(); it != student.end(); ++it) {
    cout << "键：" << it->first << "，值：" << it->second << endl;
}

// C++11及以上可用范围for循环
for (auto& pair : student) {
    cout << pair.first << " → " << pair.second << endl;
}
```

#### 6. 删除元素

- 通过`erase(键)`删除指定键的元素。
- 通过迭代器`erase(迭代器)`删除指定位置的元素。
- 通过`clear()`清空所有元素。

示例：

cpp

运行

```cpp
student.erase(101); // 删除键为101的元素

auto it = student.find(102);
if (it != student.end()) {
    student.erase(it); // 通过迭代器删除
}

student.clear(); // 清空所有元素
```

#### 7. 其他常用函数

- `size()`：返回元素个数。
- `empty()`：判断容器是否为空（空返回`true`）。
- `count(键)`：返回键出现的次数（`map`中只能是 0 或 1，`multimap`中可能≥1）。

### 自定义排序规则

`map`默认按键的升序排序（使用`less<键类型>`），可通过自定义比较器修改排序方式（如降序）。

示例：按键降序排列的 map：

cpp

运行

```cpp
#include <functional> // 包含greater比较器

// 第三个模板参数指定比较器（greater<int>表示降序）
map<int, string, greater<int>> student_desc; 

student_desc.insert({101, "Alice"});
student_desc.insert({102, "Bob"});
// 遍历结果：102→Bob，101→Alice（降序）
```

### `multimap`简介

`multimap`与`map`的区别是**允许键重复**，因此：

- 没有`[]`操作符（无法通过键直接访问值，因键可能对应多个值）。
- 查找时需用`equal_range(键)`获取所有相同键的元素范围（返回一对迭代器，表示起始和结束位置）。

示例：

cpp

运行

```cpp
multimap<int, string> mm;
mm.insert({101, "Alice"});
mm.insert({101, "Alicia"}); // 允许键101重复

// 查找所有键为101的元素
auto range = mm.equal_range(101);
for (auto it = range.first; it != range.second; ++it) {
    cout << it->first << " → " << it->second << endl; 
    // 输出：101→Alice，101→Alicia
}
```

### 总结

`<map>`头文件提供的`map`和`multimap`是处理键值对的高效工具，适合需要快速查找、排序场景（如字典、索引表）。`map`保证键唯一，`multimap`允许键重复，两者均支持按键排序和快速操作（时间复杂度通常为 O (log n)）。