# import urllib.request
# from bs4 import BeautifulSoup

# Normally we would extract the reviews by scrapping a website or
# by using an api that returns the reviews.

'''
def fetch_reviews(url):
    reviews = []  # An empty list to hold the reviews
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    review_divs = soup.select('div.review')  # Replace with the appropriate HTML tags

    for review in review_divs:
        reviews.append(review.get_text())

    return reviews
'''

# But for this example the reviews will be hard coded.

def fetch_reviews():
    return [
        "I absolutely love this product. It's fantastic!",
        "This is the worst product I have ever purchased!",
        "I received the product, but I have not used it yet."
    ]


# Normally, when working with NLP in practice text preprocessing is needed.

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_reviews(reviews):
    corpus = []
    stemmer = PorterStemmer()

    for review in reviews:
        # Remove special characters
        review = re.sub(r'\W', ' ', str(review))

        # Remove single characters
        review = re.sub(r'\s+[a-zA-Z]\s+', ' ', review)

        # Remove single characters at the start
        review = re.sub(r'\^[a-zA-Z]\s+', ' ', review)

        # Substituting multiple spaces with single space
        review = re.sub(r'\s+', ' ', review, flags=re.I)

        # Removing prefixed 'b'
        review = re.sub(r'^b\s+', '', review)

        # Converting to Lowercase
        review = review.lower()

        # Lemmatization
        review = review.split()

        review = [stemmer.stem(word) for word in review]
        review = ' '.join(review)
        
        corpus.append(review)
    
    return corpus

from textblob import TextBlob

# After the text preprocessing is done, we will perform the sentiment analysis.

def perform_sentiment_analysis(reviews):
    for review in reviews:
        sentiment = TextBlob(review).sentiment.polarity
        print(review, "->", end=" ")
        if sentiment > 0:
            print("Positive")
        elif sentiment < 0:
            print("Negative")
        else:
            print("Neutral")


'''
reviews_url = "the url"
raw_reviews = fetch_reviews(reviews_url)
preprocessed_reviews = preprocess_reviews(raw_reviews)
perform_sentiment_analysis(preprocessed_reviews)
'''

# We run the functions of the program, we could also use a class.
reviews = fetch_reviews()
preprocessed_reviews = preprocess_reviews(reviews)
perform_sentiment_analysis(preprocessed_reviews)

# We are expecting the following:
# i absolut love thi product it fantast -> Positive
# thi is the worst product have ever purchas -> Negative
# i receiv the product but have not use it yet -> Neutral

# Also when doing text preprocessing there are characters that are eliminated.
# these are called stemmed words.