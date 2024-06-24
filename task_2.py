import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot, and I'm here to help you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No worries, it's okay.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "That's great to hear!",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you today?"]
    ],
    [
        r"good (morning|afternoon|evening)",
        ["Good %1! How can I assist you today?"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I'm here to assist you. How can I help?",]
    ],
    [
        r"(.*) created you?",
        ["I was created using NLP, Python, and a touch of magic!",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm based somewhere on the Internet.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["The weather in %1 is always great!", "It's quite nice in %1.", "I hear it's lovely in %1."]
    ],
    [
        r"i work in (.*)?",
        ["%1 is a wonderful place to work!",]
    ],
    [
        r"(.*) raining in (.*)",
        ["It's not raining in %2.", "Yes, it's raining in %2."]
    ],
    [
        r"how (.*) health(.*)",
        ["I don't have health issues, but I'm here to help you with yours!"]
    ],
    [
        r"(.*)(sports|game)?",
        ["I'm a big fan of football!", "I enjoy watching basketball."]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I really like Brad Pitt.", "I'm a fan of Emma Watson."]
    ],
    [
        r"what is your favorite (color|food)?",
        ["I like blue and my favorite food is bytes!",]
    ],
    [
        r"can you give me some advice?",
        ["Always believe in yourself and stay positive!", "Take one step at a time and keep moving forward."]
    ],
    [
        r"what is (.*) (capital|capital city) of (.*)?",
        ["The capital of %2 is %1."]
    ],
    
    [
        r"quit",
        ["Goodbye for now. See you soon!", "It was nice chatting with you. Bye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand what you are saying. Can you please rephrase?",]
    ],
]

# Define reflections for simple pronoun swapping
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

# Function to get the current time of day
def time_of_day():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

# Function to start the chatbot
def chatbot():
    print(f"Good {time_of_day()}! I am a chatbot created with NLTK. How can I help you today? (type 'quit' to exit)")

    # Create a Chat object with defined pairs and reflections
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function to start the chatbot when script is run
if __name__ == "__main__":
    chatbot()
