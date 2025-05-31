
# Classe para representar um nó na árvore KD
class NoFace:
    def __init__(self, embedding, pessoa_id, eixo=0):
        self.embedding = embedding  # Vetor com 128 floats
        self.pessoa_id = pessoa_id  # String com até 100 caracteres
        self.esquerda = None
        self.direita = None
        self.eixo = eixo  # Eixo usado para dividir os dados
