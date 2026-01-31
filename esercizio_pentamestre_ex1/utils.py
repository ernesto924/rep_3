def stampa_matrice[A : list[list]]:
for i in range (len(A)):
    for j in range (len(A[i])):
        print (A[i][j], end="\t")