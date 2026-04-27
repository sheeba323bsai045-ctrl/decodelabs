def chatbot():
    print("🤖 DecodeLabs Rule-Based Chatbot")
    print("=================================")
    print("Say 'hello' to greet | 'bye' to exit")
    print("=================================\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ['hello', 'hi', 'hey', 'greetings']:
            print("Bot: Hello! Welcome to DecodeLabs! 👋")
        
        elif user_input in ['bye', 'exit', 'quit', 'goodbye']:
            print("Bot: Goodbye! Thanks for chatting! 👋")
            break
        
        elif 'name' in user_input:
            print("Bot: I'm DecodeBot, your AI assistant! 🤖")
        
        elif 'help' in user_input:
            print("Bot: I can greet you, tell my name, or say goodbye!")
        
        else:
            print("Bot: I understand greetings and goodbyes! Try 'hello' or 'bye'")
        
        print()

# Run chatbot
chatbot()