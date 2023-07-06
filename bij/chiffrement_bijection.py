import numpy as np

A = [chr(i) for i in range(ord('A'),ord('Z') + 1)]

B = [i for i in range(26)]

def custom_map(L,fun):
    return [fun(L[i]) for i in range(len(L))]

def chiffrement_bijection(alphabet = B,bijection = lambda x : x ):
    return custom_map(alphabet,bijection)

def dechiffrement_bijection(alpha_chiffre,recip):
    alpha_dechiffre = custom_map(alpha_chiffre,recip)
    return custom_map(alpha_dechiffre,np.round)

def z_to_n(k):
    if k >= 0:
        return 2*k
    else:
        return -(2*k + 1)

def n_to_z(l):
    if l % 2 == 0 :
        return l/2
    else:
        return (-l - 1)/2

def exp_coefs(a,b,c,d):
    return lambda x : (a*np.exp(b*x+c) + d)

def log_coefs(a,b,c,d):
    return lambda x : ((np.log((x - d)/a) - c)/b)

def lin_coefs(a,b):
    return lambda x : (a*x + b)

def lir_coefs(a,b):
    return lambda x: ((x -b)/a)

def pui_coefs(y,a,b,c,d):
    return lambda x : (a*pow(y,b*x+c) + d)

def log_y(y):
    return lambda x : np.log(x)/np.log(y)

def pur_coefs(y,a,b,c,d):
    return lambda x : ((log_y(y)((x - d)/a) - c)/b)

def fun_coefs(fun,a,b,c,d):
    return lambda x : (a*fun(b*x+c) + d)

def rec_coefs(rec,a,b,c,d):
    return lambda x : lir_coefs(b,c)(rec(lir_coefs(a,d)(x)))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def launch():
    C = chiffrement_bijection(B,lin_coefs(5,0))

    D = dechiffrement_bijection(C,lir_coefs(5,0))

    msg = input("Entrez le message à chiffrer : ")
    msg_cry = ""
    let_cry = 0

    for lettre in msg:
        if lettre.isalpha():
            let_cry = C[A.index(lettre.upper())]
            msg_cry+= str(let_cry) + " & "
        else:
            msg_cry += lettre + " & "

    print("Message crypté : ")
    print(msg_cry)
    print("\n")

    msg_dec = msg_cry.split(" & ")
    msg_fin = ""
    el_decr = 0
    for el in msg_dec:
        if is_number(el):
            el_decr = D[C.index(float(el))]
            msg_fin += A[int(el_decr)]
        else:
            msg_fin += el

    print("Message décrypté : ")
    print(msg_fin)
    print("\n")
