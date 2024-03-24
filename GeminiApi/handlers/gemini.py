import google.generativeai as genai
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

required_keys = [
    "API_KEY",
    "MODEL_NAME",
]

for key in required_keys:
    if not os.getenv(key):
        raise EnvironmentError(f"Missing required environment variable: {key}")

API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")


class GeminiHandler:
    def __init__(self):
        self.api_key = API_KEY
        self.model_name = MODEL_NAME

        genai.configure(api_key=self.api_key)

        self.model = genai.GenerativeModel(model_name=self.model_name)

        self.categorize_list_prompt = """
        Given an array of tweets, each tweet will look like: {"author": "tweet's author username", "text": "the tweet text"}.
        For each tweet, categorize it to 3 main categories that are most relevant for this tweet. Return an array of 3-topics arrays using the following format:
        [
            ["topic", "topic", "topic"],
	        ["topic", "topic", "topic"],
	        ["topic", "topic", "topic"]
        ].
        Tweets array:
        
        """

    async def generate_content(self, tweets: list[dict]):
        tasks = []

        async def generate_task(data: list[dict]):
            try:
                prompt_parts = [f"{self.categorize_list_prompt}{data}"]
                response = self.model.generate_content(prompt_parts)
                response = eval(response.text)
            except Exception as e:
                print(e)

            return response

        index = 0
        while index < len(tweets):
            task = asyncio.create_task(generate_task(tweets[index : index + 10]))
            tasks.append(task)
            index += 10

        generated_content = await asyncio.gather(*tasks)
        return generated_content

    async def categorize(self, tweets: list[dict]):
        try:
            generated_content = await self.generate_content(tweets)
            response = []
            for content in generated_content:
                response.extend(content)

            return response

        except Exception as ex:
            print(f"Error while categorizing tweets: {ex}")
            raise Exception(f"Error while categorizing tweets {ex}")
