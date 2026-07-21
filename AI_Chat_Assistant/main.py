responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi! Nice to meet you.",
    "how are you": "I am doing great!",
   "motivate me": "Believe in yourself! Every small step you take today brings you closer to your goal. Keep learning and never give up!",

    "study plan": "Here is a simple study plan: Study for 50 minutes, take a 10-minute break, revise what you learned, practice questions, and review your progress at the end of the day.",
    "thank you": "You're welcome! Happy to help you.",
    "bye": "Goodbye! Have a great day.",
    "Tell me a joke": "Why do programmers prefer dark mode?...",
    "What is Python?": "Python is a popular programming language.",
    "What is your name?, Who are you?": "Rule base AI chatbot my name is Quillbot."
}


def getResponseOfBot(userQuestion):

    # Convert user input into lowercase
    userQuestion = userQuestion.lower()

    # Check every key from dictionary
    for eachKey in responses:

        # Check whether key exists in user's question
        if eachKey in userQuestion:

            # Return corresponding answer
            return responses[eachKey]

    # Runs only when no key matches
    return "Sorry, currently I am not able to answer this question."


while True:

    userinput = input("Please ask your question: ")

    reply = getResponseOfBot(userinput)

    print("Bot response:", reply)

    if "bye" in userinput.lower():
        break