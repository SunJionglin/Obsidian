# unordered_map 核心笔记

`unordered_map` 是 C++ STL 中**无序键值对（key-value）容器**，底层基于**哈希表**实现，核心优势是**快速查找 / 插入 / 删除**（平均时间复杂度 O (1)），是新手处理 “键值映射” 场景的首选（如字典、缓存、计数等）。

## 一、基础认知

### 1. 核心特性（通俗理解）

- 像一本 “无序字典”：每个唯一的 `key` 对应一个 `value`（如 “学号 101” 对应 “张三”）；
- 无序性：元素不会按 `key` 排序（区别于 `map` 的红黑树有序）；
- 唯一性：`key` 不能重复，重复插入会覆盖原有值；
- 高效性：哈希表结构让查找 / 插入比 `map` 更快（适合大数据量）。

### 2. 使用前提

必须包含头文件，且建议使用 `std` 命名空间（新手友好）：

cpp

运行

```
#include <unordered_map>  // 核心头文件
using namespace std;      // 可选，否则需写 std::unordered_map
```

## 二、核心操作（代码示例）

以下是新手最常用的操作，结合 “学号 - 姓名” 映射场景演示：

cpp

运行

```cpp

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    // 1. 定义：unordered_map<键类型, 值类型> 容器名
    unordered_map<int, string> stu_map;  // key=学号(int)，value=姓名(string)

    // 2. 插入元素（3种常用方式）
    stu_map[101] = "张三";                // 方式1：[]直接赋值（无则插入，有则覆盖）
    stu_map.insert({102, "李四"});       // 方式2：insert插入pair（推荐，可判断是否插入成功）
    stu_map.emplace(103, "王五");        // 方式3：emplace直接构造（效率更高，避免拷贝）

    // 3. 访问元素
    cout << "学号101：" << stu_map[101] << endl;  // 方式1：[]访问（无key则自动插入默认值，慎用！）
    // 方式2：find查找（推荐，无key不会插入，返回迭代器）
    auto it = stu_map.find(102);
    if (it != stu_map.end()) {  // 必须判断是否找到（迭代器不等于end()）
        cout << "学号102：" << it->second << endl;
    }

    // 4. 修改元素
    stu_map[101] = "张三丰";  // 直接赋值覆盖
    it = stu_map.find(103);
    if (it != stu_map.end()) {
        it->second = "王老五";
    }

    // 5. 删除元素（3种方式）
    stu_map.erase(102);        // 方式1：按key删除（返回删除的元素个数，1/0）
    // stu_map.erase(it);      // 方式2：按迭代器删除（需确保迭代器有效）
    // stu_map.clear();        // 方式3：清空所有元素

    // 6. 遍历元素（无序）
    cout << "\n遍历所有元素：" << endl;
    for (const auto& pair : stu_map) {  // const& 避免拷贝，提高效率
        cout << "学号：" << pair.first << "，姓名：" << pair.second << endl;
    }

    // 7. 常用属性
    cout << "\n容器大小：" << stu_map.size() << endl;       // 元素个数
    cout << "是否为空：" << (stu_map.empty() ? "是" : "否") << endl;  // 是否空容器
    cout << "学号102是否存在：" << (stu_map.count(102) ? "是" : "否") << endl;  // count：存在返回1，否则0

    return 0;
}
```

### 输出结果（无序，每次运行可能不同）

plaintext

```cpp

学号101：张三
学号102：李四

遍历所有元素：
学号：101，姓名：张三丰
学号：103，姓名：王老五

容器大小：2
是否为空：否
学号102是否存在：否
```

## 三、常用成员函数速查表

表格

|函数|作用|示例|
|---|---|---|
|`operator[]`|访问 / 插入 key 对应的 value（无则插默认值）|`stu_map[101] = "张三";`|
|`find(key)`|查找 key，返回迭代器（无则返回 end ()）|`auto it = stu_map.find(101);`|
|`insert(pair)`|插入键值对（key 重复则插入失败）|`stu_map.insert({102, "李四"});`|
|`emplace(key, val)`|直接构造键值对（效率更高）|`stu_map.emplace(103, "王五");`|
|`erase(key)`|按 key 删除元素（返回删除个数）|`stu_map.erase(102);`|
|`clear()`|清空所有元素|`stu_map.clear();`|
|`size()`|返回元素个数|`int n = stu_map.size();`|
|`empty()`|判断是否为空（空返回 true）|`bool is_empty = stu_map.empty();`|
|`count(key)`|统计 key 存在个数（0 或 1）|`int cnt = stu_map.count(101);`|

## 四、unordered_map vs map（新手必区分）

表格

|特性|unordered_map|map|
|---|---|---|
|底层实现|哈希表|红黑树|
|有序性|无序（按哈希值存储）|有序（按 key 升序）|
|查找效率|平均 O (1)，最坏 O (n)（哈希冲突）|稳定 O (logn)|
|插入 / 删除|平均 O (1)|O(logn)|
|内存占用|更高（哈希表冗余）|更紧凑|
|适用场景|快速查找、不要求有序|需有序遍历、范围查找|

## 五、注意事项（新手避坑）

1. **key 的要求**：`unordered_map` 的 `key` 必须是**可哈希类型**（如 int、string、double 等基本类型），自定义类型需手动实现哈希函数（新手暂不用）；
2. **[] 的坑**：`stu_map[key]` 若 key 不存在，会**自动插入一个 key，并赋值为 value 的默认值**（如 string 默认空串，int 默认 0），因此**仅确定 key 存在时才用 []，否则用 find ()**；
3. **哈希冲突**：若大量 key 哈希值相同，效率会退化到 O (n)，可自定义哈希函数优化（新手暂不用）；
4. **遍历无序**：不要依赖遍历顺序，若需有序，改用 `map` 或遍历后排序。

## 六、典型使用场景

1. **计数统计**：统计字符串 / 数组中元素出现次数（如统计 “a,b,c,a” 中 a 出现 2 次）；
2. **快速映射**：如学号→姓名、身份证→信息、单词→释义等字典场景；
3. **缓存存储**：临时存储高频访问的数据，快速查找 / 删除。

### 总结

1. `unordered_map` 是**无序键值对容器**，底层哈希表，平均 O (1) 查找效率，适合快速映射 / 计数；
2. 核心操作：`find()`（安全查找）、`[]`（赋值 / 访问）、`insert/emplace`（插入）、`erase`（删除），注意`[]`会自动插入默认值的坑；
3. 与`map`的核心区别：无序但更快，需有序场景选`map`，需快速查找选`unordered_map`。