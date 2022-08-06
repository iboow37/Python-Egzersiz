import time


print ("""
***********************************
Beden kitle endeksi hesaplama aracı \n
**NOT:Hata almamanız için boyunuzu örnekteki gibi giriniz... Örnek = 1.85 \n 
***********************************
""")

boy = float (input("Boyunuzu yazınız: "))
kilo = int (input("Kilonuzu yazınız: "))
print("  ")
beden_kitle_indexi = kilo / (boy **2 )

while True:
    if beden_kitle_indexi < 18.5 :
        print ("Hesaplama Yapılıyor...")
        print ("Hesaplama Yapılıyor...\n")
        time.sleep(1)
        print ("Kilonuz zayıf \n")
        print ("""BKİ şişmanlığın objektif ve basit bir ölçüsü olmakla birlikte tek ölçüsü değildir. Bel kalınlığı, kalça çevresi sağlık için bakılması gereken bir başka kriterdir.Vücudun kilosu kadar, o kilonun ne kadarının yağ, ne kadarının kas olduğu da önem taşımaktadır. Hesaplama sadece bilgi amaçlıdır. Konuyla ilgili daha geniş bilgi almak için bir hekime başvurunuz.""")
    elif beden_kitle_indexi  >= 18.5 and beden_kitle_indexi < 25 :
        print ("Hesaplama Yapılıyor...")
        print ("Hesaplama Yapılıyor...\n")
        time.sleep(1)
        print ("Kilonuz normal \n")
        print ("""BKİ şişmanlığın objektif ve basit bir ölçüsü olmakla birlikte tek ölçüsü değildir. Bel kalınlığı, kalça çevresi sağlık için bakılması gereken bir başka kriterdir.Vücudun kilosu kadar, o kilonun ne kadarının yağ, ne kadarının kas olduğu da önem taşımaktadır. Hesaplama sadece bilgi amaçlıdır. Konuyla ilgili daha geniş bilgi almak için bir hekime başvurunuz.""")
    elif beden_kitle_indexi >=25 and beden_kitle_indexi < 30:
        print ("Hesaplama Yapılıyor...")
        print ("Hesaplama Yapılıyor...\n")
        time.sleep(1)
        print ("Fazla kilolusunuz \n ")
        print ("""BKİ şişmanlığın objektif ve basit bir ölçüsü olmakla birlikte tek ölçüsü değildir. Bel kalınlığı, kalça çevresi sağlık için bakılması gereken bir başka kriterdir.Vücudun kilosu kadar, o kilonun ne kadarının yağ, ne kadarının kas olduğu da önem taşımaktadır. Hesaplama sadece bilgi amaçlıdır. Konuyla ilgili daha geniş bilgi almak için bir hekime başvurunuz.""")
    else:
        print ("Hesaplama Yapılıyor...")
        print ("Hesaplama Yapılıyor...\n")
        time.sleep(1)
        print ("Obez sınıfındasınız ")
        print ("""BKİ şişmanlığın objektif ve basit bir ölçüsü olmakla birlikte tek ölçüsü değildir. Bel kalınlığı, kalça çevresi sağlık için bakılması gereken bir başka kriterdir.Vücudun kilosu kadar, o kilonun ne kadarının yağ, ne kadarının kas olduğu da önem taşımaktadır. Hesaplama sadece bilgi amaçlıdır. Konuyla ilgili daha geniş bilgi almak için bir hekime başvurunuz.""")
    break
