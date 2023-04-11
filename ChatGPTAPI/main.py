from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content":"whats is a token of gpt"}]
}
body_mensagem = json.dumps(body_mensagem)


requisicao = requests.post(link, headers=headers, data=body_mensagem)
# print(requisicao)
resposta = requisicao.json()
mensagem = resposta["choices"] [0]["message"]["content"]
print(mensagem)