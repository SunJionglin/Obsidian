# C++ 中的 `struct` 详解

## 一、什么是 `struct`？

`struct`（结构体）是 C++ 中一种**用户自定义数据类型**，用于将多个不同类型的数据（或函数）封装在一起，形成一个逻辑整体。其核心作用是 “数据聚合”，便于组织和管理相关联的数据。

`struct` 起源于 C 语言，在 C++ 中被大幅扩展，不仅能包含数据成员，还能包含成员函数、构造函数、继承等面向对象特性，功能上与 `class` 非常接近。

## 二、`struct` 的基本定义与使用

### 2.1 基本语法

cpp

```cpp
// 定义结构体类型
struct 结构体名 {
    成员类型1 成员名1;
    成员类型2 成员名2;
    // ... 更多成员
};  // 注意末尾的分号

// 定义结构体变量
struct 结构体名 变量名;  // C风格（C++中可省略struct关键字）
结构体名 变量名;        // C++风格（推荐）
```

### 2.2 示例：基础用法

cpp

```cpp
#include <iostream>
#include <string>
using namespace std;

// 定义一个"学生"结构体
struct Student {
    // 数据成员（默认访问权限为public）
    int id;         // 学号
    string name;    // 姓名
    int age;        // 年龄
};

int main() {
    // 定义结构体变量并初始化
    Student s1 = {1001, "张三", 18};  // 按成员顺序初始化（聚合初始化）
    
    // 访问成员（通过 . 运算符）
    cout << "学号：" << s1.id << endl;
    cout << "姓名：" << s1.name << endl;
    cout << "年龄：" << s1.age << endl;
    
    // 修改成员
    s1.age = 19;
    cout << "修改后年龄：" << s1.age << endl;
    
    return 0;
}
```

输出：

plaintext

```plaintext
学号：1001
姓名：张三
年龄：18
修改后年龄：19
```

## 三、C++ 中 `struct` 与 C 中 `struct` 的区别

|特性|C 语言中的 `struct`|C++ 中的 `struct`|
|---|---|---|
|成员类型|只能包含数据成员（变量）|可包含数据成员、成员函数、构造函数、析构函数等|
|访问控制|所有成员默认 public（无访问控制）|默认 public（但可通过 `public`/`private` 控制）|
|继承|不支持|支持继承（默认 public 继承）|
|模板|不支持|支持作为模板参数或定义模板结构体|
|关键字省略|定义变量时必须加 `struct` 关键字|可省略 `struct` 关键字（如 `Student s;`）|

## 四、C++ `struct` 的高级特性

### 4.1 包含成员函数

C++ 的 `struct` 可以像 `class` 一样包含成员函数，实现 “数据 + 操作” 的封装。

cpp

```cpp
struct Circle {
    // 数据成员
    double radius;  // 半径
    
    // 成员函数（计算面积）
    double area() {
        return 3.14159 * radius * radius;
    }
    
    // 成员函数（计算周长）
    double perimeter() {
        return 2 * 3.14159 * radius;
    }
};

int main() {
    Circle c;
    c.radius = 5.0;
    cout << "面积：" << c.area() << endl;       // 输出：78.5397
    cout << "周长：" << c.perimeter() << endl;   // 输出：31.4159
    return 0;
}
```

### 4.2 构造函数与析构函数

`struct` 可以定义构造函数（初始化对象）和析构函数（清理资源），与 `class` 用法一致。

cpp

```cpp
struct Book {
    string title;   // 书名
    string author;  // 作者
    int pages;      // 页数
    
    // 默认构造函数（无参）
    Book() {
        title = "未知";
        author = "未知";
        pages = 0;
    }
    
    // 带参构造函数
    Book(string t, string a, int p) {
        title = t;
        author = a;
        pages = p;
    }
    
    // 析构函数（示例：打印销毁信息）
    ~Book() {
        cout << "《" << title << "》已销毁" << endl;
    }
};

int main() {
    Book b1;  // 调用默认构造函数
    cout << b1.title << endl;  // 输出：未知
    
    Book b2("C++ Primer", "Stanley", 1000);  // 调用带参构造函数
    cout << b2.title << endl;  // 输出：C++ Primer
    
    return 0;  // 程序结束时自动调用析构函数
}
```

