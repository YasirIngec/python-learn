# Bu modül 4 işlem yapar: toplama, çıkarma, çarpma, bölme

def topla(a, b):
    return a + b

def fark(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Tanımsız (sıfıra bölme)"
    return a / b