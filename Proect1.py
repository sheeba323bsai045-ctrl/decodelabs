import os
import time

def clear_screen():
    """Clear the terminal screen for better UX"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    """Display the chatbot welcome message"""
    clear_screen()
    print("=" * 50)
    print("🤖 WELCOME TO DECODELABS AI CHATBOT 🤖")
    print("💬 I'm your friendly AI assistant!")
    print("👋 Type 'hello', 'hi', or 'hey' to greet me")
    print("❌ Type 'bye', 'exit', or 'quit' to leave")
    print("💭 Try asking about me, time, or just chat!")
    print("=" * 50)
    print()

def get_response(user_input):
    """Rule-based decision making using if-elif-else logic"""
    user_input = user_input.lower().strip()
    
    # Greetings handling
    if any(greeting in user_input for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
        responses = [
            "Hello! 👋 How can I assist you today?",
            "Hi there! 😊 Great to see you!",
            "Hey! What's up? 🚀",
            "Hello! Welcome to DecodeLabs AI! 🤖"
        ]
        return responses[hash(user_input) % len(responses)]
    
    # Exit commands
    elif any(exit_cmd in user_input for exit_cmd in ['bye', 'exit', 'quit', 'goodbye', 'see you', 'farewell']):
        return None  # Signal to exit
    
    # Name inquiries
    elif any(word in user_input for word in ['name', 'who are you', 'your name']):
        return "I'm DecodeBot 🤖, your AI assistant from DecodeLabs!"
    
    # Capability questions
    elif any(word in user_input for word in ['what can you do', 'help', 'capabilities']):
        return """I can:
- Greet you warmly! 😊
- Tell you about myself 🤖
- Give you the current time ⏰
- Chat about AI and programming 💻
- Say goodbye politely 👋"""
    
    # Time requests
    elif any(word in user_input for word in ['time', 'clock']):
        current_time = time.strftime("%H:%M:%S")
        return f"It's currently {current_time} 📅"
    
    # AI/Programming questions
    elif any(word in user_input for word in ['ai', 'artificial intelligence', 'chatbot']):
        return "I'm a rule-based AI chatbot built with Python! I'm the first step in your AI journey at DecodeLabs 🚀"
    
    # Name asking
    elif 'your name' in user_input or 'name is' in user_input:
        return "You can call me whatever you like! But I'm officially DecodeBot 🤖 What's your name?"
    
    # Default responses (nested conditions for variety)
    elif '?' in user_input:
        responses = [
            "That's an interesting question! 🤔 Can you tell me more?",
            "Hmm... I'm still learning! What do you think? 💭",
            "Great question! I'm a rule-based bot, so I respond based on patterns I recognize 🎯"
        ]
        return responses[hash(user_input) % len(responses)]
    
    elif len(user_input) < 3:
        return "I heard you! 😊 Say something more and I'll respond!"
    
    else:
        responses = [
            "Cool! Tell me more about that! ✨",
            "Interesting! What else? 😄",
            "I see! Keep talking, I'm listening! 👂",
            "That's awesome! 🤩 Anything else on your mind?"
        ]
        return responses[hash(user_input) % len(responses)]

def main():
    """Main chatbot loop - continuous interaction"""
    print_welcome()
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            print("Bot: Please say something! 😊")
            continue
        
        # Get bot response
        response = get_response(user_input)
        
        if response is None:  # Exit condition
            print("\nBot: Goodbye! 👋 Thanks for chatting with DecodeLabs AI!")
            print("🤖 Have a great day! See you next time! 🚀")
            time.sleep(1)
            break
        
        print(f"Bot: {response}")
        
        # Small delay for natural conversation feel
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBot: Goodbye! 👋 Thanks for using DecodeLabs AI!")
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")