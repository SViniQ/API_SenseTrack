# 🌡️ SenseTrack API

API desenvolvida em Python utilizando FastAPI para registro, análise e consulta de dados de temperatura e umidade provenientes de sensores (ex: DHT22/ESP32).

Os dados são armazenados em um banco de dados MongoDB e analisados por uma árvore de decisão para fornecer recomendações automáticas.

---

## 🚀 Funcionalidades

- **Registro de Leituras:** Recebe e armazena leituras de temperatura e umidade.
- **Consulta de Dados por Sensor:** Permite listar todas as leituras registradas para um sensor específico.
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

> **Nota:** No código atual, a string de conexão está fixa. Recomenda-se alterar para ler do ambiente.

### 4. Execute a API

```bash
uvicorn api_sensetrack:app --reload
```

Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Endpoints

### `POST /registrar/{id_sensor}`

Registra uma nova leitura de temperatura e umidade para um sensor específico.

**Exemplo de requisição:**
```
POST /registrar/sensor123
Content-Type: application/json

{
  "temperatura": 25.3,
  "umidade": 60.2
}
```

**Resposta:**
```json
{
  "status": "ok",
  "sensor": "sensor123",
  "salvo_em": "2025-05-21T14:30:00.000000"
}
```

---

### `GET /dados/{id_sensor}`

Retorna todas as leituras registradas para o sensor informado.

**Exemplo de requisição:**
```
GET /dados/sensor123
```

**Resposta:**
```json
[
  {
    "_id": "6650e2e7c7a1b2f3a4c5d6e7",
    "id_sensor": "sensor123",
    "temperatura": 25.3,
    "umidade": 60.2,
    "timestamp": "2025-05-21T14:30:00.000000"
  }
]
```

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

- **Segurança:** Nunca exponha credenciais sensíveis no código-fonte. Recomenda-se utilizar variáveis de ambiente para a string de conexão do MongoDB.

---