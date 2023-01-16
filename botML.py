import nltk
import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the training data
training_data = [
    ("Hi, can you help me?", "Yes, what do you need help with?"),
    ("I need help finding a product", "What kind of product are you looking for?"),
    ("I'm looking for a new laptop", "What features are you looking for in a laptop?"),
    ("I need something with a fast processor and a lot of storage", "I recommend checking out laptops with i5 or i7 processors and at least 256GB of storage."),
    ("Thank you for your help", "You're welcome! Let me know if you need anything else.")
]

# Define a function to prepare the training data
def prepare_training_data(data):
    training_questions = []
    training_answers = []
    for item in data:
        training_questions.append(item[0])
        training_answers.append(item[1])
    return training_questions, training_answers

# Prepare the training data
questions, answers = prepare_training_data(training_data)

# Define a function to determine the most similar question
def most_similar_question(question):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(questions)
    query_vector = tfidf_vectorizer.transform([question])
    similarity = pairwise_distances(query_vector, tfidf_matrix, metric='cosine')
    return questions[np.argmin(similarity)]

# Define a function to get the answer to a question
def get_answer(question):
    most_similar = most_similar_question(question)
    index = questions.index(most_similar)
    return answers[index]

# Start the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    else:
        response = get_answer(user_input)
        print("Chatbot: " + response)
