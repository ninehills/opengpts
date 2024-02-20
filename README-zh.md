# OpenGPTs - 基于 Langchain 的开源 GPTs 实现

OpenGPTs 是一个基于 Langchain 的开源 GPTs 实现，它是一个开放的、可扩展的 GPTs 实现。本项目的目标是为 OpenGPTs 引入支持中文的大语言模型（包括闭源和开源的模型）。同时还探讨如何通过模型训练提升模型在 Agent 场景下的效果。

## 架构

TODO

## 快速开始

### 1. 启动后端服务（Backend）

**安装依赖**

```shell
cd backend
pip install -r requirements.txt
poetry install
```

**设置持久化层**

后端服务默认使用 Redis 作为持久化层，用来保存 Agent 配置以及聊天历史，你需要设置 `REDIS_URL` 环境变量。

```shell
export REDIS_URL="redis://localhost:6379/0"
```

**设置向量数据库**

后端服务默认使用 Redis 作为向量数据库，你可以修改为使用 LangChain 支持的 50+ 种向量数据库。

如果使用 Redis 作为向量数据库，需要启用 `redissearch` 模块，可以使用 Docker 启动 Redis。

```shell
docker run --name opengpts-redis -d -p 6379:6379 redis/redis-stack-server:latest
```

**设置大语言模型（LLM）**

配置对应模型的环境变量，如果是 OpenAI 模型：

```shell
export OPENAI_API_KEY="sk-..."
```

如果是百度千帆平台 ERNIE-Bot-4 模型：

```shell
export QIANYAN_AK="..."
export QIANYAN_SK="..."
```

**设置工具**

By default this uses a lot of tools.
Some of these require additional environment variables.
You do not need to use any of these tools, and the environment variables are not required to spin up the app
(they are only required if that tool is called).

For a full list of environment variables to enable, see the `Tools` section below.

**设置监控**

Set up [LangSmith](https://smith.langchain.com/).
This is optional, but it will help with debugging, logging, monitoring.
Sign up at the link above and then set the relevant environment variables

```shell
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY=...
```

启动后端服务：

```shell
langchain serve --port=8100
```

### 2. 启动前段服务（Frontend）

```shell
cd frontend
yarn
yarn dev
```

Navigate to [http://localhost:5173/](http://localhost:5173/) and enjoy!

## 定制化

### 定制机器人（Bot）

目前本项目支持三种 Bot：

- `ChatBot`：基于系统人设（System Persona）的聊天机器人，无法调用工具。
- `RAG`：基于 RAG 架构，可以上传文件，针对内容进行提问，无法调用工具。
- `Assistant`：助手机器人，支持RAG、工具调用等，对标 OpenAI 的 GPTs 实现。

前两种 Bot 不是本项目的重点，我们以 `Assistant` 为主要的实现。

### 定制大语言模型（LLM）

### 定制工具（Tools）
