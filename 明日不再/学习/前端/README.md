# 前端 · 有空就学

> **在总纲里的位置**：[[00-总纲]] 的**全程可选项**。任何阶段吃紧，第一个停的就是它，不算欠债。

> 不占主线时间。什么时候有空什么时候来，学多少算多少，不许影响 W1–W3 的清单。
> 目标只有一个：**能独立做出可用的界面**，不是做前端专家。

---

## 零、怎么用这份文件

- 三个关卡 L1 → L2 → L3，一关过了再进下一关，别跳
- 每关都有「知识点」「验收项目」「常见坑」，验收项目做不出来就不算过
- 每次学完在文件末尾的「进度」里记一行，写清今天学了什么、卡在哪
- 时间不够就停，别硬撑，主线永远优先

---

## 一、L1 页面 · 约 40 小时

### 知识点

**HTML（8 小时）**
- 文档结构：`html`、`head`、`body`、`meta charset`、`meta viewport`
- 语义标签：`header`、`nav`、`main`、`section`、`article`、`aside`、`footer`
- 文本：`h1`–`h6`、`p`、`strong`、`em`、`code`、`pre`、`blockquote`
- 列表：`ul`、`ol`、`dl`
- 链接与图片：`a`（target、rel）、`img`（alt、loading="lazy"）
- 表格：`table`、`thead`、`tbody`、`th`、`td`
- 表单：`form`、`input` 各 type、`label` 与 for、`select`、`textarea`、`button`、`fieldset`
- 无障碍基础：alt 必须写、按钮用 button 不用 div、表单要有 label

**CSS（20 小时）**
- 选择器：类、id、后代、子代、属性、伪类（`:hover`、`:focus`、`:nth-child`）
- 盒模型：content、padding、border、margin，`box-sizing: border-box`
- 单位：px、rem、em、%、vw/vh，什么时候用哪个
- 排版：字体栈、行高、字重、字间距、`text-align`
- 颜色：hex、rgb、hsl、透明度、渐变
- 布局：`display` 各值、`position` 五种、`z-index`
- Flex：主轴交叉轴、`justify-content`、`align-items`、`flex-wrap`、`gap`
- Grid：`grid-template-columns`、`fr`、`gap`、`minmax`、`auto-fit`
- 响应式：媒体查询断点、移动优先写法
- 常用技巧：居中三种写法、等高卡片、粘顶导航、图片自适应

**调试（4 小时）**
- 浏览器 DevTools：Elements 面板改样式、盒模型高亮
- 看计算样式，判断是谁覆盖了谁
- 设备模式下测不同宽度

**工具（8 小时）**
- 一个编辑器插件：Prettier 格式化
- 一个组件库起步：先会用现成按钮、卡片、输入框
- 一个图标库

### 验收项目
**静态个人页**：导航栏、Hero 区、三张卡片、页脚；桌面和手机宽度都不塌；顶部导航滚动时吸顶。

### 常见坑
- 用 `div` 当按钮，键盘按不了
- 不加 `box-sizing`，宽度算到怀疑人生
- 只写死像素，手机上一屏放不下
- 图片不写 `alt`，无障碍直接挂
- 用 `float` 布局，被现代写法吊打

---

## 二、L2 交互 · 约 60 小时

### 知识点

**JS 基础（20 小时）**
- 变量：`let`、`const`，为什么不用 `var`
- 类型：string、number、boolean、null、undefined、object、array
- 运算：`===` 与 `==`、`??`、`?.`
- 字符串：模板字符串、常用方法
- 数组：`map`、`filter`、`find`、`reduce`、`sort`、`some`、`every`
- 对象：取值、解构、展开、`Object.keys/values/entries`
- 函数：箭头函数、默认参数、回调
- 条件与循环：`if`、`switch`、`for`、`for...of`
- 作用域与闭包：知道闭包能存住变量就够

**DOM 与事件（20 小时）**
- 选中：`querySelector`、`querySelectorAll`
- 改内容：`textContent`、`innerHTML`（注意 XSS）
- 改样式与类：`classList`、`style`
- 建元素：`createElement`、`append`、`remove`
- 事件：`addEventListener`、事件对象、冒泡与委托、`preventDefault`
- 表单：取值、校验、提交拦截
- 存储：`localStorage` 读写与 JSON 序列化

**异步（15 小时）**
- 回调与回调地狱
- Promise：`then`、`catch`、`finally`
- async/await、`try/catch`
- `fetch`：GET、POST、JSON、状态码判断
- 并发：`Promise.all`
- 加载态、错误态、空态、超时

