import joblib
#import streamlit as st
import streamlit as st

saved_model = joblib.load("Sentiment_Analysis_NLP/sentiment-model.pkl")

sentiment_labels = {0: "Negative", 1: "Positive"}

st.title("Sentiment Analysis")
user_input = st.text_input("Enter a sentence:")

if st.button("Predict"):
    prediction = saved_model.predict([user_input])
    st.info(f"Predicted Sentiment: {sentiment_labels[prediction[0]]}")
    

