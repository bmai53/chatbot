from bot.chatbot import ChatBot

if __name__ == '__main__':

    bot_name = "BennyBot"
    bot = ChatBot()
    print(f"{bot_name}: Hi how are you! Type 'quit' to exit.")
    while True:
        sentence = input("You: ")
        if sentence == 'quit':
            break
        response = bot.chat(sentence)
        print(f"{bot_name}: {response['msg']}")
