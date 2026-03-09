import numpy as np

def fun_1(A:list):
    for i in range(len(A)):
        maggiore=0
        if maggiore <= A[i]:
            maggiore = A[i]
    return maggiore 

def fun_2(A:list):
    prodotto=1
    for i in range(len(A)):
        if A[i] % 2 != 0:
            prodotto *= A[i]
    return prodotto

def fun_4(A:np.ndarray):
    s_p=0
    s_d=0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i][j] % 2 == 0:
                s_p += A[i][j]
            else:
                s_d += A[i][j]
    return s_p-s_d