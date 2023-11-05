import openai
import requests
import json

# - Configura o ambiente:
api_key = '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'

headers = {"Authorization": f"Bearer {api_key}","Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"

model = "gpt-3.5-turbo"

mensagem = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "O que sao APIs "}]
}

mensagem = json.dumps(mensagem)

req = requests.post(link,headers=headers,data=mensagem)

print(req.text)
resposta = req.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(resposta)