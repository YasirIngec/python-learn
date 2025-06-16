# Basit dosya yazma ve okuma

# Yazma (write) – var olanı siler
with open("ornek.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Python!\n")
    dosya.write("Dosya işlemleri harika.")

# Ekleme (append)
with open("ornek.txt", "a", encoding="utf-8") as dosya:
    dosya.write("\nBu satır sonradan eklendi.")

# Okuma (read)
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosya içeriği:\n", icerik)

# Satır satır okuma (readlines)
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()
    for i, satir in enumerate(satirlar, 1):
        print(f"{i}. satır: {satir.strip()}")
