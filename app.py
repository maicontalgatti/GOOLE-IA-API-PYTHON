from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define a chave da API
API_KEY = ""

# Rota para renderizar a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.json['message']
        response = generate_response(user_message)
        return jsonify(response)
    else:
        return render_template('index.html')

def generate_response(user_message):
    # Chama a API para gerar uma resposta
    data = {
        "contents": [{
            "parts": [{
                "text": user_message
            }]
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": API_KEY
    }
    response = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent', json=data, headers=headers, params=params)
    
    if response.status_code == 200:
        try:
            # Acessa a história dentro da estrutura da resposta
            generated_response = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return generated_response
        except KeyError:
            # Imprime a resposta da API para depuração
            print(response.json())
            return "Erro: Resposta da API não está no formato esperado."
    else:
        return f"Erro na solicitação da API: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
