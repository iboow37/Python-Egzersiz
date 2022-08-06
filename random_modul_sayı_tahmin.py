import random
import time

print ("""
Sayı tahmin oyunu

1 - 40 arasında sayı tahmin edin. 

""")

rastgele_sayı = random.randint(1, 40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayı):
        print ("Tahmin ediliyor...")
        time.sleep(3)
        print ("Daha yüksek bir sayı söyleyiniz.")
        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print ("Tahmin ediliyor...")
        time.sleep(3)
        print ("Daha düşük bir sayı söyleyiniz.")
        tahmin_hakkı -= 1
    else:
        print ("Tahmin ediliyor...")
        time.sleep(3)
        print ("Tebrikler Doğru Tahmin :",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print ("Tahmin Hakkınız Bitti: ",tahmin_hakkı)
        print ("Sayımız :",rastgele_sayı)
        break





