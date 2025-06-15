# Mantıksal operatörler, birden fazla koşulu birlikte değerlendirir:
# - and → her iki koşul da doğruysa True
# - or  → herhangi biri doğruysa True
# - not → koşulun tersini alır

a = 5
b = 10

# and: Her ikisi de doğruysa sonuç True
print(a > 3 and b < 20)   # True and True → True

# or: Herhangi biri doğruysa sonuç True
print(a < 3 or b == 10)   # False or True → True

# not: Koşulu tersine çevirir
print(not a == 5)         # not True → False
