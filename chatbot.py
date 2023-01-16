import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a Chatbot, you can call me Bot or chatbot"]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
