from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv("GOOGLE_API_KEY", "")
MODEL_NAME = os.getenv("GOOGLE_MODEL", "gemini-1.5-flash")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.json['message']
        response = generate_response(user_message)
        return jsonify(response)
    return render_template('index.html')

def list_generate_models():
    url = f"{BASE_URL}/models?key={API_KEY}"
    response = requests.get(url, timeout=20)
    if response.status_code != 200:
        return []

    models = response.json().get("models", [])
    available = []
    for model in models:
        methods = model.get("supportedGenerationMethods", [])
        if "generateContent" in methods:
            model_name = model.get("name", "")
            if model_name.startswith("models/"):
                model_name = model_name.split("/", 1)[1]
            if model_name:
                available.append(model_name)
    return available

def request_generate_content(model_name, user_message):
    url = f"{BASE_URL}/models/{model_name}:generateContent?key={API_KEY}"
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_message
                    }
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    return requests.post(url, json=data, headers=headers, timeout=30)

def generate_response(user_message):
    if not API_KEY:
        return "Erro: defina a variável de ambiente GOOGLE_API_KEY com sua chave da API."

    preferred_models = [MODEL_NAME, "gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
    available_models = list_generate_models()
    model_candidates = []
    for model in preferred_models + available_models:
        if model and model not in model_candidates:
            model_candidates.append(model)

    last_response = None
    selected_model = MODEL_NAME
    for candidate in model_candidates:
        selected_model = candidate
        response = request_generate_content(candidate, user_message)
        print(f"Tentando modelo: {candidate} -> {response.status_code}")
        if response.status_code != 404:
            last_response = response
            break
        last_response = response

    response = last_response
    if response is None:
        return "Erro: não foi possível consultar os modelos disponíveis na API."

    if response.status_code == 200:
        try:
            generated_response = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return generated_response
        except (KeyError, IndexError):
            return "Erro: Resposta da API não está no formato esperado."
    elif response.status_code == 404:
        return (
            f"Erro 404: nenhum modelo disponível respondeu no endpoint para esta chave. "
            f"Último testado: '{selected_model}'."
        )
    else:
        return f"Erro na solicitação da API: {response.status_code} - {response.text}"

if __name__ == '__main__':
    app.run(debug=True)