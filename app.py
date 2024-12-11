import streamlit as st
from textblob import TextBlob

# Title and app description
st.title("Sentiment Analysis Web Application")
st.write("This app analyzes the sentiment of the text you provide. Enter your text below!")

# Input from user
user_input = st.text_area("Enter text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        # Perform sentiment analysis
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine sentiment type
        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

        # Display results
        st.subheader("Analysis Results")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity:** {polarity:.2f} (range: -1 to 1)")
        st.write(f"**Subjectivity:** {subjectivity:.2f} (range: 0 to 1)")
    else:
        st.error("Please enter some text to analyze.")
