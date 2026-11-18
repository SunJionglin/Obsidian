

## 一、基本定义与头文件

|特性|C 风格数组|`std::array`（C++11 及以上）|
|:--|:--|:--|
|**定义语法**|`type arr[N];`<br><br>例：`int arr[3];`|`std::array<type, N> arr;`<br><br>例：`std::array<int, 3> arr;`|
|**依赖头文件**|无，C/C++ 原生支持|需包含 `<array>` 头文件|
|**长度要求**|`N` 必须是编译期常量|`N` 必须是编译期常量|
|**本质**|连续内存的元素集合，数组名可退化为指针|封装 C 风格数组的模板类，属于容器|

## 二、核心功能与用法对比

|操作场景|C 风格数组|`std::array`|
|:--|:--|:--|
|**初始化**|1. 未初始化：元素值随机（栈上）/ 0（全局）<br><br>`int arr[3];`<br><br>2. 列表初始化：<br><br>`int arr[3] = {1,2,3};`<br><br>`int arr[] = {1,2,3};`（长度自动推导为 3）|1. 未初始化：元素值随机<br><br>`std::array<int,3> arr;`<br><br>2. 列表初始化：<br><br>`std::array<int,3> arr = {1,2,3};`<br><br>3. 聚合初始化（C++11）：<br><br>`std::array<int,3> arr{1,2,3};`|
|**获取长度**|1. 手动硬编码：`3`<br><br>2. 用 `sizeof` 计算：<br><br>`int len = sizeof(arr)/sizeof(arr[0]);`|1. 成员函数 `size()`（推荐）：<br><br>`int len = arr.size();`<br><br>2. 静态成员 `size()`：<br><br>`int len = std::array<int,3>::size();`|
|**元素访问**|1. 下标访问（无越界检查）：`arr[0]`<br><br>2. 指针访问：`*(arr+1)`|1. 下标访问（无越界检查）：`arr[0]`<br><br>2. `at()` 方法（有越界检查，抛异常）：<br><br>`arr.at(0);`<br><br>3. 指针访问：`*(arr.data())`|
|**遍历方式**|1. 普通 for 循环：<br><br>`for(int i=0; i<3; i++){}`<br><br>2. 范围 for（C++11）：<br><br>`for(int num : arr){}`|1. 普通 for 循环：<br><br>`for(int i=0; i<arr.size(); i++){}`<br><br>2. 范围 for：<br><br>`for(int num : arr){}`<br><br>3. 迭代器遍历：<br><br>`for(auto it=arr.begin(); it!=arr.end(); it++){}`|
|**拷贝赋值**|不支持直接赋值：<br><br>`int arr1[3] = {1,2,3};`<br><br>`int arr2[3] = arr1;` ❌ 报错|支持直接赋值：<br><br>`std::array<int,3> arr1{1,2,3};`<br><br>`std::array<int,3> arr2 = arr1;` ✅ 合法|
|**`std::sort` 排序**|需传指针作为迭代器：<br><br>`sort(arr, arr+3);`<br><br>头文件 `<algorithm>`|用迭代器范围：<br><br>`sort(arr.begin(), arr.end());`<br><br>头文件 `<algorithm>`|
|**与 STL 算法兼容**|需手动传递首尾指针，兼容性差|原生支持迭代器，完美兼容所有 STL 算法|

## 三、安全性对比

|风险点|C 风格数组|`std::array`|
|:--|:--|:--|
|**越界访问**|下标访问 `arr[5]` 无检查，导致未定义行为|1. 下标访问 `arr[5]` 无检查<br><br>2. `at(5)` 会抛出 `std::out_of_range` 异常，可捕获|
|**数组名退化**|数组名易退化为指针，导致误判类型：<br><br>`void func(int arr[])` 实际是 `int* arr`|不会退化，类型始终是 `std::array<type,N>`，传递时不会丢失长度信息|
|**命名冲突**|数组名若与库函数重名（如 `abs`），会屏蔽函数|属于 `std` 命名空间，不会与全局标识符冲突|

## 四、适用场景

|数组类型|适用场景|不适用场景|
|:--|:--|:--|
|**C 风格数组**|1. 兼容 C 语言代码的场景<br><br>2. 追求极致精简，不依赖 STL 的环境|1. 需要频繁拷贝、赋值的场景<br><br>2. 对安全性要求高，需避免越界的场景<br><br>3. 大量使用 STL 算法的场景|
|**`std::array`**|1. 纯 C++ 开发，需要类型安全、易维护的代码<br><br>2. 需使用 STL 算法，或需要直接拷贝的场景<br><br>3. 希望通过 `at()` 做越界检查的场景|1. 必须兼容 C 语言的接口（可通过 `data()` 转指针）<br><br>2. 编译环境不支持 C++11 及以上|

## 五、关键总结

1. **`std::array` 是 C 风格数组的升级版**：保留了 C 风格数组的高效性，弥补了其安全性和易用性的缺陷。
2. **纯 C++ 项目优先用 `std::array`**：尤其是需要拷贝、迭代器、越界检查的场景。
3. **兼容 C 代码用 C 风格数组**：或通过 `std::array` 的 `data()` 方法获取内部指针，对接 C 接口。