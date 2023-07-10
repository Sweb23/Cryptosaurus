import numpy as np
from random import shuffle

MAGIC_NUMBER = 821


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
    
A = [chr(i) for i in range(ord('A'),ord('Z') + 1)]

B = [i for i in range(26)]

def custom_map(L,fun):
    return [fun(L[i]) for i in range(len(L))]

def suite():
    a = np.random.rand() - 1/2
    b = np.random.rand() - 1/2
    u0 = np.random.rand()*MAGIC_NUMBER - MAGIC_NUMBER/2
    la = np.random.rand()*u0
    mu = u0 - la
    delta = 0
    while delta <= 0:
        a = np.random.rand()
        b = np.random.rand()
        delta = a**2 + 4*b
    delta = np.sqrt(delta)

    return (a,b,la,mu,delta)

def crypt(indices, message):
    msg_cry = ""
    (a,b,la,mu,delta) = suite()
    r1 = (a + delta) / 2
    r2 = (a - delta) / 2
    for l in message:
        if l.isalpha():
            l = indices[A.index(l.upper())]
            l = la*r1**l + mu*r2**l
        msg_cry += str(l)
        msg_cry += " & "
    return msg_cry,a,b,mu,la

def decrypt(msg_cry,a,b,mu,la):
    nombres = msg_cry.split(" & ")
    termes_retrouves = [mu + la]
    delta = a**2 + 4*b
    delta = np.sqrt(delta)
    r1 = (a + delta) / 2
    r2 = (a - delta) / 2
    for i in range(1,27):
        termes_retrouves += [la*r1**i + mu*r2**i] 
    msg_decrypt = ""
    print(termes_retrouves)
    for n in nombres:
        if is_number(n):
            i = termes_retrouves.index(float(n))
            lettre_retrouvee = A[int(i)]
            msg_decrypt += lettre_retrouvee
        else:
            msg_decrypt += n

    return msg_decrypt