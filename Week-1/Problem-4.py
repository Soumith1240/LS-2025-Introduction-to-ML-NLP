import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

positive_reviews = [f"Good Movie but It was too boring for my parents. #{i}" for i in range(50)]
negative_reviews = [f"Terrible Movie for my parents but I like it. #{i}" for i in range(50)]

reviews = positive_reviews + negative_reviews
sentiments = ['positive'] * 50 + ['negative'] * 50

df = pd.DataFrame({
    'Reviews': reviews,
    'Sentiments': sentiments
})

print(df.head())

# Tokenize using CountVectorizer
vectorizer = CountVectorizer(max_features=500, stop_words='english')
X = vectorizer.fit_transform(df['Reviews'])  
y = df['Sentiments']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Training & Evaluating Model
model = MultinomialNB()
model.fit(X_train, y_train)

y_predict = model.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)
print(f"\nAccuracy: {accuracy:.4f}")

# predict_review_sentiment
def predict_review_sentiment(model, vectorizer, review):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)[0]
    return prediction

# Testing
sample_review = "I don't like this movie, maybe due to bad VFX and direction."
result = predict_review_sentiment(model, vectorizer, sample_review)
print(f"\nPredicted Sentiment: \"{sample_review}\" → {result}")

# Accuracy = 1. bcz Reviews are too simple, Balanced Data (50 positive, 50 negative)