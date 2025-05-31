
import requests
import random

API_URL = "http://127.0.0.1:5000"

# Função para gerar um vetor de 128 floats aleatórios
def gerar_embedding():
    return [random.random() for _ in range(128)]

# Função para inserir uma face na API
def inserir_face(pessoa_id, embedding):
    url = f"{API_URL}/faces"
    dados = {
        "embedding": embedding,
        "pessoa_id": pessoa_id
    }
    resposta = requests.post(url, json=dados)
    print(f"Inserindo {pessoa_id}: Status {resposta.status_code}")

# Função para buscar os k vizinhos mais próximos
def buscar_vizinhos(embedding, k=1):
    url = f"{API_URL}/faces/vizinhos"
    dados = {
        "embedding": embedding,
        "k": k
    }
    resposta = requests.post(url, json=dados)
    print(f"Busca: Status {resposta.status_code}")
    print("Vizinhos encontrados:", resposta.json())

def main():
    # Inserir 1000 pessoas fictícias
    for i in range(1, 1001):
        pessoa_id = f"pessoa_{i}"
        embedding = gerar_embedding()
        inserir_face(pessoa_id, embedding)

    # Inserir 3 pessoas conhecidas
    conhecidas = {
        "eu": gerar_embedding(),
        "amigo1": gerar_embedding(),
        "amigo2": gerar_embedding()
    }

    for pessoa_id, embedding in conhecidas.items():
        inserir_face(pessoa_id, embedding)

    # Testar a busca para uma das pessoas conhecidas
    print("\nTestando busca para 'eu':")
    buscar_vizinhos(conhecidas["eu"], k=3)

if __name__ == "__main__":
    main()
