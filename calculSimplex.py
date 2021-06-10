from remplirMatriceA import remplirMatriceA
from scipy.optimize import linprog

def calculSimplex(m,n,c,b_ub,b_eq):
    B = remplirMatriceA(m,n)
    c_simp = c
    b_ub_simp = b_ub
    A_ub = b_ub_simp*c_simp
    b_eq_simp = b_eq
    A_eq = b_eq_simp*c_simp
    res = linprog(c=c_simp, A_ub=A_ub, b_ub=b_ub_simp, A_eq=A_eq, b_eq=b_eq_simp, bounds=(0,None))
    return (res.x[:-1], res.fun)


