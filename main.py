import google.generativeai as genai

print("Alex IA iniciando...")

# Aqui depois vamos colocar a chave do Gemini
genai.configure(api_key="SUA_CHAVE_AQUI")

modelo = genai.GenerativeModel("gemini-1.5-flash")

resposta = modelo.generate_content("Olá Gemini, eu sou a Alex IA")

print(resposta.text)
