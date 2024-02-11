import google.generativeai as genai

genai.configure(api_key="AIzaSyAd05wJ2mZwVazFxnXa_sbtHQ3jTcHYtpU")

model = genai.GenerativeModel(model_name="gemini-pro")

prompt_parts = [
  "Categorize the following tweet to 3 or less main categories:\n\"Bradly Beal becomes the first player to score 50+ points in consecutive night since Kobe Bryant.\"\nReturn as: [ 'A' , 'B', 'C']",
]

response = model.generate_content(prompt_parts)
print(response.text)