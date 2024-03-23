import os
import pandas as pd
import re
import requests
from requests_oauthlib import OAuth1


CSV_FILENAME = "tweets.csv"
CSV_FOLDER = "csvs_data"
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", CSV_FOLDER, CSV_FILENAME)
TRASH_HOLD = 50

CONSUMER_KEY = "4BybQiGUW0UojkYGDZW9giUQ9"
CONSUMER_SECRET_KEY = "WwbpIts6cs4qioAf1Xn30wnnfNyKp7nEVCtOEvrwZalnu8KP4G"
ACCESS_TOKEN = "1758919085021126656-pMs4ryjqUjdUljjoh4QMgp75qT4Lsn"
ACCESS_TOKEN_SECRET = "7ZXyMN68cpTubahe5IZHZSwkTJfTbhLumosyfbP80cHPy"


# Set up the OAuth1 authentication
class Service:
    def __init__(self):
        self.df = self.init_df()
        self.auth = OAuth1(
            CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        )
        self.api_url = "https://api.twitter.com/2/tweets"

    def init_df(self):
        if not os.path.isfile(CSV_PATH):
            raise Exception(f"File {CSV_PATH} not found")

        if os.path.isfile(CSV_PATH.replace(".csv", "_cleaned.csv")):
            return pd.read_csv(
                CSV_PATH.replace(".csv", "_cleaned.csv"),
                skip_blank_lines=True,
                lineterminator="\n",
            )

        df = pd.read_csv(CSV_PATH)
        df = self.clean_data(df)
        df.to_csv("DataFetcher/tweets_cleaned.csv", index=False, lineterminator="\n")
        return df

    def fetch(self, tokens):
        tokens = [token.lower() for token in tokens]
        result = self.fetch_from_df(tokens=tokens)
        return result

    def post_tweet(self, text: str):
        payload = {"text": text}
        response = requests.post(self.api_url, auth=self.auth, json=payload)

        if response.status_code == 201:
            return "Tweet successfully posted."
        else:
            return f"Failed to post tweet: {response.status_code}"

    def fetch_from_df(self, tokens):
        matched_tweets = []
        # Start by checking if all tokens are in the tweet
        required_tokens_count = len(tokens)

        # Loop to decrease the number of required tokens until we find enough matches
        while required_tokens_count > 0 and len(matched_tweets) < TRASH_HOLD:
            matched_tweets.clear()  # Clear the list for the new iteration

            for author, text in self.df.values:
                try:
                    # Split the tweet into words
                    tweet_tokens = text.split()
                    # Check if the required number of tokens are in the tweet
                    if (
                        sum(token in tweet_tokens for token in tokens)
                        >= required_tokens_count
                    ):
                        matched_tweets.append({"author": author, "text": text})
                except Exception as e:
                    print(f"Error while processing tweet: {text}, because of {e}")

            # Check if we have enough matches
            if len(matched_tweets) >= TRASH_HOLD:
                break

            # Decrease the number of required tokens for the next iteration
            required_tokens_count -= 1

        return matched_tweets

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[["author", "content"]]
        df["content"] = df["content"].apply(self.clean_and_edit_tweet)
        df = df[df["content"].str.strip().astype(bool)]

        return df

    def clean_and_edit_tweet(self, tweet: str):
        tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)
        tweet = re.sub(r"\@\w+|\#", "", tweet, flags=re.MULTILINE)
        tweet = tweet.lower()
        tweet = tweet.replace("\n", " ")

        return tweet


# data_fetcher = DataFetcher()
# res = data_fetcher.fetch(["israel"], False)
