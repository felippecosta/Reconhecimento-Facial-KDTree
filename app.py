#FELIPPE ALLAN COSTA
from flask import Flask, request, jsonify
from kdtree import ArvoreKD

app = Flask(__name__)
arvore = ArvoreKD()

# Rota para adicionar uma face na árvore
@app.route('/faces', methods=['POST'])
def adicionar_face():
    dados = request.get_json()
    embedding = dados.get('embedding')
    pessoa_id = dados.get('pessoa_id')

    if not embedding or not pessoa_id:
        return jsonify({'erro': 'embedding e pessoa_id são obrigatórios'}), 400

    arvore.inserir(embedding, pessoa_id)
    return jsonify({'mensagem': 'Face adicionada com sucesso'}), 201

# Rota para buscar os vizinhos mais próximos
@app.route('/faces/vizinhos', methods=['POST'])
def buscar_vizinhos():
    dados = request.get_json()
    embedding = dados.get('embedding')
    k = dados.get('k', 1)

    if not embedding:
        return jsonify({'erro': 'embedding é obrigatório'}), 400

    vizinhos = arvore.buscar_vizinhos(embedding, k)
    return jsonify({'vizinhos': vizinhos})

if __name__ == '__main__':
    app.run(debug=True)
