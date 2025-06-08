#FELIPPE ALLAN COSTA
import numpy as np

# Função para calcular a distância Euclidiana entre dois vetores
def distancia_euclidiana(v1, v2):
    return np.linalg.norm(np.array(v1) - np.array(v2))
