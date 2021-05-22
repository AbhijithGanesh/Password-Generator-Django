"""passphrase
def S():
    a=[]
    for i in range(33,49):
        a.append(chr(i))
    return a
def U():
    b=[]
    for i in range(65,91):
        b.append(chr(i))
    return b
def L():
    c=[]
    for i in range(97,123):
        c.append(chr(i))
    return c
def N():
    d=[]
    for i in range(48,58):
        d.append(chr(i))
    return d
"""
import random
def RanS():
    b=random.choice(S())
    return b
def RanU():
    b=random.choice(U())
    return b
def RanL():
    b=random.choice(L())
    return b
def RanN():
    b=random.choice(N())
    return b
def pA():
    a=[]
    for i in range(64):
            a.append(RanS())
            a.append(RanU())
            a.append(RanL())
            a.append(RanN())
    return a

def PasswordGenerator():
    a=pA()
    passphrase=''
    for j in range(len(a)):
        passphrase+=a[j]
    return passphrase
