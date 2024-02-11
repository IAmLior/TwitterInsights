import requests

class AppHandler:
    def __init__(self):
        self.twitter_api_path = ''
        self.gemini_api_path = ''


    def get_insights(self, tokens: list[str], is_prd: bool):
        twitter_params = {
            "tokens": tokens,
            "is_prd": is_prd
        }
        twitter_response = requests.post(url = self.twitter_api_path, data = twitter_params)
        #Here do some processing over twitter response
        gemini_params = {}
        gemini_response = requests.post(url = self.gemini_api_path, data = gemini_params)
        return gemini_response