# Fonksiyon, belirli işlemleri topluca tanımlar ve tekrar kullanılmasını sağlar.

# Parametresiz fonksiyon
def selamla():
    print("Merhaba, Python!")

# Parametreli fonksiyon
def topla(a, b):
    return a + b

# Varsayılan parametreli fonksiyon
def carp(a, b=2):
    return a * b

# Fonksiyonları çağıralım
selamla()                    # çıktı: Merhaba, Python!
print(topla(5, 3))           # çıktı: 8
print(carp(4))               # çıktı: 8
print(carp(4, 5))            # çıktı: 20
