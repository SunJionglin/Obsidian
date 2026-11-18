我们用 **C++** 实现一个**简易版的 String 类**，覆盖标准 `std::string` 最核心的功能：

- 构造函数（默认、带参）
- 拷贝构造、赋值重载（**深拷贝**，核心重点）
- 析构函数
- 长度获取、C 字符串转换
- 字符访问 `[]`
- 字符串拼接 `+=`/`+`
- 比较、判空、输出重载

---

# 简易 String 类完整实现

cpp

运行

```cpp
#include <iostream>
// 用于字符串操作：strlen/strcpy/strcmp/strcat
#include <cstring>
using namespace std;

// 自定义简易 String 类
class MyString {
private:
    char* _str;    // 存储字符串的堆内存指针
    size_t _len;   // 字符串长度（不含 '\0'）

public:
    // 1. 默认构造函数：空字符串
    MyString() : _str(nullptr), _len(0) {
        // 空字符串分配1字节存储 '\0'
        _str = new char[1];
        *_str = '\0';
    }

    // 2. 带参构造函数：接收C风格字符串
    MyString(const char* s) {
        if (s == nullptr) { // 处理空指针
            _str = new char[1];
            *_str = '\0';
            _len = 0;
        } else {
            _len = strlen(s);         // 计算长度
            _str = new char[_len + 1];// 分配内存（+1存结束符）
            strcpy(_str, s);          // 拷贝内容
        }
    }

    // 3. 拷贝构造函数（深拷贝！）
    MyString(const MyString& other) {
        _len = other._len;
        _str = new char[_len + 1]; // 重新分配内存
        strcpy(_str, other._str);  // 拷贝数据
    }

    // 4. 析构函数：释放堆内存
    ~MyString() {
        delete[] _str; // 释放数组内存
        _str = nullptr;
        _len = 0;
    }

    // 5. 赋值运算符重载（深拷贝，处理自赋值）
    MyString& operator=(const MyString& other) {
        // 1. 防止自赋值
        if (this == &other) {
            return *this;
        }

        // 2. 释放当前对象原有内存
        delete[] _str;

        // 3. 深拷贝新数据
        _len = other._len;
        _str = new char[_len + 1];
        strcpy(_str, other._str);

        return *this;
    }

    // ---------------- 常用成员函数 ----------------
    // 获取C风格字符串（const 保证不修改原数据）
    const char* c_str() const {
        return _str;
    }

    // 获取字符串长度
    size_t length() const {
        return _len;
    }
    size_t size() const {
        return _len;
    }

    // 判断是否为空字符串
    bool empty() const {
        return _len == 0;
    }

    // ---------------- 运算符重载 ----------------
    // [] 重载：访问单个字符（支持读写）
    char& operator[](size_t index) {
        return _str[index];
    }
    // const 版本：只读访问
    const char& operator[](size_t index) const {
        return _str[index];
    }

    // += 重载：字符串拼接
    MyString& operator+=(const MyString& other) {
        size_t new_len = _len + other._len;
        // 申请新内存
        char* new_str = new char[new_len + 1];
        // 拼接字符串
        strcpy(new_str, _str);
        strcat(new_str, other._str);

        // 释放旧内存，指向新内存
        delete[] _str;
        _str = new_str;
        _len = new_len;

        return *this;
    }

    // ---------------- 友元函数 ----------------
    // + 重载：字符串拼接（全局函数）
    friend MyString operator+(const MyString& s1, const MyString& s2);
    // == 重载：字符串比较
    friend bool operator==(const MyString& s1, const MyString& s2);
    // << 重载：输出字符串
    friend ostream& operator<<(ostream& os, const MyString& s);
};

// 实现 + 运算符
MyString operator+(const MyString& s1, const MyString& s2) {
    MyString res;
    res._len = s1._len + s2._len;
    res._str = new char[res._len + 1];
    strcpy(res._str, s1._str);
    strcat(res._str, s2._str);
    return res;
}

// 实现 == 运算符
bool operator==(const MyString& s1, const MyString& s2) {
    return strcmp(s1._str, s2._str) == 0;
}

// 实现输出运算符
ostream& operator<<(ostream& os, const MyString& s) {
    os << s._str;
    return os;
}

// ---------------- 测试代码 ----------------
int main() {
    // 1. 带参构造
    MyString s1("Hello");
    cout << "s1 = " << s1 << ", 长度：" << s1.length() << endl;

    // 2. 默认构造 + 赋值
    MyString s2;
    s2 = "World";
    cout << "s2 = " << s2 << endl;

    // 3. 拷贝构造
    MyString s3 = s1;
    cout << "s3 = " << s3 << endl;

    // 4. 字符串拼接
    MyString s4 = s1 + " " + s2;
    cout << "s4 = " << s4 << endl;

    // 5. += 拼接
    s4 += "!!!";
    cout << "s4 += !!! : " << s4 << endl;

    // 6. 字符访问
    cout << "s1[0] = " << s1[0] << endl;
    s1[0] = 'h';
    cout << "修改后 s1 = " << s1 << endl;

    // 7. 比较
    cout << "s1 == s3 ? " << (s1 == s3 ? "是" : "否") << endl;

    return 0;
}
```

