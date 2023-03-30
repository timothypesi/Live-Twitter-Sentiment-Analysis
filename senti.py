import streamlit as st
import tweepy
import pandas as pd
from transformers import pipeline

# Twitter API credentials Use your twitter credentials
consumer_key = '***************888'
consumer_secret = '**************888'
access_token = '**************888'
access_token_secret = '**************888'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the Streamlit app
def app():
    # Set app title
    st.title("Live Twitter Sentiment Analysis")

    # Define the search terms
    search_terms = st.text_input("Enter search terms separated by commas", "Economy , USA, Africa, Financial Crisis")
    search_terms = [term.strip() for term in search_terms.split(",")]

    # Set the number of tweets to fetch
    tweet_count = 50

    # Fetch tweets
    tweets = []
    for term in search_terms:
        search_results = api.search(q=term, lang="en", count=tweet_count)
        for tweet in search_results:
            tweets.append(tweet.text)

    # Perform sentiment analysis using Hugging Face pipeline
    sentiment_analysis = pipeline("sentiment-analysis")
    results = []
    for tweet in tweets:
        result = sentiment_analysis(tweet)[0]
        results.append((tweet, result['label'], result['score']))

    # Convert results to DataFrame
    df = pd.DataFrame(results, columns=["Tweet", "Sentiment", "Polarity Score"])

    # Display results
    st.write("Results:")
    st.write(df)

if __name__ == '__main__':
    app()
