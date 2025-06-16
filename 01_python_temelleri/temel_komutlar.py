# Python'da temel komutlar:
# print(), input(), type(), len(), help(), dir() gibi yerleşik fonksiyonlardır.
# Bu komutlar dilin temel yapıtaşlarını oluşturur.

# 1. print() komutu: Ekrana çıktı vermek için kullanılır
print("Merhaba Dünya")
print("Ad:", "Yasir", "Yaş:", 22)

# 2. input() komutu: Kullanıcıdan veri almak için kullanılır
isim = input("Adınızı girin: ")
print("Hoş geldin", isim)

# 3. type() komutu: Bir değişkenin veri tipini gösterir
sayi = 10
print("Veri tipi:", type(sayi))  # <class 'int'>

# 4. len() komutu: Uzunluk döndürür (karakter sayısı, liste eleman sayısı vb.)
metin = "Python"
print("Metnin uzunluğu:", len(metin))

# 5. help() komutu: Belirli bir fonksiyon veya yapının yardım dökümanını gösterir
# help(print)  # Yoruma alındı çünkü çalıştırınca terminali doldurur

# 6. dir() komutu: Bir nesnenin kullanılabilir metotlarını listeler
liste = [1, 2, 3]
print("Liste metodları:", dir(liste))

# Hatalı kullanım örneği
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 100 / sayi
    print("Sonuç:", sonuc)
except ZeroDivisionError:
    print("0'a bölme hatası!")
except ValueError:
    print("Geçersiz giriş. Sayı girmeniz gerek.")

# Gerçek kullanım senaryosu
# Kullanıcıdan ad ve yaş al, yaşını 10 yıl sonra göster
ad = input("Adınız: ")
try:
    yas = int(input("Yaşınız: "))
    print(ad, "10 yıl sonra", yas + 10, "yaşında olacak.")
except ValueError:
    print("Yaş sayı olmalı.")
