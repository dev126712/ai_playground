import os
from dotenv import load_dotenv
from groq import Groq

# Explicitly load the .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    print("Error: GROQ_API_KEY is not set. Check your .env file.")
else:
    print(f"API Key found: {api_key[:5]}... (length: {len(api_key)})")
    client = Groq(api_key=api_key)
    models = client.models.list()
    for model in models.data:
        print(model.id)
