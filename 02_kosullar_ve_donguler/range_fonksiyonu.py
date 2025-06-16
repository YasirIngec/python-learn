# range() fonksiyonu, sayısal döngülerde kullanılır.
# Belirli bir başlangıç, bitiş ve adım değeri ile sayı üretir.
# Genelde for döngüsü içinde kullanılır.

# Temel kullanım: 0'dan 4'e kadar
for i in range(5):
    print("Sayı:", i)  # 0,1,2,3,4

# Başlangıç ve bitiş belirleme: 3'ten 8'e kadar
for i in range(3, 9):
    print("Aralık:", i)

# Adım değeri belirleme: 0'dan 10'a kadar 2'şer artarak
for i in range(0, 11, 2):
    print("Çift sayı:", i)

# Geriye doğru sayma: 10'dan 1'e kadar
for i in range(10, 0, -1):
    print("Geri sayım:", i)

# Hatalı kullanım: Adım değeri sıfır olamaz
try:
    for i in range(0, 5, 0):
        print(i)
except ValueError as e:
    print("Hata:", e)

# Gerçek senaryo: Kullanıcının belirlediği aralıkta sayıların karesini yazdırma
try:
    baslangic = int(input("Başlangıç değeri: "))
    bitis = int(input("Bitiş değeri: "))
    for i in range(baslangic, bitis + 1):
        print(f"{i}^2 =", i**2)
except ValueError:
    print("Geçerli bir sayı giriniz.")
