# ==========================================
# Project Name : Basic ChatBot
# Internship   : CodeAlpha Python Internship
# Developed by : Pinali Lokhande
# ==========================================

print("===================================")
print(" Welcome to Pinali's ChatBot ")
print("===================================")

while True:

    user = input("You : ").strip().lower()
    if user in ["hi", "hello", "hey"]:
    
        print("Bot : Hello! How can I help you?")

    elif user == "hello":
        print("Bot : Hi! Nice to meet you.")

    elif user == "how are you?":
        print("Bot : I'm fine. Thank you!")

    elif user == "what is your name?":
        print("Bot : My name is CodeAlpha Bot.")

    elif user == "who created you?":
        print("Bot : I was created by Pinali 🥹.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot : Goodbye! Have a nice day.")
        break

    else:
        print("Bot : Sorry, I don't understand.")