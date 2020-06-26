# 請將 08-scientific/algebra/root2.py 擴展到複數上
## code
```
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
print("root of 3x^2+6x+2=", root2(3,1,2))
```
## python 的數學模組
* math : 只能處理實數
```py
import math
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific>python .\root2.py
root of 1x^2+4x+0= [0.0, -4.0]
```

* cmath : 可以處理複數 (python 的複數為j)
```py
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific>python .\root2.py
root of 1x^2+4x+0= [0j, (-4+0j)]
root of 3x^2+6x+2= [(-0.42264973081037427+0j), (-1.5773502691896255+0j)]
root of 3x^2+1x+2= [(-0.16666666666666666+0.7993052538854531j), (-0.16666666666666666-0.7993052538854531j)]
```