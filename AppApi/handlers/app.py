import requests
from models.app import InsightRequestModel

class AppHandler:
    def __init__(self):
        self.twitter_api_path = ''
        self.gemini_api_path = ''

    def get_insights(self, request: InsightRequestModel):
        twitter_params = request
        twitter_response = requests.post(url = self.twitter_api_path, data = twitter_params)
        gemini_params = twitter_response.content
        gemini_response = requests.post(url = self.gemini_api_path, data = gemini_params)
        return gemini_response