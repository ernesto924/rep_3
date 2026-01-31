def stampa_matrice(A : list[list]):
    for i in range (len(A)):
        for j in range (len(A[i])):
            print (A[i][j], end="\t")
        print()


def somma_matrice(A:list[list]):
    somma=0
    for i in range (len(A)):
        for j in range (len(A[i])):
                somma = somma + A[i][j]
    return somma

def min_matrice(A:list[list]):
    min=A[0][0]
    for i in range (len(A)):
        for j in range (len(A[i])):
            if A[i][j]< min:
                min=A[i][j]
    return min
