# Sentiment Analysis on Social Media

## 📌 Project Overview

This project uses Machine Learning to analyze social media posts and classify user sentiments as Positive, Negative, Neutral, or Irrelevant. The system preprocesses text data, trains a Logistic Regression model, and predicts sentiment based on user input. It helps understand public opinions and trends from social media content.

## 🚀 Features

 * Social media text sentiment analysis
 * Text preprocessing and cleaning
 * TF-IDF feature extraction
 * Logistic Regression model training
 * Sentiment classification (Positive, Negative, Neutral, Irrelevant)
 * Accuracy evaluation and performance reporting
 * Custom user input sentiment prediction
 * Sentiment distribution visualization

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Jupyter Notebook

## 📂 Dataset

Dataset Used: Twitter Training Dataset (`twitter_training.csv`)

Columns:
* ID
* Topic
* Sentiment
* Text

## 🔄 Methodology

1. Load the dataset.
2. Clean and preprocess text data.
3. Convert text into TF-IDF features.
4. Split data into training and testing sets.
5. Train a Logistic Regression model.
6. Predict sentiments.
7. Evaluate model accuracy and generate visualizations.

## 📊 Results

* Model: Logistic Regression
* Accuracy: 77.12%
* Sentiment Classes:

  * Positive
  * Negative
  * Neutral
  * Irrelevant

## 📂 Project Structure

Sentiment-Analysis-Social-Media/

├── twitter_training.csv

├── Sentiment_analysis.py

├── README.md

├── app.py

└── requirements.txt

## ▶️ How to Run

1. Install required packages:

pip install -r requirements.txt

2. Run the application:

streamlit run app.py

3. Enter text and click Analyze to view the sentiment.

## 💬 Sample Commands

Input:
I love this game
Output:
Positive

Input:
This product is terrible
Output:
Negative

## 🎯 Objectives

 * Analyze social media posts.
 * Classify sentiments as Positive, Negative, Neutral, or Irrelevant.
 * Train a Machine Learning model for sentiment prediction.
 * Evaluate model performance using accuracy metrics.

## 📈 Future Enhancements

 * Integrate real-time social media data.
 * Improve accuracy using Deep Learning models such as LSTM or BERT.
 * Add multilingual sentiment analysis.
 * Develop an interactive dashboard with advanced visualizations.
 * Deploy the application on cloud platforms for public access.

## 📜 Conclusion

The project successfully classified social media posts into sentiment categories using Machine Learning techniques. The model achieved an accuracy of 77.12%, demonstrating effective sentiment prediction on social media text data.

## 👩‍💻 Developed By

RAJAMANI S
