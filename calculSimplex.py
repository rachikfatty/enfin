from remplirMatriceA import remplirMatriceA
from scipy.optimize import linprog
def calculSimplex(m,n,c,b_ub,b_eq):
    B = remplirMatriceA(m,n)
    c_simp = c
    b_ub_simp = b_ub.copy()
    A_ub = np.zeros((m,m*n))
    for i in range(m):
        for j in range(m*n):
            A_ub[i][j]=B[i][j]


    b_eq_simp = b_eq.copy()

    A_eq = np.zeros((n,m*n))
    for i in range(n):
        for j in range(m*n):
            x=B[i+2][j]
            A_eq[i][j]=x
            
    method='Simplex'

    res = linprog(c=c_simp, A_ub=A_ub, b_ub=b_ub_simp,A_eq=A_eq,b_eq=b_eq_simp, bounds=(0,None), method=method)
    print(res)



