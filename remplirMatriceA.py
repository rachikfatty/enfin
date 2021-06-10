import numpy as np


def remplirMatriceA(m,n):
    b=0
    A = np.zeros((n+m,n*m))
    for i in range(m):
        k=1
        for j in range(b,n*m):
            if(k<=n):
                A[i][j]=1
                k += 1
            else:
                continue
        b += n       

    c=0    
    for i in range(m,m+n):
        for j in range(c,m*n,n):
            A[i][j]=1
        c += 1

    return A    
