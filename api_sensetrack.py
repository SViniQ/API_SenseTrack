# Importa as bibliotecas necessárias do FastAPI, Pydantic, PyMongo, BSON, typing e datetime
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List
from datetime import datetime

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Conexão com o banco de dados MongoDB usando uma string de conexão
client = MongoClient("")
db = client[""]  # Seleciona o banco de dados
colecao = db[""]  # Seleciona a coleção de sensores

# Define o modelo de dados para leitura dos sensores usando Pydantic
class Leitura(BaseModel):
    temperatura: float
    umidade: float

# Função para serializar documentos do MongoDB, convertendo o ObjectId para string
def serialize_document(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# Classe para representar um nó da árvore de decisão binária
class Node:
    def __init__(self, valor_limite, mensagem):
        self.valor_limite = valor_limite  # Valor de corte para decisão
        self.mensagem = mensagem          # Mensagem associada ao nó
        self.esquerda = None              # Filho à esquerda (valores menores)
        self.direita = None               # Filho à direita (valores maiores)

# Função recursiva para verificar a temperatura na árvore de decisão
def verificar_temperatura(raiz, temperatura):
    if raiz is None:
        return "✅ Temperatura dentro da faixa ideal."
    
    if temperatura < raiz.valor_limite:
        if raiz.esquerda is None:
            return raiz.mensagem
        return verificar_temperatura(raiz.esquerda, temperatura)
    elif temperatura > raiz.valor_limite:
        if raiz.direita is None:
            return raiz.mensagem
        return verificar_temperatura(raiz.direita, temperatura)
    else:
        return raiz.mensagem

# Construção manual da árvore de decisão para análise de temperatura
raiz = Node(23, "Temperatura ideal.")
raiz.esquerda = Node(22, "Temperatura reduzindo. Recomenda-se ajustar a temperatura geral dos ares-condicionados.")
raiz.esquerda.esquerda = Node(15, "Temperatura muito baixa. Recomenda-se ajustar a temperatura geral dos ares-condicionados.")
raiz.direita = Node(27, "Temperatura aumentando. É recomendável prestar atenção na temperatura geral.")
raiz.direita.direita = Node(29, "Temperatura muito alta. Recomenda-se ajustar a temperatura geral dos ares-condicionados.")

# Endpoint para registrar uma nova leitura de temperatura e umidade
@app.post("/registrar/{id_sensor}")
async def registrar(id_sensor: str, leitura: Leitura):
    try:
        timestamp = datetime.now().isoformat()
        dados = {
            "id_sensor": id_sensor,
            "temperatura": leitura.temperatura,
            "umidade": leitura.umidade,
            "timestamp": timestamp
        }
        colecao.insert_one(dados)
        return {"status": "ok", "sensor": id_sensor, "salvo_em": timestamp}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}

# Endpoint para listar todos os dados registrados no banco de dados
@app.get("/dados/{id_sensor}", response_model=List[dict])
async def get_dados_por_sensor(id_sensor: str):
    try:
        dados = list(colecao.find({"id_sensor": id_sensor}))
        dados_serializados = [serialize_document(doc) for doc in dados]
        return dados_serializados
    except Exception as e:
        return [{"erro": str(e)}]

# Endpoint para analisar a temperatura recebida e retornar uma mensagem baseada na árvore de decisão
@app.post("/analisar")
async def analisar(leitura: Leitura):
    mensagem = verificar_temperatura(raiz, leitura.temperatura)  # Analisa a temperatura
    return {"temperatura": leitura.temperatura, "analise": mensagem}
