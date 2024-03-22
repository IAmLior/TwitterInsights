import requests
import os

class AppHandler:
    def __init__(self):
        self.twitter_api_path = "http://localhost:8001/"
        self.gemini_api_path = "http://localhost:8000/"    
        # self.twitter_api_path = os.environ['TWITTER-API-PATH']
        # self.gemini_api_path = os.environ['GEMINI-API-PATH']

    def get_insights(self, request: list[str]):
        twitter_params = request
        twitter_response = requests.get(url = self.twitter_api_path + 'get_data/', data = twitter_params)
        gemini_params = twitter_response.content
        gemini_response = requests.post(url = self.gemini_api_path, data = gemini_params)
        return gemini_response