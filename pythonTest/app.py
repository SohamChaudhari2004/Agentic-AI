from langchain_mistralai import ChatMistralAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv

load_dotenv()

mistral_api = os.getenv("MISTRAL_API_KEY")
gemini_api = os.getenv("GEMINI_API_KEY")
client = ChatMistralAI(
    api_key= mistral_api,
    model_name='mistral-large-latest',

)
gemini_client = ChatGoogleGenerativeAI(
    api_key = gemini_api,
    model = 'gemini-2.5-pro',
)

res = gemini_client.invoke('Hello, how can I assist you today?')
print(res.content)