# 🤖 Google AI API com Python (Flask)

Este projeto demonstra como consumir a **API de IA do Google** utilizando Python com uma aplicação simples em Flask.

⚠️ **Status:** Versão beta (uso para testes e aprendizado)

---

## 🚀 Visão Geral

A aplicação cria um servidor local utilizando Flask que permite integrar e testar chamadas à API de IA do Google.

Após configurar, você poderá acessar a aplicação diretamente no navegador:

👉 http://localhost:5000

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

---

## 🔑 Obter chave da API

1. Acesse o site oficial:
   👉 https://aistudio.google.com/app/

2. Gere sua chave de API

3. Configure a chave via variável de ambiente:

```powershell
$env:GOOGLE_API_KEY="sua_chave_aqui"
```

Opcional (modelo):  
```powershell
$env:GOOGLE_MODEL="gemini-1.5-flash"
```

---

## ⚙️ Instalação

Abra o terminal (recomendado em modo administrador) e instale as dependências:

```bash
pip install flask
pip install requests
```

---

## ▶️ Como rodar o projeto

1. Clone ou copie o código para sua máquina

2. Navegue até a pasta do projeto

3. Execute o servidor Flask:

```bash
python app.py
```

4. Abra o navegador e acesse:

👉 http://localhost:5000

---

## 🧠 Estrutura do Projeto (Exemplo)

```
/projeto
│── app.py
│── README.md
```

---

## ⚠️ Observações importantes

- Esta é uma versão **beta**, focada apenas em testes
- Não é recomendado para uso em produção
- Certifique-se de **não expor sua chave de API publicamente**

---

## 🛠 Possíveis melhorias

- Implementar autenticação
- Criar interface frontend mais robusta
- Adicionar tratamento de erros
- Logs e monitoramento
- Deploy em ambiente cloud (AWS, GCP, etc.)

---

## 💡 Dica

Se você pretende evoluir esse projeto, comece separando:

- Lógica da API
- Configurações
- Rotas do Flask

Isso evita dor de cabeça depois.

---

## 📄 Licença

Este projeto é livre para uso educacional.