---

## 核心知识点解释

### 1. 为什么必须用**深拷贝**？

- 浅拷贝：只拷贝指针地址，多个对象指向**同一块内存**，析构时会重复释放内存，导致程序崩溃。
- 深拷贝：为每个对象**重新分配独立内存**，再拷贝数据，安全无冲突。

### 2. 关键函数说明

表格

|函数|作用|
|---|---|
|`MyString(const char*)`|用 C 字符串初始化|
|`MyString(const MyString&)`|拷贝构造（深拷贝）|
|`operator=`|赋值重载（深拷贝 + 自赋值判断）|
|`c_str()`|转换为 C 风格`const char*`，兼容 C 接口|
|`operator[]`|像数组一样访问字符|
|`operator+`/`+=`|字符串拼接|

---

## 运行结果

plaintext

```
s1 = Hello, 长度：5
s2 = World
s3 = Hello
s4 = Hello World
s4 += !!! : Hello World!!!
s1[0] = H
修改后 s1 = hello
s1 == s3 ? 否
```

---

### 总结

1. 这个简易 `MyString` 实现了**标准 string 的核心功能**，完全满足日常使用；
2. **深拷贝**是自定义字符串类的灵魂，解决了指针内存安全问题；
3. 代码遵循 C++ 类的设计规范：构造 / 析构 / 拷贝 / 赋值四大函数齐全。


# C++ 简易 String 类（MyString）实现 学习笔记

基于我们的对话整理，**覆盖核心原理、代码实现、语法细节、避坑指南**，是新手理解自定义字符串类的完整资料。

---

## 一、笔记核心目标

1. 手动实现一个简易版 `string` 类，掌握 C++ 类的**四大核心函数**（构造 / 拷贝构造 / 赋值重载 / 析构）；
2. 彻底理解**深拷贝**（自定义字符串类的灵魂）；
3. 搞懂赋值运算符重载的**参数、返回值、底层逻辑**。

---

## 二、核心前置知识：浅拷贝 VS 深拷贝

### 1. 浅拷贝（默认行为，致命缺陷）

- C++ 自动生成的拷贝 / 赋值逻辑：**只拷贝指针地址，不拷贝数据**；
- 后果：多个对象共用同一块内存，析构时**重复释放内存**（程序崩溃）、**一改全改**。

### 2. 深拷贝（手动实现，安全方案）

- 为每个对象**重新分配独立内存**，再复制字符串内容；
- 后果：对象互不干扰，内存安全，是自定义字符串类的必须操作。

---

## 三、完整 MyString 类实现（带核心注释）

cpp

运行

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class MyString {
private:
    char* _str;    // 指向堆内存，存储字符串内容
    size_t _len;   // 字符串长度（不含结束符\0）

public:
    // 1. 默认构造：空字符串
    MyString() : _len(0) {
        _str = new char[1];
        *_str = '\0';
    }

    // 2. 带参构造：接收C风格字符串
    MyString(const char* s) {
        if (s == nullptr) {
            _str = new char[1];
            *_str = '\0';
            _len = 0;
        } else {
            _len = strlen(s);
            _str = new char[_len + 1]; // +1 存储\0
            strcpy(_str, s);
        }
    }

    // 3. 拷贝构造函数（深拷贝）：用已有对象创建新对象
    MyString(const MyString& other) {
        _len = other._len;         // 拷贝长度
        _str = new char[_len + 1]; // 开辟新内存
        strcpy(_str, other._str);  // 拷贝数据
    }

    // 4. 析构函数：释放堆内存，防止泄漏
    ~MyString() {
        delete[] _str;
        _str = nullptr;
        _len = 0;
    }

    // 5. 赋值运算符重载（核心！深拷贝）
    MyString& operator=(const MyString& other) {
        // ① 防止自赋值：自己=自己，直接返回
        if (this == &other) {
            return *this;
        }
        // ② 释放当前对象旧内存，避免泄漏
        delete[] _str;
        // ③ 深拷贝新数据
        _len = other._len;
        _str = new char[_len + 1];
        strcpy(_str, other._str);
        // ④ 返回当前对象引用（支持连续赋值）
        return *this;
    }

    // 成员函数
    const char* c_str() const { return _str; }
    size_t length() const { return _len; }
    bool empty() const { return _len == 0; }

    // 运算符重载
    char& operator[](size_t index) { return _str[index]; }
    const char& operator[](size_t index) const { return _str[index]; }

    MyString& operator+=(const MyString& other) {
        size_t new_len = _len + other._len;
        char* new_str = new char[new_len + 1];
        strcpy(new_str, _str);
        strcat(new_str, other._str);

        delete[] _str;
        _str = new_str;
        _len = new_len;
        return *this;
    }

    // 友元函数
    friend MyString operator+(const MyString& s1, const MyString& s2);
    friend bool operator==(const MyString& s1, const MyString& s2);
    friend ostream& operator<<(ostream& os, const MyString& s);
};