输出：

plaintext

```plaintext
未知
C++ Primer
《C++ Primer》已销毁
《未知》已销毁
```

### 4.3 访问控制（`public`/`private`/`protected`）

C++ 的 `struct` 支持访问控制关键字，默认成员为 `public`（与 `class` 相反，`class` 默认 `private`）。

cpp

```cpp
struct Person {
public:  // 公开成员（外部可直接访问）
    string name;
    
private:  // 私有成员（仅内部或友元可访问）
    int age;
    
public:  // 公开成员函数（可访问私有成员）
    void setAge(int a) {
        if (a > 0) age = a;  // 内部可访问私有成员
    }
    
    int getAge() {
        return age;
    }
};

int main() {
    Person p;
    p.name = "李四";  // 正确：public成员可直接访问
    p.setAge(20);     // 正确：通过public函数访问private成员
    cout << p.getAge() << endl;  // 输出：20
    // p.age = 20;  // 错误：private成员不可直接访问
    return 0;
}
```

### 4.4 继承

`struct` 支持继承，默认继承方式为 `public`（`class` 默认 `private` 继承）。

cpp

```cpp
// 基类（父类）
struct Animal {
    void eat() {
        cout << "动物吃东西" << endl;
    }
};

// 派生类（子类）：public继承Animal（struct默认）
struct Dog : Animal {  // 等价于 struct Dog : public Animal
    void bark() {
        cout << "狗叫：汪汪" << endl;
    }
};

int main() {
    Dog d;
    d.eat();  // 继承自Animal的成员函数
    d.bark(); // 自身的成员函数
    return 0;
}
```

输出：

plaintext

```plaintext
动物吃东西
狗叫：汪汪
```

### 4.5 模板结构体

`struct` 可以与模板结合，定义通用数据结构（如链表节点、容器等）。

cpp

```cpp
// 模板结构体：存储一对不同类型的数据
template <typename T1, typename T2>
struct Pair {
    T1 first;  // 第一个元素
    T2 second; // 第二个元素
    
    // 构造函数
    Pair(T1 f, T2 s) : first(f), second(s) {}
};

int main() {
    Pair<int, string> p1(1, "one");  // 第一个元素int，第二个string
    Pair<double, char> p2(3.14, 'a'); // 第一个double，第二个char
    
    cout << p1.first << " : " << p1.second << endl;  // 1 : one
    cout << p2.first << " : " << p2.second << endl;  // 3.14 : a
    return 0;
}
```

## 五、`struct` 与 `class` 的异同

C++ 中 `struct` 和 `class` 功能几乎完全一致，唯一区别在于**默认访问权限**和**默认继承方式**：

|特性|`struct`|`class`|
|---|---|---|
|默认成员访问权限|`public`|`private`|
|默认继承方式|`public` 继承|`private` 继承|
|其他特性|支持构造函数、析构函数、多态等|支持构造函数、析构函数、多态等|

## 六、`struct` 的适用场景

1. **数据载体**：当需要一个纯粹的数据容器（如存储坐标、配置信息等），且成员通常需要公开访问时，优先用 `struct`。
    
    示例：`struct Point { int x; int y; };`
    
2. **与 C 兼容**：若代码需要与 C 语言交互（如跨语言调用），`struct` 更适合（C 不支持 `class`）。
    
3. **POD 类型**：`struct` 更容易满足 “Plain Old Data”（POD）类型要求（如无自定义构造函数、析构函数等），POD 类型在内存布局上与 C 兼容，适合二进制序列化。
    
4. **强调 “数据聚合” 而非 “封装”**：当逻辑上更偏向 “一组相关数据的集合” 而非 “具有复杂行为的对象” 时，用 `struct` 更符合语义。
    

## 七、总结

- `struct` 是 C++ 中用于封装数据和操作的自定义类型，起源于 C 但功能更强大。
- 支持成员函数、构造函数、继承、模板等面向对象特性，与 `class` 仅在默认访问权限和继承方式上有区别。
- 适合作为数据载体、与 C 兼容场景，或强调 “数据聚合” 的场景。

合理使用 `struct` 可以让代码更清晰、更符合逻辑，尤其在处理结构化数据时非常高效。