**调试（5 小时）**
- Console 各方法
- Sources 断点、单步、看作用域
- Network 看请求与响应、看 CORS 报错

### 验收项目
**一个调接口的页面**：搜索框输入关键词，请求接口，列表展示结果；有加载动画、无结果提示、请求失败提示；用 `localStorage` 记住上次搜索。

### 常见坑
- `innerHTML` 拼用户输入，被 XSS
- 忘了 `await`，拿到 Promise 当数据用
- 事件绑在新增的元素上，绑不上
- 不判断 `response.ok`，404 当成成功
- 请求竞态，后发的先回，列表被旧数据覆盖（要会取消或用序号判断）

---

## 三、L3 工程 · 约 40 小时

### 知识点

**React（18 小时）**
- 组件与 JSX、props、children
- 状态：`useState`
- 副作用：`useEffect`、依赖数组、清理函数
- 事件与受控组件
- 列表渲染与 `key`
- 条件渲染
- 自定义 hook 入门
- 上下文：`createContext` + `useContext`（够用即可）
- 路由：`react-router` 基本用法

**工程化（12 小时）**
- 包管理：npm 或 pnpm，`package.json` 的 scripts 与依赖
- Vite：起项目、开发服务器、环境变量 `import.meta.env`
- 组件库接入：安装、主题、按需引入
- 样式方案：CSS Modules 或 Tailwind，选一个
- 构建产物：`dist` 目录、静态资源路径

**联调与部署（10 小时）**
- 接口约定：请求体、响应结构、错误码
- 跨域：CORS 是什么，开发代理怎么配
- 部署：静态托管（Vercel / Netlify）或 Nginx
- 环境区分：本地、测试、线上接口地址
- 上线后自测：缓存、路径、刷新 404

### 验收项目
**能上线的小应用**：至少两个页面（列表页 + 详情页），路由可跳转，数据来自你自己的后端接口，部署后有公开地址。

### 常见坑
- `useEffect` 依赖写不全，数据不更新；写多了，请求死循环
- 列表 `key` 用下标，删一项渲染错乱
- 部署后刷新 404，要配 history fallback
- 环境变量写死在后端地址，换域名就挂
- 打包后图片路径错，忘记 `public` 目录

---

## 四、四个练手项目（按顺序做）

### 1. 静态个人页（L1）
- 导航、Hero、卡片区、页脚
- 桌面与手机两套布局
- 导航吸顶，有滚动阴影

### 2. 待办清单（L2 前半）
- 增删改查，勾选完成
- 数据存 `localStorage`，刷新不丢
- 按完成状态筛选
- 空状态有提示文案

### 3. 接口页（L2 后半）
- 搜索 + 列表 + 分页
- 加载、空、错误三态齐全
- 请求失败可重试
- 处理竞态

### 4. 上线小应用（L3）
- 接自己的后端，两个页面
- 路由、样式统一
- 部署到公网，能发给别人看

---

## 五、学习节奏建议

- 每次 40 分钟就够，超过一小时效率下降
- 一周三到四次，别攒到周末一次做三小时
- 学完立刻动手写，看完不算学会
- 每周挑一个坑记下来，比记十个概念有用

---

## 六、资源

- MDN Web Docs，查标签、查 API，最权威
- React 官方文档的「Learn React」部分，建议配合中文版
- Vite 官方文档，起项目与配置
- freeCodeCamp 的前端部分，练手可用
- 遇到布局问题，先看 DevTools 的盒模型高亮，再看文档

---

## 七、先不要碰

- Next、Nuxt 这类 SSR 框架
- 微前端、Monorepo
- Redux 之类的复杂状态管理
- 框架源码与渲染原理
- 动画库、Canvas、WebGL

这些等你工作一两年、真碰上需求再学，现在学只会占脑容量。

---

## 八、进度

| 日期 | 学了什么 | 卡在哪 | 下一步 |
| --- | --- | --- | --- |
|  |  |  |  |

- 开始日期：
- 当前关卡：L1 / L2 / L3
- 完成的练手项目：无 / 1 / 2 / 3 / 4

---

## 九、和主线的关系

- 主线是 Python 后端 + AI 应用，前端只是让你显得「能独立把东西做完」
- 学到的东西优先用在项目 B、C 上，不要只做练习不落地
- 主线吃紧的时候，这边直接停，不算欠债
