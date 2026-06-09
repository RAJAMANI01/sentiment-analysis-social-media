import pandas as pd
import re
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv(
    r"C:\Users\Rajamani\OneDrive\Desktop\Training projects\Sentiment-Analysis Social-Media\twitter_training.csv\twitter_training.csv",
    header=None
)
df.columns = ['ID', 'Topic', 'Sentiment', 'Text']

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

df['Text'] = df['Text'].apply(clean_text)

# Features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Text'])
y = df['Sentiment']

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Streamlit UI
st.title("Sentiment Analysis on Social Media")

user_input = st.text_area("Enter text")

if st.button("Analyze"):
    text_vector = vectorizer.transform([user_input])
    prediction = model.predict(text_vector)

    st.success(f"Predicted Sentiment: {prediction[0]}")