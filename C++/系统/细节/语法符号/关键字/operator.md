# 核心概念

`operator` 是 C++ 关键字 = **运算符重载**

- 默认 `+`/`==`/`=` 只能给 `int`/`double` 用
- 用 `operator` 可以**给自定义类重新定义运算符的用法**
- 让**对象**能像普通数字一样做运算

---

# 例子 1：最简单的 + 号重载

我们定义一个 **坐标类 Point**，让两个坐标能直接用 `+` 相加

cpp

运行

```
#include <iostream>
using namespace std;

// 自定义类：坐标 (x, y)
class Point {
private:
    int x, y;

public:
    // 构造函数
    Point(int x_, int y_) : x(x_), y(y_) {}

    // ✅ operator+：重载 + 号
    // 作用：让两个 Point 对象可以直接相加
    Point operator+(const Point& other) {
        // 新坐标 = 自身x + 对方x，自身y + 对方y
        return Point(x + other.x, y + other.y);
    }

    // 打印坐标
    void show() {
        cout << "x=" << x << ", y=" << y << endl;
    }
};

int main() {
    Point a(1, 2);   // 坐标(1,2)
    Point b(3, 4);   // 坐标(3,4)

    // ✅ 直接用 + 号！这就是 operator+ 的作用
    Point c = a + b; 

    c.show(); // 输出 x=4, y=6
    return 0;
}
```

---

# 例子 2：重载 == 号（判断相等）

给上面的类，加一个**判断两个坐标是否相等**的功能

cpp

运行

```
// 在 Point 类里添加
// ✅ operator==：重载 == 号
bool operator==(const Point& other) {
    // x和y都相等，才返回true
    return (x == other.x) && (y == other.y);
}
```

使用：

cpp

运行

```
Point a(1,2);
Point b(1,2);

if(a == b){  // ✅ 直接用 == 号
    cout << "两个坐标相等";
}
```

---

# 例子 3：重载 = 号（赋值）

cpp

运行

```
// ✅ operator=：重载赋值号
Point& operator=(const Point& other) {
    x = other.x;
    y = other.y;
    return *this;
}
```

使用：

cpp

运行

```
Point a(1,2);
Point b(5,6);
b = a;  // ✅ 直接用 = 号
```

---

# 万能语法公式（背会）

cpp

运行

```
返回值 operator 你要重载的符号 (参数) {
    // 自定义运算逻辑
}
```

---

# 一句话总结

1. `operator` = **给自定义类，重新定义运算符**
2. 没有它：`对象 + 对象` 直接报错
3. 有它：`对象 + 对象` / `对象 == 对象` 都能正常用
4. 你想让哪个符号生效，就重载哪个符号！