import streamlit as st
import transformers
import torch

# Load the model and tokenizer
model = transformers.AutoModelForSequenceClassification.from_pretrained("DeeeTeeee01/twitter-xlm-roberta-base-sentiment_dee")
tokenizer = transformers.AutoTokenizer.from_pretrained("DeeeTeeee01/twitter-xlm-roberta-base-sentiment_dee")

# Define the function for sentiment analysis
@st.cache_resource
def predict_sentiment(text):
    # Load the pipeline.
    pipeline = transformers.pipeline("sentiment-analysis")

    # Predict the sentiment.
    prediction = pipeline(text)
    sentiment = prediction[0]["label"]
    score = prediction[0]["score"]

    return sentiment, score

# Setting the page configurations
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon=":smile:",
    layout="wide",
    initial_sidebar_state="auto",
)

# Add description and title
st.write("""
# Predict if your text is  Positive, Negative or Nuetral ...
Please type your text and press ENTER key to know if your text is positive, negative, or neutral sentiment!
""")


# Add image
image = st.image("https://medium.com/scrapehero/sentiment-analysis-using-svm-338d418e3ff1", width=400)

# Get user input
text = st.text_input("Type here:")

# Define the CSS style for the app
st.markdown(
"""
<style>
body {
    background-color: #f5f5f5;
}
h1 {
    color: #4e79a7;
}
</style>
""",
unsafe_allow_html=True
)

# Show sentiment output
if text:
    sentiment, score = predict_sentiment(text)
    if sentiment == "Positive":
        st.success(f"The sentiment is {sentiment} with a score of {score*100:.2f}%!")
    elif sentiment == "Negative":
        st.error(f"The sentiment is {sentiment} with a score of {score*100:.2f}%!")
    else:
        st.warning(f"The sentiment is {sentiment} with a score of {score*100:.2f}%!")