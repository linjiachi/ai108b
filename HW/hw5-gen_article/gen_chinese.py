'''
S = NP VP           -> 句子 = 名詞子句 + 動詞子句
NP = DET Adj* N PP* -> 名詞子句 = 定詞 + 名詞
VP = V NP           -> 動詞子句 = 動詞 + 名詞子句
PP = P NP           -> 副詞子句 = 副詞 + 名詞子句
'''

import random as r

role = ['我','你','他','她']
day = ['今天','明天','昨天','後天']
actor = ['咬','喝','吃','吞']
adj = ['好喝的','難喝的','貴的','便宜的']
shop = ['50嵐','迷克夏','鮮茶道','沐白','茶湯會','武厚茶']
drink = ['紅茶','綠茶','鮮奶茶','鮮奶綠','珍珠鮮奶茶','冰淇淋紅茶','芋頭牛奶','果汁']

role.append(input("請輸入名字 : "))
print(role)

def S():
    return NP() + ' ' + VP()

def NP():
    return N() + ' ' + DAY()

def VP():
    return Wish() + ' ' + V() + ' ' + Thing()

def Thing():
    return SHOP() + ' ' + DRINK()

def SHOP():
    return r.choice(shop)

def DRINK():
    return r.choice(drink)

def N():
    return r.choice(role)

def DAY():
    return r.choice(day)

def Wish():
    return r.choice(['想','不想'])

def V():
    return r.choice(actor)

print(S())