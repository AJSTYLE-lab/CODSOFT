rules = {
    "hello": "Hi there! I am Chatbot Developed by Muhammad Ahmed Javed. How can I help you?",
    "how are you": "I'm doing well, thank you. How about you?",
    "good morning": "Good morning! What can I do for you today?",
    "good night": "Good night! Sleep well.",
    "bye": "Goodbye! Have a great day.",
    "your name": "I'm Chatbot, developed by Muhammad Ahmed Javed.",
    "help": "I'm here to assist you. Please feel free to ask any questions.",
    "weather": "I'm sorry, I don't have real-time weather information. You can check a weather website for the latest updates.",
    "joke": "Sure, here's a joke: Why did the computer go to therapy? It had too many bytes of emotional baggage!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}
def GET_USER_INPUT():
    return input("User: ")
def GET_BOT_RESPONSE(user_input):
    user_input=user_input.lower()
    if user_input in rules:
        return rules[user_input]
    else:
        return rules["default"]
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = GET_USER_INPUT()
        if user_input.lower()=="exit":
            print("Chatbot: Goodbye!")
            break
        bot_response = GET_BOT_RESPONSE(user_input)
        print(f"Chatbot: {bot_response}")