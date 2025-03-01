from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

res=model.invoke("What Is the 7 colours of rainbow")

print(res.content)