"""
Sentiment Analysis 
Muhammad Adisatriyo Pratama - November 2020

Predict sentiment from reviews 

"""

# import library
import pickle
import numpy as py
import re
import os

model_path = 'd:/VSCODE/Machine-Learning-in-Python/[Project 2] Basic NLP with Sklearn Classification/models/sentiment_classifier.pkl'

# open model file
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# sentiment_predict function to predict from reviews


def sentiment_predict(text):
    cleaned_text = re.sub('[^a-zA-Z]', ' ', text)
    cleaned_text = cleaned_text.lower()

    sentiment = model.predict([cleaned_text])

    return sentiment

n = True

while (n == True):
    print('================ SENTIMENT PREDICTION ===============')
    print('=====================================================')
    review = input('Enter some reviews : ')
    predict = sentiment_predict(review)
    if predict == ['Positive']:
        print('This is a positive sentiment')
    else:
        print('This is a negative sentiment')

    cont = input('Another reviews?[y/n] : ')
    print(cont)
    if (cont == 'n') or (cont == 'N'):
        n = True
    else:
        continue

print('========== END ==========')