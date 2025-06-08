#FELIPPE ALLAN COSTA
from modelos import NoFace
from utilitarios import distancia_euclidiana
import heapq

# Classe que representa a Árvore KD
class ArvoreKD:
    def __init__(self):
        self.raiz = None
        self.k = 128  # Tamanho do vetor embedding

    # Função para inserir um novo nó na árvore
    def inserir(self, embedding, pessoa_id):
        def _inserir(no, embedding, pessoa_id, eixo):
            if no is None:
                return NoFace(embedding, pessoa_id, eixo)

            if embedding[eixo] < no.embedding[eixo]:
                no.esquerda = _inserir(no.esquerda, embedding, pessoa_id, (eixo + 1) % self.k)
            else:
                no.direita = _inserir(no.direita, embedding, pessoa_id, (eixo + 1) % self.k)

            return no

        self.raiz = _inserir(self.raiz, embedding, pessoa_id, 0)

    # Função para buscar os k vizinhos mais próximos
    def buscar_vizinhos(self, alvo_embedding, k=1):
        heap = []

        def _buscar(no):
            if no is None:
                return

            dist = distancia_euclidiana(alvo_embedding, no.embedding)
            heapq.heappush(heap, (-dist, no))

            if len(heap) > k:
                heapq.heappop(heap)

            eixo = no.eixo
            diff = alvo_embedding[eixo] - no.embedding[eixo]

            perto, longe = (no.esquerda, no.direita) if diff < 0 else (no.direita, no.esquerda)

            _buscar(perto)

            if abs(diff) < -heap[0][0] or len(heap) < k:
                _buscar(longe)

        _buscar(self.raiz)

        return [(no.pessoa_id, -dist) for dist, no in sorted(heap, reverse=True)]
