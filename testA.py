import numpy as np


m = 2
n = 3
b=0
A = np.zeros((m+n,m*n)) # matrice de m+n lignes et m*n colonnes

for i in range(m):
    k=1
    for j in range(b,m*n):
        if(k<=n):
            A[i][j]=1
            k += 1
        else :
            continue 
    b += n
c=0
for i in range(m,m+n):
    for j in range(c,m*n,n):
        A[i][j]=1
    c += 1

print(A)        

            










