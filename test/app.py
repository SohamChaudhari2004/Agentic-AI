from PIL import Image
from io import BytesIO
import google.generativeai as genai
from google.generativeai import types
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(
    api_key=os.getenv("GENAI_API_KEY")
)




