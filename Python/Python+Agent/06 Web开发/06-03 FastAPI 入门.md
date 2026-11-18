---
title: FastAPI 入门
chapter: 6
section: 3
course: Python+AI 从入门到大神
tags: [Python, Web开发, 类型/语法, 难度/入门]
difficulty: 入门
status: 待复习
source: 第6章 PPT
created: 2026-10-22
aliases: [FastAPI, uvicorn, 路由, pydantic]
---

<!-- filename: 06-03 FastAPI 入门.md -->

## 0. 速记

> [!tip] 五句话
> - Web = 前端（展示）+ 后端（逻辑）+ 数据库（存储）
> - FastAPI 四步：导入 → `app = FastAPI()` → 装饰器定义路径 → uvicorn 启动
> - 函数返回 dict/list，FastAPI 自动转 JSON
> - 请求体用 Pydantic 模型声明，自动校验、自动出文档
> - 启动后访问 `/docs` 就有交互式 API 文档

## 1. 语法速查

### 1.1 最小应用

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "张三"}]
```

### 1.2 启动

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
# 或
fastapi dev main.py
```

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 1.3 三类参数

```python
# 路径参数
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

# 查询参数（没在路径里的参数自动当查询参数）
@app.get("/users")
def list_users(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

# 请求体（Pydantic 模型）
from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/api/chat")
def chat(req: ChatRequest):
    return {"reply": req.message}
```

### 1.4 返回文件与静态资源

```python
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

@app.get("/")
def index():
    return FileResponse("static/index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")
```

## 2. 与 C++ 的差异

| 维度 | C++ | FastAPI |
|---|---|---|
| Web 框架 | Crow / Drogon / cpp-httplib | FastAPI |
| 路由 | 手写注册 | 装饰器 |
| JSON | nlohmann/json 手动序列化 | 返回 dict 自动转 |
| 参数校验 | 手写 | Pydantic 自动 |
| 接口文档 | 手写 Swagger | `/docs` 自动生成 |
| 启动 | 编译后运行 | `uvicorn` 热重载 |
| 类型检查 | 编译期 | 运行期 + 类型提示 |

## 3. 易漏点

- **装饰器决定方法**：`@app.get` 和 `@app.post` 是两条不同的路由。
- **返回值自动 JSON**：返回 dict/list 即可，不用手动 `json.dumps`。
- **路径参数要写进 URL**：`/users/{user_id}`，函数参数名要一致。
- **请求体必须用模型**：直接写 `def chat(data: dict)` 拿不到自动校验。
- **`--reload` 只用于开发**：生产别开。
- **路由顺序**：`/users/{id}` 写在 `/users/me` 前面会吞掉后者。
- **端口占用**：8000 被占就换 8001。

## 4. 易错点

> [!warning] 只写了函数没启动
> 代码没错但访问不了，忘了 `uvicorn main:app --reload`。

> [!warning] 路径参数类型不匹配
> `user_id: int`，访问 `/users/abc` 直接 422。

> [!warning] Pydantic 校验失败
> 少字段或类型不对 → 422，响应里有具体字段错误。

> [!warning] 路由被通配路径吞掉
> `/users/{user_id}` 放在 `/users/me` 前面，`me` 被当成 id。

> [!warning] 静态文件 404
> `directory` 是相对启动目录的，不是相对脚本。

> [!warning] 改了代码没生效
> 没加 `--reload`，或 reload 失败，手动重启。

## 5. 自测

> [!question]- FastAPI 定义一个 GET 接口最少要几步？
> **答案**：导入 `FastAPI`、创建 `app`、用 `@app.get("/路径")` 装饰函数、启动服务。

> [!question]- 路径参数和查询参数怎么区分？
> **答案**：写在路径模板里的 `{name}` 是路径参数；函数里其余带默认值的参数自动成为查询参数。

> [!question]- 请求体为什么要用 Pydantic 模型？
> **答案**：自动解析 JSON、校验字段类型、生成文档；校验失败返回 422。

## 6. 关联

- 上游：[[06-02 图书管理系统]]
- 下游：[[06-04 RESTful]]、[[06-05 汉字谜盒实战]]
- 课程原文：第 6 章 PPT，第 30–38 页
- 代码：`第6章/08_FastAPI入门.py`
