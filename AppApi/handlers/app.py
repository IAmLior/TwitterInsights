import requests
import os
import json


class AppHandler:
    def __init__(self):
        self.twitter_api_path = "http://localhost:8002"
        self.gemini_api_path = "http://localhost:8001"
        # self.twitter_api_path = os.environ['TWITTER-API-PATH']
        # self.gemini_api_path = os.environ['GEMINI-API-PATH']

    def get_insights(self, request: list[str]):
        twitter_params = request
        try:
            twitter_response = requests.get(
                url=f"{self.twitter_api_path}/get_data/",
                params={"tokens": twitter_params},
            )
            if twitter_response.status_code != 200:
                raise Exception(
                    f"Error while fetching data from Twitter API: {twitter_response.content}"
                )
        except Exception as ex:
            print(f"Error while fetching data from Twitter API: {ex}")
            raise Exception("Error while fetching data from Twitter API")

        try:
            gemini_params = twitter_response.json()["result"]
            gemini_response = requests.post(
                url=f"{self.gemini_api_path}/gemini/categorize",
                data=json.dumps(gemini_params[:3]),
            )

            if gemini_response.status_code != 200:
                raise Exception(
                    f"Error while fetching data from Gemini API: {gemini_response.content}"
                )

            return gemini_response.json()

        except Exception as ex:
            print(f"Error while fetching data from Gemini API: {ex}")
            raise Exception("Error while fetching data from Gemini API")
