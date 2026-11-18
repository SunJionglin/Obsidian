在 C++ 中，`std::vector` 的 `insert` 函数用于在容器的**指定位置**插入元素（单个元素、多个元素或另一个容器的区间），插入后原位置及之后的元素会自动后移，容器大小相应增加。它是比 `push_back` 更灵活的插入方式（`push_back` 仅能在末尾插入单个元素）。

### `insert` 的核心用法（常见重载形式）

`insert` 有多种重载形式，以下是最常用的几种：

#### 1. 插入单个元素

**函数原型**：

cpp

运行

```cpp
iterator insert(iterator pos, const T& value);
```

- **功能**：在迭代器 `pos` 指向的位置插入单个元素 `value`。
- **参数**：
    - `pos`：插入位置的迭代器（如 `v.begin()`、`v.end()` 等）。
    - `value`：要插入的元素（类型需与 `vector` 存储的元素类型一致）。
- **返回值**：指向插入元素的迭代器（方便后续操作）。

**示例**：

cpp

运行

```cpp
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> v = {1, 3, 4};
    
    // 在第二个位置（索引1）插入元素2
    auto it = v.insert(v.begin() + 1, 2);  // v.begin()+1 指向索引1的位置
    
    // 输出插入后的vector
    for (int num : v) {
        cout << num << " ";  // 结果：1 2 3 4
    }
    cout << endl;
    
    // 输出插入元素的位置（迭代器指向2）
    cout << "插入的元素：" << *it << endl;  // 结果：2
    return 0;
}
```

#### 2. 插入多个相同元素

**函数原型**：

cpp

运行

```cpp
iterator insert(iterator pos, size_type count, const T& value);
```

- **功能**：在 `pos` 位置插入 `count` 个相同的元素 `value`。
- **参数**：
    - `count`：要插入的元素数量。

**示例**：

cpp

运行

```cpp
vector<int> v = {1, 4};

// 在索引1的位置插入2个元素3
v.insert(v.begin() + 1, 2, 3);  

// 输出：1 3 3 4
for (int num : v) {
    cout << num << " ";
}
```

#### 3. 插入另一个容器的区间（最常用）

**函数原型**：

cpp

运行

```cpp
template <class InputIt>
iterator insert(iterator pos, InputIt first, InputIt last);
```

- **功能**：将另一个容器（或数组）中 `[first, last)` 区间的所有元素插入到 `pos` 位置。
- **参数**：
    - `first`：源容器的起始迭代器（包含）。
    - `last`：源容器的结束迭代器（不包含）。

**示例**：

cpp

运行

```cpp
vector<int> v1 = {1, 2, 3};
vector<int> v2 = {4, 5};

// 将v1的所有元素插入到v2的末尾（v2.end() 表示末尾位置）
v2.insert(v2.end(), v1.begin(), v1.end());  

// 输出v2：4 5 1 2 3
for (int num : v2) {
    cout << num << " ";
}
```

也可以插入部分区间（如只插入 v1 的前 2 个元素）：

cpp

运行

```cpp
v2.insert(v2.end(), v1.begin(), v1.begin() + 2);  // 插入v1的[1,2]
// v2 结果：4 5 1 2
```

#### 4. 插入初始化列表

**函数原型**：

cpp

运行

```cpp
iterator insert(iterator pos, initializer_list<T> ilist);
```

- **功能**：插入初始化列表 `{a, b, c...}` 中的元素到 `pos` 位置。

**示例**：

cpp

运行

```cpp
vector<int> v = {1, 5};

// 在索引1的位置插入 {2, 3, 4}
v.insert(v.begin() + 1, {2, 3, 4});  

// 输出：1 2 3 4 5
for (int num : v) {
    cout << num << " ";
}
```

### 注意事项

1. **迭代器有效性**：
    
    插入元素后，原容器中 `pos` 及之后的迭代器、指针、引用可能失效（因为元素被移动），但 `insert` 返回的迭代器是有效的（指向插入的第一个元素）。
    
2. **时间复杂度**：
    
    插入操作会导致 `pos` 位置之后的元素整体后移，因此时间复杂度为 **O(n)**（n 是容器中元素的个数），在 vector 中间插入效率较低，末尾插入（`pos = v.end()`）相对高效。
    
3. **元素类型匹配**：
    
    插入的元素类型必须与 `vector` 声明的元素类型一致（如 `vector<int>` 只能插入 `int` 类型元素）。
    

### 总结

`insert` 是 vector 中灵活的插入工具，核心场景包括：

- 插入单个元素到指定位置；
- 批量插入相同元素；
- 合并两个容器（插入另一个容器的全部 / 部分元素）；
- 插入初始化列表中的元素。

根据需求选择对应的重载形式即可。