import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

good_feedback = [f"I love this product, but it is not recommended for all. #{i}" for i in range(50)]
bad_feedback = [f"This product was terrible, I don't like it. #{i}" for i in range(50)]

texts = good_feedback + bad_feedback
labels = ['good'] * 50 + ['bad'] * 50

df = pd.DataFrame({
    'Text': texts,
    'Label': labels
})

print(df.head())

# Pre-Processing with TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=300, stop_words='english', lowercase=True)
X = vectorizer.fit_transform(df['Text'])
y = df['Label']

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Logistic Regression Model & Evaluating Model
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nReport:")
print(classification_report(y_test, y_pred))

# text_preprocess_vectorize
def text_preprocess_vectorize(texts, vectorizer):
    """
    Takes a list of texts and a fitted TfidfVectorizer.
    Returns the vectorized feature matrix.
    """
    return vectorizer.transform(texts)

# Testing
sample_texts = ["The product was useful", "I don't like this Product, Worst purchase ever made"]
sample_vectors = text_preprocess_vectorize(sample_texts, vectorizer)
sample_predictions = model.predict(sample_vectors)

for text, pred in zip(sample_texts, sample_predictions):
    print(f"\nReview: \"{text}\" → Prediction: {pred}")
