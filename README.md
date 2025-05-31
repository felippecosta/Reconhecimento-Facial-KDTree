# Reconhecimento-Facial-KDTree

Parte 1:

refatorar o código fornecido em sala para que a API de latitude e longitude com as seguintes alterações:

1- incomporar heap para que a busca retorne os N vizinhos mais próximo na árvore KD (opcional e se implementado incrementa a nota em 1 ponto)

2- alterar a estrutura de dados para que ela comporte um vetor de 128 floats  e uma string de 100 caracteres para representar respectivamente o embedding de face e o id da pessoa

Parte 2:

Com a API funcionando  e com auxílio do código   

https://colab.research.google.com/drive/1Xq-H-Agj6o1paiA6SAKSeoDeX3kRj739?usp=sharing
faça chamadas a API para armazenar 1000 faces, incluindo a sua e de mais duas pessoas e verifique o vizinho mais próximo é a face da pessoa conhecida (baixe as faces do https://www.kaggle.com/datasets/atulanandjha/lfwpeople)


Este projeto implementa uma API em Flask para realizar reconhecimento facial utilizando uma Árvore KD (k-d tree) para armazenar embeddings de faces.

## ✅ Funcionalidades

- Inserção de embeddings de faces (vetores de 128 floats) associados a um identificador de pessoa (string de até 100 caracteres).
- Busca dos **k** vizinhos mais próximos na árvore usando distância Euclidiana.
- Estrutura de dados eficiente para busca em espaços multidimensionais.
- Script de automação para inserir 1000 faces e testar o sistema.

## 📁 Estrutura do Projeto

- `app.py`: API Flask com rotas para adicionar e buscar faces.
- `modelos.py`: Classe `NoFace` representando cada nó na árvore.
- `utilitarios.py`: Função para cálculo de distância Euclidiana.
- `kdtree.py`: Implementação da Árvore KD com inserção e busca.
- `inserir_e_testar.py`: Script para inserir 1000 faces + 3 conhecidas e testar a busca.
- `requirements.txt`: Dependências do projeto.

## 🚀 Como executar

1. **Clonar o repositório e entrar na pasta:**

git clone <seu-repositorio>
cd <sua-pasta>


2. **Instalar as dependências:**

pip install -r requirementos.txt


3. **Executar a API:**

python app.py


4. **Em outro terminal, rodar o script de inserção e teste:**

python inserir_e_testar.py


## 📝 Como funciona

- O usuário envia uma **requisição POST** para `/faces` com o `embedding` e o `pessoa_id`.
- Para buscar os vizinhos mais próximos, faz uma **requisição POST** para `/faces/vizinhos` com o `embedding` e `k` (quantidade de vizinhos).
- A árvore KD armazena as faces de forma eficiente, e a busca retorna os vizinhos mais próximos baseando-se na menor distância Euclidiana.

## 🎯 Objetivo

- Simular um sistema de reconhecimento facial simples usando uma estrutura de dados eficiente.
- Demonstrar a aplicação prática de árvores KD na área de Machine Learning e Visão Computacional.

## 👨‍💻 Autor

Projeto para fins acadêmicos, com foco na prática de estruturas de dados e desenvolvimento de APIs.

FELIPPE ALLAN COSTA