// 友元函数实现
MyString operator+(const MyString& s1, const MyString& s2) {
    MyString res;
    res._len = s1._len + s2._len;
    res._str = new char[res._len + 1];
    strcpy(res._str, s1._str);
    strcat(res._str, s2._str);
    return res;
}

bool operator==(const MyString& s1, const MyString& s2) {
    return strcmp(s1._str, s2._str) == 0;
}

ostream& operator<<(ostream& os, const MyString& s) {
    os << s._str;
    return os;
}
```

---

## 四、核心语法逐句解析（对话重点）

### 1. 赋值运算符重载声明

cpp

运行

```
MyString& operator=(const MyString& other)
```

表格

|语法部分|含义|为什么这么写？|
|---|---|---|
|`operator=`|重载赋值符号`=`|让自定义类支持 `a = b` 语法|
|`const MyString& other`|常量引用，传入源对象|1. 引用传递：不拷贝对象，效率高<br><br>2. const：保护源对象不被修改|
|`MyString&`|返回**当前对象的引用**|1. 支持连续赋值 `a = b = c`<br><br>2. 不拷贝对象，提升效率|
|`return *this`|返回当前对象本身|`this`是当前对象指针，`*this`是对象本体|

### 2. 赋值重载执行流程（必背）

1. **判断自赋值**：避免 `a = a` 时先删内存再拷贝，导致崩溃；
2. **释放旧内存**：防止内存泄漏；
3. **深拷贝**：开辟新内存 + 复制数据；
4. **返回引用**：支持连续赋值。

### 3. 拷贝构造函数

cpp

运行

```
MyString(const MyString& other)
```

- 调用时机：`MyString s2 = s1;` 或 `MyString s2(s1);`（用已有对象创建新对象）；
- 必须深拷贝，否则和浅拷贝有相同崩溃风险。

---

## 五、测试代码（验证功能）

cpp

运行

```cpp
int main() {
    MyString s1("Hello");
    MyString s2 = s1;        // 拷贝构造
    MyString s3;
    s3 = s2;                 // 赋值重载

    cout << "s1 = " << s1 << endl;
    cout << "s2 = " << s2 << endl;
    cout << "s1+s2 = " << s1 + s2 << endl;

    s1[0] = 'h';
    cout << "修改s1后：s1=" << s1 << "，s2=" << s2 << endl;
    return 0;
}
```

### 运行结果

plaintext

```cpp
s1 = Hello
s2 = Hello
s1+s2 = HelloHello
修改s1后：s1=hello，s2=Hello
```

✅ 深拷贝生效：修改`s1`不影响`s2`，内存安全。

---

## 六、关键避坑指南

1. **不重载赋值运算符的后果**
    
    编译器生成默认浅拷贝，程序运行崩溃（双重释放内存），**编译不报错，运行炸程序**。
    
2. **指针必须用深拷贝**
    
    只要类中有**堆内存指针**（`char*`、`int*`等），必须手动实现拷贝构造 + 赋值重载。
    
3. **赋值重载必须先释放旧内存**
    
    否则旧内存无法回收，造成**内存泄漏**。
    

---

## 七、笔记总结

1. 自定义 `String` 类的核心是**深拷贝**；
2. 四大函数缺一不可：构造、拷贝构造、赋值重载、析构；
3. 赋值重载：`const&`参数（高效安全）+ `返回引用`（支持连续赋值）；
4. 浅拷贝是坑，深拷贝是解。