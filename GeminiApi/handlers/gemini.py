import google.generativeai as genai


class GeminiHandler:
    def __init__(self):
        self.api_key = "AIzaSyAd05wJ2mZwVazFxnXa_sbtHQ3jTcHYtpU"
        self.model_name = "gemini-pro"
        self.categorize_prompt = "Categorize the following tweet to 3 or less main categories:\n\"{}\"\nReturn as: [ 'A' , 'B', 'C']"


    def categorize(self, text: str):
        genai.configure(api_key = self.api_key)
        model = genai.GenerativeModel(model_name= self.model_name)
        prompt_parts = [
            self.categorize_prompt.format(text)
        ]
        response = model.generate_content(prompt_parts)
        return {'text': text, 'categories': eval(response.text)}