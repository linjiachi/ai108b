# 請改進 07-scientific/algebra/diffn.py ，讓 4 次以上微分的誤差縮小或幾乎消失

* 原本 step 是 0.0001，如果偏差很小，重複算時會產生一些誤差，而誤差會經過遞迴而放大
## step = 0.0001(原式)
* 執行結果：
```c
PS C:\Users\USER\Desktop\LC_AI\ai\python\08-scientific\calculus> python .\diffn.pyy
df(sin, pi/4)= 0.70710678000796
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.70710678000796
dfn(sin, 2 pi/4)= -0.7071067842367995
dfn(sin, 3 pi/4)= -0.7071010443837622
dfn(sin, 4 pi/4)= 1.1796119636642288
dfn(sin, 5 pi/4)= -693.8893903907228
dfn(sin, 6 pi/4)= -41633363.42344337
dfn(sin, 7 pi/4)= 69388939039.07228
dfn(sin, 8 pi/4)= 3729655473350135.5
dfn(sin, 9 pi/4)= -6.505213034913026e+18
```
## step = 0.00001
* 執行結果：
```c
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific\2.diffn> python .\diffn.py
df(sin, pi/4)= 0.7071067811725839
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.7071067811725839
dfn(sin, 2 pi/4)= -0.7071068730546414
dfn(sin, 3 pi/4)= -0.7216449660063516
dfn(sin, 4 pi/4)= 0.0
dfn(sin, 5 pi/4)= 138777878.07814455
dfn(sin, 6 pi/4)= 3469446951953.6133
dfn(sin, 7 pi/4)= -1.2143064331837645e+18
dfn(sin, 8 pi/4)= -5.204170427930419e+22
dfn(sin, 9 pi/4)= 1.0408340855860836e+28
```

## step = 0.001
* 執行結果：
```c
df(sin, pi/4)= 0.707106663335455
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.707106663335455
dfn(sin, 2 pi/4)= -0.7071065455110936
dfn(sin, 3 pi/4)= -0.7071064428432194
dfn(sin, 4 pi/4)= 0.7071218610654739
dfn(sin, 5 pi/4)= 0.7147060721024445
dfn(sin, 6 pi/4)= -12.14306433183765
dfn(sin, 7 pi/4)= -3469.446951953614
dfn(sin, 8 pi/4)= 9540979.11787244
```

## step = 0.01
* 執行結果：
```c
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific\2.diffn> python .\diffn.py
df(sin, pi/4)= 0.7070949961324569
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.7070949961324569
dfn(sin, 2 pi/4)= -0.7070832112751613
dfn(sin, 3 pi/4)= -0.7070714266449452
dfn(sin, 4 pi/4)= 0.7070596448610633
dfn(sin, 5 pi/4)= 0.7070481353177449
dfn(sin, 6 pi/4)= -0.7070559415733868
dfn(sin, 7 pi/4)= -0.7094151655007153
dfn(sin, 8 pi/4)= 0.8586881206085195
dfn(sin, 9 pi/4)= 21.467203015212988
```

## step = 0.1
* 執行結果：
```c
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific\2.diffn> python .\diffn.py
df(sin, pi/4)= 0.7059288589999413
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.7059288589999413
dfn(sin, 2 pi/4)= -0.7047528990356128
dfn(sin, 3 pi/4)= -0.7035788980248175
dfn(sin, 4 pi/4)= 0.7024068527043681
dfn(sin, 5 pi/4)= 0.7012367598164398
dfn(sin, 6 pi/4)= -0.7000686161131447
dfn(sin, 7 pi/4)= -0.6989024184007875
dfn(sin, 8 pi/4)= 0.6977381634791502
dfn(sin, 9 pi/4)= 0.6965758561974789
```

## step = 1
* 執行結果：
```c
PS C:\Users\USER\Desktop\LC_AI\ai108b\HW\hw6-scientific\2.diffn> python .\diffn.py
df(sin, pi/4)= 0.5950098395293859
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.5950098395293859
dfn(sin, 2 pi/4)= -0.5006835156391809
dfn(sin, 3 pi/4)= -0.42131065098198134
dfn(sin, 4 pi/4)= 0.35452068839186385
dfn(sin, 5 pi/4)= 0.298318872795875
dfn(sin, 6 pi/4)= -0.2510266756783266
dfn(sin, 7 pi/4)= -0.2112316639960939
dfn(sin, 8 pi/4)= 0.17774531632540388
dfn(sin, 9 pi/4)= 0.1495675263733286
```