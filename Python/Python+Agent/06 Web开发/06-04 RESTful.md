---
title: RESTful
chapter: 6
section: 4
course: Python+AI 从入门到大神
tags: [Python, Web开发, 类型/概念, 难度/入门]
difficulty: 入门
status: 待复习
source: 第6章 PPT
created: 2026-10-22
aliases: [REST, API设计, 幂等]
---

<!-- filename: 06-04 RESTful.md -->

## 0. 速记

> [!tip] 五句话
> - URL 表示「资源」，HTTP 方法表示「动作」
> - GET 查、POST 增、PUT 改、DELETE 删
> - URL 用名词复数：`/users`、`/users/5`，不要 `/getUser`
> - GET / PUT / DELETE 幂等，POST 不幂等
> - 状态码要如实：200 成功、201 创建、404 不存在、422 校验失败

## 1. 语法速查

### 1.1 资源与动作

| 操作 | 方法 | URL 示例 |
|---|---|---|
| 查列表 | `GET` | `/api/users` |
| 查单个 | `GET` | `/api/users/5` |
| 新增 | `POST` | `/api/users` |
| 全量修改 | `PUT` | `/api/users/5` |
| 部分修改 | `PATCH` | `/api/users/5` |
| 删除 | `DELETE` | `/api/users/5` |

### 1.2 FastAPI 写法

```python
@app.get("/api/sessions")
def list_sessions(): ...

@app.post("/api/sessions")
def create_session(): ...

@app.get("/api/sessions/{session_id}")
def get_session(session_id: str): ...

@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str): ...
```

### 1.3 状态码

| 状态码 | 含义 |
|---|---|
| `200` | 成功 |
| `201` | 已创建（POST 新增） |
| `204` | 成功但无返回体（DELETE） |
| `400` | 请求参数错误 |
| `401` / `403` | 未认证 / 无权限 |
| `404` | 资源不存在 |
| `422` | 参数校验失败（FastAPI 默认） |
| `500` | 服务端异常 |

### 1.4 幂等性

同一请求执行多次，结果是否一致：

| 方法 | 幂等 | 说明 |
|---|---|---|
| `GET` | 是 | 查多少次都一样 |
| `PUT` | 是 | 全量覆盖，重复执行结果相同 |
| `DELETE` | 是 | 删了再删，资源都是不存在 |
| `POST` | 否 | 每次都可能新建一条 |

## 2. 与 C++ 的差异

REST 是设计风格，和语言无关。区别在「接口思维方式」：

| 维度 | RPC 风格 | REST 风格 |
|---|---|---|
| URL | `/getUser`、`/deleteUser` | `/users/5` |
| 动作 | 写在 URL 里 | 用 HTTP 方法 |
| 返回 | 自定义结构 | 资源 + 状态码 |
| 缓存 | 难 | GET 天然可缓存 |
| 学习成本 | 低 | 需要理解资源建模 |
| 扩展 | 加动作就加 URL | 加资源即可 |

## 3. 易漏点

- **URL 用名词**：`/users` 而不是 `/getUsers`。
- **复数 + 层级**：`/users/5/orders` 表示 5 号用户的订单。
- **PUT 是全量替换**：只传一个字段会把其他字段清空，部分更新用 PATCH。
- **DELETE 成功可返回 204**：不必返回被删对象。
- **版本号放 URL**：`/api/v1/users`，方便以后升级。
- **过滤用查询参数**：`/users?page=2&size=10`。

## 4. 易错点

> [!warning] URL 里带动词
> `/api/getUser`、`/api/deleteUser` 不是 REST。改成 `/api/users/5` + 方法。

> [!warning] 用 GET 做删除
> 浏览器预取、爬虫会误触发。删除必须用 DELETE 或 POST。

> [!warning] 所有响应都返回 200
> 业务失败也 200，前端没法区分。用状态码表达结果。

> [!warning] POST 当 PUT 用
> POST 不幂等，重试会重复创建；全量更新用 PUT。

> [!warning] 层级过深
> `/a/1/b/2/c/3/d/4` 难维护。超过两层就拆接口。

## 5. 自测

> [!question]- 删除 id 为 5 的用户，REST 风格的 URL 和方法是什么？
> **答案**：`DELETE /api/users/5`。

> [!question]- 为什么 POST 不幂等？
> **答案**：每次调用都可能新建一条记录，重复提交会产生多条。

> [!question]- PUT 和 PATCH 的区别？
> **答案**：PUT 全量替换，PATCH 只改传入的字段。

## 6. 关联

- 上游：[[06-03 FastAPI 入门]]
- 下游：[[06-05 汉字谜盒实战]]
- 课程原文：第 6 章 PPT，第 41–44 页
- 代码：`第6章/汉字谜盒/main.py`
