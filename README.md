# 🌡️ SenseTrack API

API desenvolvida em Python utilizando FastAPI para registro, análise e consulta de dados de temperatura e umidade provenientes de sensores (ex: DHT22/ESP32). 

Os dados são armazenados em um banco de dados MongoDB e analisados por uma árvore de decisão para fornecer recomendações automáticas.

---

## 🚀 Funcionalidades

- **Registro de Leituras:** Recebe e armazena leituras de temperatura e umidade.
- **Consulta de Dados:** Permite listar todas as leituras registradas.
- **Análise Inteligente:** Analisa a temperatura recebida e retorna recomendações automáticas baseadas em árvore de decisão.
- **Armazenamento Seguro:** Integração com MongoDB Atlas para persistência dos dados.

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SViniQ/esp32_climate_bridge.git
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi pymongo uvicorn
```

### 3. Configure as variáveis de ambiente

> **Importante:** Nunca exponha credenciais diretamente no código. Utilize variáveis de ambiente para a string de conexão do MongoDB.

```bash
set MONGO_URI="mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/"
```

### 4. Execute a API

```bash
uvicorn api_sensetrack:app --reload
```

Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Endpoints

### `POST /registrar`

Registra uma nova leitura de temperatura e umidade.

**Exemplo de corpo:**
```json
{
  "temperatura": 25.3,
  "umidade": 60.2
}
```

---

### `GET /dados`

Retorna todas as leituras registradas.

---

### `POST /analisar`

Recebe uma leitura e retorna uma análise automática baseada na árvore de decisão.

**Exemplo de corpo:**
```json
{
  "temperatura": 28.0,
  "umidade": 55.0
}
```

**Resposta:**
```json
{
  "temperatura": 28.0,
  "analise": "Temperatura muito alta. Recomenda-se ajustar a temperatura geral dos ares-condicionados."
}
```

---

## 🧠 Lógica de Análise

A API utiliza uma árvore de decisão binária para classificar a temperatura em faixas e fornecer recomendações automáticas para ajustes no ambiente.

---

## 📚 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

---

## 👨🏽‍💻 Autor

- Vinícius S. Queiroz - [LinkedIn](https://www.linkedin.com/in/viníciussilvaqueiroz/)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma *Issue* ou envie um *Pull Request* para sugerir melhorias.

---

## ⚠️ Avisos

- **Segurança:** Nunca exponha credenciais sensíveis no código-fonte.

---