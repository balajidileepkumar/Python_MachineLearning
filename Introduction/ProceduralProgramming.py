def movatob(a):
    b = a+1
    return b   

def movbtoc(b):
    c = b+1
    return c

def movctod(c):
    d = c+1
    return d 

def movdtoe(d):
    e = d + 1
    return e

def movetof(e):
    f = e + 1
    return f

def movatof(a):
    x = movatob(a)
    y = movbtoc(x)
    z = movctod(y)
    i = movdtoe(z)
    j = movetof(i)
    return j

