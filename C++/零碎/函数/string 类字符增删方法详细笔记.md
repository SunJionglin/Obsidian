
## 一、核心说明

C++ 中的 `string` 类是处理字符串的核心工具，其增删方法均为**成员函数**，大部分增删操作是**原地修改**字符串（除 `substr` 外，它生成新字符串）。本笔记聚焦字符串的**字符添加**和**字符删除**两类高频操作，结合场景和示例讲解用法。

## 二、字符添加方法

|方法原型|功能描述|适用场景|代码示例|执行结果|
|---|---|---|---|---|
|`void push_back(char c)`|在字符串**末尾**添加**单个字符**|仅追加单个字符|`string s="ab"; s.push_back('c');`|`s = "abc"`|
|`string& operator+=(const string& str)`<br><br>`string& operator+=(char c)`|在末尾拼接**字符串**或**单个字符**|追加字符 / 字符串（最常用）|`string s="a"; s+="bc"; s+='d';`|`s = "abcd"`|
|`string& insert(size_t pos, const string& str)`|在 `pos` 位置插入**字符串**|中间插入字符串|`string s="ac"; s.insert(1, "b");`|`s = "abc"`|
|`string& insert(size_t pos, size_t n, char c)`|在 `pos` 位置插入 `n` 个重复的字符 `c`|插入多个相同字符|`string s="ab"; s.insert(2, 3, 'c');`|`s = "abccc"`|

### 注意事项

1. `push_back` 只能添加**单个字符**，不能添加字符串；`+=` 支持字符和字符串，灵活性更高。
2. `insert` 的 `pos` 参数是插入的起始位置，取值范围是 `0 ~ s.size()`（`pos = s.size()` 等价于末尾追加）。
3. 越界插入会触发未定义行为，使用时需确保 `pos` 合法。

## 三、字符删除方法

| 方法原型                                               | 功能描述                                                 | 适用场景       | 代码示例                                                   | 执行结果        |
| -------------------------------------------------- | ---------------------------------------------------- | ---------- | ------------------------------------------------------ | ----------- |
| `void pop_back()`                                  | 删除字符串**最后一个字符**                                      | 仅删除末尾单个字符  | `string s="test"; s.pop_back();`                       | `s = "tes"` |
| `string& erase(size_t pos = 0, size_t len = npos)` | 从 `pos` 位置开始，删除 `len` 个字符<br><br>若 `len` 缺省，删除到字符串末尾 | 删除指定长度的子串  | `string s="abcde"; s.erase(1,2);`                      | `s = "ade"` |
| `iterator erase(iterator p)`                       | 删除迭代器 `p` 指向的字符                                      | 按迭代器删除单个字符 | `string s="abc"; s.erase(s.begin()+1);`                | `s = "ac"`  |
| `iterator erase(iterator first, iterator last)`    | 删除 `[first, last)` 区间内的字符                            | 按迭代器删除区间字符 | `string s="abcde"; s.erase(s.begin()+1, s.begin()+3);` | `s = "ade"` |

### 注意事项

1. `pop_back()` 无参数、无返回值，仅删末尾字符；删除空字符串会触发未定义行为。
2. `erase(pos, len)` 中：
    - 若 `pos` 超出字符串长度，触发未定义行为；
    - 若 `pos + len` 超出字符串长度，则删除到字符串末尾。
3. 迭代器版本的 `erase` 会返回指向**被删字符下一个位置**的迭代器，适合遍历删除场景。

## 四、实战场景示例（结合 Amog'u 名词转换题）

### 需求

删除字符串末尾的 `"us"`（2 个字符），然后添加 `"i"`。

### 实现方法对比

|方法|代码片段|优点|
|---|---|---|
|`erase` + `+=`|`string s="amogus"; s.erase(s.size()-2, 2); s+='i';`|原地修改，效率高|
|`substr` + `+=`|`string s="amogus"; s = s.substr(0, s.size()-2); s+='i';`|逻辑直观，适合新手|
|两次 `pop_back()` + `push_back`|`string s="amogus"; s.pop_back(); s.pop_back(); s.push_back('i');`|仅用首尾操作，适合理解基础方法|

三种方法最终结果均为 `s = "amogi"`。

## 五、方法选用建议

1. **末尾追加**
    - 加单个字符 → `push_back` 或 `+=`
    - 加字符串 → `+=`
2. **中间插入** → 必用 `insert`
3. **末尾删除**
    - 删单个字符 → `pop_back`
    - 删多个字符 → `erase(pos, len)`
4. **保留原字符串** → 用 `substr` 生成新串，避免修改原串