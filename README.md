# 🐱 Yuu Chat - Mistral Character Chatbot

⚠️ **This is a personal attempt. The effect was not satisfactory. Archived.** ⚠️

A self-hosted, Dockerized LLM chatbot powered by Mistral-7B (GGUF, quantized in Q4_K format) + Gradio + llama.cpp.

## ✨ Features
- Role-playing character chatbot (Yuu the cat)
- llama-cpp-python backend
- Docker + HTTPS + domain + ChatML
- Ready for future LoRA fine-tuning

## 📦 Requirements

> ❗ This project **does not include** any models, certs, or nginx configs. You must:
> - Download your own **quantized Mistral-7B (GGUF)** model file
> - Place it in `models/` directory (e.g. `models/mistral.gguf`)
> - Set up your own **nginx reverse proxy with HTTPS** (optional if not using domain)

## 🚀 Quick Start

```bash
git clone ...
cd yuu-chat-deploy
docker compose up --build -d
```

Then visit your app at: `http://your-server-ip:7860`

> For HTTPS and domain support, configure your system-level nginx separately.
