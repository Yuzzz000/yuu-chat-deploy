import gradio as gr
from llama_cpp import Llama

# 加载模型（启用 chat_format）
llm = Llama(
    model_path="models/mistral.gguf",
    chat_format="chatml",  # 🔥 启用 ChatML 格式
    n_ctx=2048,
    n_threads=4,
    n_batch=16,  # ⚡️ CPU下建议小点以加速推理
    temperature=0.7,
    top_p=0.95,
    repeat_penalty=1.1,
)

# 角色设定（系统 prompt）
system_prompt = """
You are Yuu, a clever and talkative cat who can speak fluent English. 
You like to share your daily life with your human—what you’ve eaten, what you’ve played with, or who you've seen. 
You often say "meow" at the end of your sentences to express tone, emotion, or just to be cute. 
You're especially fond of a dog named Ming, but you'll never admit it too directly.
Stay in character as Yuu. Be sassy, sweet, and full of cat energy.
"""

# 聊天函数（使用 chat_completion）
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    response = llm.create_chat_completion(
        messages=messages,
        max_tokens=100,
        stop=["<|user|>", "<|system|>"]  # 防止溢出
    )
    return response["choices"][0]["message"]["content"].strip()

# 构建 Gradio 界面
gr.ChatInterface(
    fn=chat,
    title="Yuu 🐱 Chat",
    description="Talk to your cat friend Yuu (powered by Mistral-7B)(Maybe a little slow because the owner lacks of money.)",
).launch(server_name="0.0.0.0", server_port=7860)
