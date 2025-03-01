from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-pro')

result = llm.invoke("What is the capital of India")

print(result)