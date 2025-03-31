import g4f

provider = g4f.Provider.HuggingChat
model = g4f.models.gpt_3_5_turbo

tasks = {
    "Task 1": "Create three unique prompts for a chatbot designed to assist startup founders with fundraising strategies.",
    "Task 2": "Improve this prompt to make it more specific and result-oriented: 'Tell me about digital marketing.'",
    "Task 3": "Draft a short welcome message for our 'Startup GPT' chatbot that's launching on a website. It should set a helpful tone and encourage user engagement.",
}

responses = {}

for task_title, task_prompt in tasks.items():
    print(f"\n📌 {task_title}:\nPrompt: {task_prompt}\n")
    try:
        response = g4f.ChatCompletion.create(
            model=model,
            provider=provider,
            messages=[{"role": "user", "content": task_prompt}],
        )
        responses[task_title] = response
        print(f"✅ Response:\n{response}\n{'-'*60}")
    except Exception as e:
        responses[task_title] = f"❌ Failed: {e}"
        print(f"❌ Failed with error: {e}")

# Save results
with open("internship_prompts_output.txt", "w", encoding="utf-8") as f:
    for title, reply in responses.items():
        f.write(f"{title}:\nPrompt: {tasks[title]}\nResponse:\n{reply}\n{'-'*50}\n")

print("\n🎉 All responses saved to 'internship_prompts_output.txt'")
