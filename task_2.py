import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime
import re

# Uncomment and run this line at least once to download NLTK resources
# nltk.download('punkt')

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
        ["The capital of %3 is %1."]
    ],
    [
        r"how can i get information about any college?",
        ["For information about colleges, you can visit their official websites or contact their admissions offices directly."]
    ],
    [
        r"admission process",
        ["The admission process varies by college. It usually involves submitting an application, transcripts, test scores, and possibly an interview."]
    ],
    [
        r"which courses?|courses offered",
        ["Colleges offer a wide range of courses including arts, sciences, engineering, medicine, law, and many others. It depends on the college and its academic programs."]
    ],
    [
        r"which college is best for engineering?",
        ["Indian institute of technology(IIT), IISC(Indian Institute of science),some other college like NIT,IIIT and you can prefered to your state government collge. "]
    ],
    [
        r"where is your college located?",
        ["XYZ University is located in City, State."]
    ],
    [
        r"is this college public or private?",
        ["mostly iit is government or other new iit are private"]
    ],
    [
        r"what are the admission requirements for (.*)?",
        ["Admission requirements for %1 vary. Typically, they include transcripts, test scores, letters of recommendation, and an application fee."]
    ],
    [
        r"how do i apply to in this college?",
        ["josaa counselling"]
    ],
    [
        r"when is the application deadline?",
        ["The application deadline for XYZ University varies by program. It's best to check our website for specific deadlines."]
    ],
    [
        r"what undergraduate programs do you offer?",
        ["We offer a wide range of undergraduate programs including arts, sciences, business, engineering, and more."]
    ],
    [
        r"can you tell me about the (.*) program at your college?",
        ["The %1 program at XYZ University focuses on [brief description of program]. It prepares students for careers in [field]."]
    ],
    [
        r"are there any specialized courses or majors available?",
        ["Yes, we have specialized courses and majors in fields like data sicence, machine learning, and Artificial intelligence."]
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

# Function to remove punctuation marks from a string
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Function to split a string into individual sentences
def split_sentences(text):
    return nltk.sent_tokenize(text)

# Function to start the chatbot
def chatbot():
    print(f"Good {time_of_day()}! I am a chatbot created with NLTK. How can I help you today? (type 'quit' to exit)")

    # Create a Chat object with defined pairs and reflections
    chat = Chat(pairs, reflections)

    # Process user input
    while True:
        user_input = input("> ")
        user_input = remove_punctuation(user_input)

        # Process each sentence separately
        sentences = split_sentences(user_input)
        for sentence in sentences:
            if sentence.strip() == "quit":
                print("Goodbye for now. See you soon!")
                return
            response = chat.respond(sentence)
            print(response)

# Main function to start the chatbot when script is run
if __name__ == "__main__":
    chatbot()
