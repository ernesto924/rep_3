import numpy as np


def stampa_matrice(A: list[list]):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="\t")
        print()


def somma_matrice(A: list[list]):
    somma = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            somma = somma + A[i][j]
    return somma


def min_matrice(A: list[list]):
    min = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < min:
                min = A[i][j]
    return min


def somma_elementi(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Somma due matrici"""
    C = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i][j] = A[i][j] + B[i][j]
    return C
