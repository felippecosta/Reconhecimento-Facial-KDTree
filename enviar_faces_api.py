#Felippe Allan Costa

import os
import requests
from deepface import DeepFace
from PIL import Image

# URL da sua API local
API_URL = "http://127.0.0.1:5000/faces"

# Caminho da pasta de imagens (baixadas do Kaggle)
LFW_PATH = "./lfw_funneled"

# Função para extrair embedding de uma imagem
def extrair_embedding(imagem_path):
    try:
        emb = DeepFace.represent(img_path=imagem_path, model_name='Facenet')
        return emb[0]['embedding']
    except Exception as e:
        print(f"Erro ao processar {imagem_path}: {e}")
        return None

# Envia embedding para a API
def enviar_embedding(embedding, pessoa_id):
    try:
        resposta = requests.post(API_URL, json={
            "embedding": embedding,
            "pessoa_id": pessoa_id
        })
        print(f"Enviando {pessoa_id}: Status {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao enviar {pessoa_id}: {e}")

# Processar 1000 imagens da pasta lfw_funneled
def processar_faces_lfw(limite=1000):
    count = 0
    for pasta in os.listdir(LFW_PATH):
        pasta_completa = os.path.join(LFW_PATH, pasta)
        if not os.path.isdir(pasta_completa):
            continue

        for imagem in os.listdir(pasta_completa):
            if not imagem.endswith('.jpg'):
                continue

            caminho_imagem = os.path.join(pasta_completa, imagem)
            embedding = extrair_embedding(caminho_imagem)
            if embedding:
                enviar_embedding(embedding, f"{pasta}_{imagem}")
                count += 1
            if count >= limite:
                return

# Inserir rosto da própria pessoa e de amigos
def inserir_conhecidos():
    conhecidos = {
        "eu": "face1.jpg",
        "amigo1": "face2.jpg",
        "amigo2": "face3.jpg"
    }
    for nome, arquivo in conhecidos.items():
        embedding = extrair_embedding(arquivo)
        if embedding:
            enviar_embedding(embedding, nome)

# Buscar vizinhos mais próximos para "eu"
def testar_busca():
    try:
        emb = extrair_embedding("face1.jpg")
        if not emb:
            return

        resposta = requests.post("http://127.0.0.1:5000/faces/vizinhos", json={
            "embedding": emb,
            "k": 3
        })
        print("Resultado da busca:")
        print(resposta.json())
    except Exception as e:
        print("Erro na busca:", e)

# Execução principal
if __name__ == "__main__":
    print("🔄 Inserindo 1000 faces do dataset...")
    processar_faces_lfw()

    print("🙋‍♂️ Inserindo suas próprias faces...")
    inserir_conhecidos()

    print("🔍 Testando vizinho mais próximo para 'eu'...")
    testar_busca()
