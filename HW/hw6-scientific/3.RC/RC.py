from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import t
C, R = symbols('C R') # C、R 為變數
V = Function('V')
sol = dsolve(C*Derivative(V(t), t) + V(t)/R, 0, hint="best")   # V(t) 對 t 取微分，
# print('dsolve(Derivative(V(t), t)* + V/R,V(t))=', sol.doit())
print('V(t) = ', sol.doit())

'''
維基百科的解：V(t) = V0 e^{-t/(RC)}

sympy 求得的解： V(t)= Eq(V(t), C1*exp(-t/(C*R)))
令 C1 = V0 就得到相同結果。
'''