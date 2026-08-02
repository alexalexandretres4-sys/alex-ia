import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=chave)

modelo = genai.GenerativeModel("gemini-1.5-flash")

resposta = modelo.generate_content("Olá Gemini, eu sou a Alex IA. Me apresente.")

print(resposta.text)
