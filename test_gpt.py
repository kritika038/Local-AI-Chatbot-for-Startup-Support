import g4f

provider = g4f.Provider.HuggingChat
model = g4f.models.gpt_3_5_turbo

# List of internship tasks
tasks = [
    {
        "role": "user",
        "content": "Create three unique prompts for a chatbot designed to assist startup founders with fundraising strategies.",
    },
    {
        "role": "user",
        "content": "Improve this prompt to be more specific and result-oriented: 'Tell me about digital marketing.'",
    },
    {
        "role": "user",
        "content": "Write a short welcome message for our 'Startup GPT' chatbot that's launching on a website. It should set a helpful tone and encourage user engagement.",
    },
]

try:
    print(f"\n🔄 Using provider: {provider.__name__}\n")
    for i, task in enumerate(tasks, 1):
        print(f"📌 Task {i}: {task['content']}\n")
        response = g4f.ChatCompletion.create(
            model=model,
            provider=provider,
            messages=[task],
        )
        print(f"✅ Response to Task {i}:\n{response}\n{'-' * 60}\n")

except Exception as e:
    print(f"❌ Failed with HuggingChat: {e}")
