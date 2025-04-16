# Dockerfile
FROM python:3.11-slim

# 安装系统依赖
RUN apt update && apt install -y build-essential git && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 拷贝代码文件
COPY webui/chat_mistral.py /app/chat_mistral.py
COPY models /app/models

# 安装 Python 依赖
RUN pip install --upgrade pip \
    && pip install llama-cpp-python gradio

# 启动 Gradio 服务
CMD ["python", "chat_mistral.py"]
