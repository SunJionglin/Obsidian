

## 一、ISBN 码验证需求概述

ISBN 码格式为`x-xxx-xxxxx-x`（共 13 个字符），包含 9 位有效数字、3 个分隔符`-`和 1 位识别码。识别码计算规则：

- 前 9 位数字分别乘以 1~9 的权重并求和
- 总和对 11 取模，结果为 0~9 时，识别码为对应数字；结果为 10 时，识别码为`X`
- 程序需验证识别码正确性，正确输出`Right`，错误则输出修正后的完整 ISBN

## 二、常见代码错误分类与修正

### 1. 数组越界访问

#### 错误表现

cpp

运行

```cpp
char isb_arr[13];
cin >> isb_arr[13];  // 访问下标13（越界）
if (num%11 == isb_arr[13]-'0')  // 持续越界访问
```

#### 错误原因

- 数组`isb_arr[13]`的有效下标范围是`0~12`（共 13 个元素）
- 识别码位于最后一位，正确下标为`12`（`13-1=12`）

#### 修正方法

cpp

运行

```cpp
char isb_arr[13];
cin >> isb_arr;  // 正确读取整个字符串到数组
if (num%11 == isb_arr[12]-'0')  // 使用正确下标12
```

### 2. 输入方式错误

#### 错误表现

cpp

运行

```cpp
cin >> isb_arr[13];  // 仅读取单个字符（还是越界位置）
```

#### 错误原因

- 误解了数组输入方式，ISBN 是完整字符串（13 个字符），需整体输入
- 数组名本身可代表首地址，直接接收字符串输入

#### 修正方法

cpp

运行

```cpp
cin >> isb_arr;  // 正确方式：将整个ISBN字符串存入数组
```

### 3. 逻辑判断错误

#### 错误表现

cpp

运行

```cpp
// 括号位置错误导致逻辑混乱
if (num%11==isb_arr[12]-'0'|| num%11==10 && isb_arr[12]=='X')
// 或错误嵌套
if (num%11==(isb_arr[12]-'0'|| num%11==10) && isb_arr[12]=='X')
```

#### 错误原因

- 未正确处理`||`与`&&`的优先级（`&&`优先级高于`||`）
- 识别码正确的条件是**两种互斥情况**：
    1. 余数为 0~9 且等于识别码数字
    2. 余数为 10 且识别码是`X`

#### 修正方法

cpp

运行

```cpp
// 用括号明确两种情况，逻辑清晰
if ((num%11 == isb_arr[12]-'0') || (num%11 == 10 && isb_arr[12] == 'X'))
```

### 4. 字符与整数转换错误

#### 错误表现

cpp

运行

```cpp
isb_arr[12] = num%11;  // 直接将整数赋值给字符数组
```

#### 错误原因

- `num%11`是整数（如 3），而`isb_arr`是字符数组，需存储字符形式的数字（如`'3'`）
- 字符`'0'~'9'`的 ASCII 码是连续的，整数转字符需加`'0'`

#### 修正方法

cpp

运行

```cpp
isb_arr[12] = num%11 + '0';  // 正确转换：3 + '0' = '3'
```

### 5. 输出语句位置错误

#### 错误表现

cpp

运行

```cpp
else{
    if(num%11==10){
        isb_arr[12]='X';  // 修正后未输出
    } else {
        isb_arr[12]=num%11+'0'; 
        cout<<isb_arr<<endl;  // 仅该分支有输出
    }
}
```

#### 错误原因

- 当识别码需修正为`X`时，未添加输出语句，导致程序不输出结果
- 题目要求：识别码错误时必须输出**完整的正确 ISBN**（无论修正为数字还是`X`）

#### 修正方法

cpp

运行

```cpp
else{
    if(num%11==10){
        isb_arr[12]='X';
    } else {
        isb_arr[12]=num%11+'0';
    }
    cout << isb_arr << endl;  // 统一输出，两种情况都覆盖
}
```

### 6. 循环范围问题

#### 错误表现

cpp

运行

```cpp
// 虽结果正确但可读性差
for(int i=0;i<sizeof(isb_arr)-1;i++)
```

#### 优化建议

cpp

运行

```cpp
// 直接使用12更直观（前12个字符不含识别码）
for(int i=0; i<12; i++)
```

## 三、正确代码实现

cpp

运行

```cpp
#include <iostream>
using namespace std;

int main() {
    char isb_arr[13];  // 存储13位ISBN（0~12下标）
    cin >> isb_arr;    // 读取完整ISBN字符串

    int num = 0;       // 加权和
    int weight = 1;    // 权重（1~9）

    // 遍历前12个字符（排除最后一位识别码）
    for(int i = 0; i < 12; i++) {
        if(isb_arr[i] == '-') {  // 跳过分隔符
            continue;
        }
        num += weight * (isb_arr[i] - '0');  // 字符转数字并计算加权和
        weight++;
    }

    // 验证识别码
    if ((num%11 == isb_arr[12]-'0') || (num%11 == 10 && isb_arr[12] == 'X')) {
        cout << "Right" << endl;
    } else {
        // 修正识别码
        if(num%11 == 10) {
            isb_arr[12] = 'X';
        } else {
            isb_arr[12] = num%11 + '0';
        }
        cout << isb_arr << endl;  // 输出完整正确ISBN
    }

    return 0;
}
```

## 四、关键注意事项

1. **数组下标规则**：n 个元素的数组，下标范围是`0~n-1`，避免越界
2. **字符转换**：数字转字符加`'0'`（如`3→'3'`），字符转数字减`'0'`（如`'5'→5`）
3. **逻辑优先级**：`&&`高于`||`，复杂条件用括号明确范围
4. **输出完整性**：错误修正后必须输出完整 ISBN（含分隔符），不能只输出识别码
5. **代码可读性**：合理缩进、明确循环范围，提升可维护性

通过避免上述错误，可正确实现 ISBN 码的验证功能，确保边界情况和特殊情况（如识别码为`X`）都能正确处理。

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string isbn;  // 用字符串存储ISBN，方便处理分隔符
    cin >> isbn;
    
    int sum = 0;
    int numIndex = 0;  // 记录前9位数字的索引
    
    // 提取前9位有效数字并计算总和
    for (int i = 0; i < isbn.size() - 1; i++) {  // 排除最后一位识别码
        if (isbn[i] == '-') continue;  // 跳过分隔符
        // 将字符数字转为整数，乘以对应权重（1-9）
        sum += (isbn[i] - '0') * (++numIndex);
    }
    
    // 计算正确的识别码
    int mod = sum % 11;
    char correctCode;
    if (mod == 10) {
        correctCode = 'X';
    } else {
        correctCode = '0' + mod;
    }
    
    // 对比输入的识别码与计算结果
    if (isbn.back() == correctCode) {
        cout << "Right" << endl;
    } else {
        // 输出正确的ISBN
        isbn[isbn.size() - 1] = correctCode;
        cout << isbn << endl;
    }
    
    return 0;
}

```
用string的另一种可能