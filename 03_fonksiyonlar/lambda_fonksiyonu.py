# Lambda fonksiyonları, kısa ve isimsiz fonksiyonlardır.

# Normal fonksiyon:
def karesini_al(x):
    return x * x

print(karesini_al(4))   # çıktı: 16

# Aynı işlevi lambda ile:
karesi = lambda x: x * x
print(karesi(4))        # çıktı: 16

# Birden fazla parametreyle:
topla = lambda a, b: a + b
print(topla(3, 7))      # çıktı: 10

# Listelerde lambda kullanımı (filter, map gibi)
sayilar = [1, 2, 3, 4, 5]
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(ciftler)          # çıktı: [2, 4]
