from llama_cpp import Llama

# ✅ Load your local model (Q2_K version)
llm = Llama(
    model_path="mistral-7b-instruct-v0.1.Q2_K.gguf",
    n_ctx=2048,
    n_threads=4  # Adjust if you have more CPU cores
)

print("🤖 Mistral GPT Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("🧑 You: ")

    if prompt.lower() == "exit":
        print("👋 Goodbye!")
        break

    print("🧠 Generating response...\n")

    try:
        # ✅ Instruction format required by Mistral
        full_prompt = f"[INST] {prompt.strip()} [/INST]"

        output = llm(full_prompt, max_tokens=300)
        reply = output['choices'][0]['text']
        print(f"🤖 Mistral: {reply.strip()}\n")

    except Exception as e:
        print(f"⚠️ Error: {e}")
