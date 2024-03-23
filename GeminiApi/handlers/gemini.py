import google.generativeai as genai
from models.gemini import TweetData


class GeminiHandler:
    def __init__(self):
        self.api_key = "AIzaSyAd05wJ2mZwVazFxnXa_sbtHQ3jTcHYtpU"
        self.model_name = "gemini-pro"
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)
        # self.categorize_prompt = '''
        # Given a tweet looks like: {"author": "tweet's author username", "text": "the tweet text"}.
        # According to the author name and the text of the tweet, categorize the tweet to 3 or less main categories. Return a 3-topics array using the following format:
        # ["topic", "topic", "topic"]
        # Tweet:
        # {}
        # '''
        self.categorize_list_prompt = """
        Given an array of tweets, each tweet will look like: {"author": "tweet's author username", "text": "the tweet text"}.
        According to the author name and the text of each tweet, categorize each tweet to 3 main categories that are most relevant for this tweet. Return an array of 3-topics arrays using the following format:
        [
            ["topic", "topic", "topic"],
	        ["topic", "topic", "topic"],
	        ["topic", "topic", "topic"]
        ].
        Tweets array:
        
        """

    def categorize(self, tweets: list[dict]):
        prompt_parts = [f"{self.categorize_list_prompt}{tweets}"]
        print(prompt_parts)
        response = self.model.generate_content(prompt_parts)
        return eval(response.text)
