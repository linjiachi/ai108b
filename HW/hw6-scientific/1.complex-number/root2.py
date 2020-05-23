import math
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    '''if (t < 0):
        raise Exception('沒有實根')'''
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]


print("root of 1x^2+4x+0=", root2(1,4,0))
print("root of 3x^2+6x+2=", root2(3,6,2))
print("root of 3x^2+1x+2=", root2(3,1,2))