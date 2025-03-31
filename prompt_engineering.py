# Digital Sampark AI Internship - Interactive Chatbot App
# Author: [Your Name]

def fundraising_prompts():
    return [
        "1️⃣ What fundraising strategy should my startup use to attract angel investors in the EdTech sector?",
        "2️⃣ Can you provide key points to include in a pitch deck for attracting venture capitalists in FinTech?",
        "3️⃣ What essential tips and common pitfalls should I be aware of when crowdfunding for my mobile app?"
    ]

def digital_marketing_advice():
    return ("📢 To increase customer engagement and sales, startups should leverage techniques like SEO, content marketing, social media advertising, email marketing, and performance analytics.")

def welcome_message():
    return ("🚀 Welcome to Startup GPT! Your AI assistant for expert fundraising strategies and startup advice. How can I help your startup today?")

def show_menu():
    print("\n" + "-"*60)
    print(welcome_message())
    print("-"*60)
    print("Select an option by entering the number:")
    print("1. Get fundraising strategy prompts")
    print("2. Get digital marketing advice")
    print("3. Exit chatbot")

def chatbot():
    while True:
        show_menu()
        choice = input("\nYour choice (1-3): ").strip()

        if choice == '1':
            print("\n🎯 **Fundraising Strategy Prompts:**")
            for prompt in fundraising_prompts():
                print(prompt)
            
            input("\n(Press Enter to return to main menu...)")

        elif choice == '2':
            print("\n📈 **Digital Marketing Advice:**")
            print(digital_marketing_advice())
            
            input("\n(Press Enter to return to main menu...)")

        elif choice == '3':
            print("\n👋 **Thank you for using Startup GPT. Best of luck!**")
            break

        else:
            print("\n⚠️ Invalid selection! Please choose (1-3).")

if __name__ == "__main__":
    chatbot()
