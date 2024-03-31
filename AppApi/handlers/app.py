import requests
import os
import json

TWITTER_API_PATH = "http://twitter-api-service:8002"
GEMINI_API_PATH = "http://gemini-api-service:8001"


class AppHandler:
    def __init__(self):
        pass

    def get_insights(self, request: list[str]):
        twitter_params = request
        try:
            twitter_response = requests.get(
                url=f"{TWITTER_API_PATH}/get_data/",
                params={"tokens": twitter_params},
            )
            if twitter_response.status_code != 200:
                raise Exception(
                    f"Error while fetching data from Twitter API: {twitter_response.content}"
                )
        except Exception as ex:
            print(f"Error while fetching data from Twitter API: {ex}")
            raise Exception("Error while fetching data from Twitter API")

        print(f"Twiiter success: {twitter_response.json()['result']}")

        try:
            gemini_params = twitter_response.json()["result"] or []
            gemini_response = requests.post(
                url=f"{GEMINI_API_PATH}/gemini/categorize",
                data=json.dumps(gemini_params[:100]),
            )

            if gemini_response.status_code != 200:
                raise Exception(
                    f"Error in response from Gemini API: {gemini_response.content}"
                )

            return gemini_response.json()

        except Exception as ex:
            print(f"Error while fetching data from Gemini API: {ex}")
            raise Exception(f"Error while fetching data from Gemini API: {ex}")

    def post_tweet(self, tweet: str):
        try:
            response = requests.post(
                url=f"{TWITTER_API_PATH}/post_tweet/",
                data=json.dumps({"text": tweet}),
            )
            if response.status_code != 200:
                raise Exception(f"Error while posting tweet: {response.content}")

            response = response.json()
            return response["result"]

        except Exception as ex:
            print(f"Error while posting tweet: {ex}")
            raise Exception("Error while posting tweet")
