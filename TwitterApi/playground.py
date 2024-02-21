import requests
from requests_oauthlib import OAuth1

# Replace the following variables with your own credentials
consumer_key = '4BybQiGUW0UojkYGDZW9giUQ9'
consumer_secret = 'WwbpIts6cs4qioAf1Xn30wnnfNyKp7nEVCtOEvrwZalnu8KP4G'
access_token = '1758919085021126656-pMs4ryjqUjdUljjoh4QMgp75qT4Lsn'
access_token_secret = '7ZXyMN68cpTubahe5IZHZSwkTJfTbhLumosyfbP80cHPy'

# Set up the OAuth1 authentication
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

url = 'https://api.twitter.com/2/tweets'

# The payload contains the text of the tweet
payload = {
    'text': 'Hapoel Holon Hole Hole!!!'  # Your tweet content
}

# Make a POST request to the Twitter API to create a new tweet
response = requests.post(url, auth=auth, json=payload)

# Check if the request was successful
if response.status_code == 201:
    print("Tweet successfully posted.")
else:
    print(f"Failed to post tweet: {response.status_code}")
    print(response.json())  # Print the error message from Twitter


    