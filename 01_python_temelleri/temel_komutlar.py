# input() → kullanıcıdan veri alır (her zaman str olarak döner)
# int(input()) → sayısal girişler için stringi sayıya dönüştürür
# print() → ekrana veri yazdırır
# f-string → yazının içine değişken yerleştirir

isim = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))

print(f"Merhaba {isim}, {yas} yaşındasınız.")
