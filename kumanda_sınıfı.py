import random
import time


class Kumanda (): # Kumanda Ana Sınıfı \ Televizyon Durum Bilgisi!
    def __init__ (self,tv_durum ="Kapalı",tv_ses =0,kanal_listesi =["TRT","Kanal D","Show TV","ATV","DMAX","TV8","TV8,5","Star TV","Fox TV"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self): # Televizyon Açma Fonksiyonu
        if (self.tv_durum == "Açık"):
            print ("Televizyon Şuan Açık!")
        else:
            print ("Televizyon Açılıyor...")
            time.sleep(3)
            self.tv_durum = "Açık"
            print ("Televizyon Durumu :",self.tv_durum)
    def tv_kapat(self): # Televizyon Kapatma Fonksiyonu
        if (self.tv_durum == "Kapalı"):
            print ("Televizyon Şuan Kapalı!")
        else:
            print ("Televizyon Kapatılıyor...")
            time.sleep(3)
            self.tv_durum = "Kapalı"
            print ("Televizyon Durumu :",self.tv_durum)
    
    def ses_ayarları(self): # Televizyon Ses Ayarları Fonksiyonu
        while True:
            cevap = input (" Sesi Azalt: '-' \n Sesi Arttır: '+' \n Çıkış : 'q' \n\n Yapmak İstediğiniz İşlem: ")
            if (cevap == "-"):
                if (self.tv_ses !=0):
                    self.tv_ses -= 5
                    print (" Ses Seviyesi :",self.tv_ses)
                elif (self.tv_ses <=0):
                    print (" En Düşük Ses Seviyesi :",self.tv_ses)
            elif (cevap == "+"):
                if (self.tv_ses !=100):
                    self.tv_ses += 5
                    print (" Ses Seviyesi :",self.tv_ses)
                elif (self.tv_ses >=100):
                    print (" En Yüksek Ses Seviyesi :",self.tv_ses)
            else:
                print ("Ses Seviyesi Güncellendi :",self.tv_ses)
                break
    
    def kanal_ekle (self,kanal_ismi): # Televizyon'a Yeni Kanal Ekleme Fonksiyonu
        print ("Yeni Kanal Ekleniyor...")
        time.sleep(3)
        self.kanal_listesi.append(kanal_ismi)
        print ("Kanal Eklendi!")
    def kanal_silme (self,kanal_ismi): # Televizyon Kanal Listesinden Kanal Silme Fonksiyonu
        print ("Kanal Siliniyor...")
        time.sleep(3)
        self.kanal_listesi.remove(kanal_ismi)
        print ("Kanal Listeden Silindi!")
    def rastgele_kanal(self): # Televizyon Rastgele Kanal Değiştirme Fonksiyonu
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print ("Mevcut Kanal : {}".format(self.kanal))
    def __len__(self): # Kanal Listesinde Kaç Kanal Olduğunu Gösteren Fonksiyon
        return len (self.kanal_listesi)
    def __str__(self):
        return "Tv Durum : {}\nTV Ses: {}\nKanal listesi : {}\nMevcut Kanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print ("""

Televizyon Kumanda Uygulaması

1.TV Aç
2.TV Kapat
3.Ses Ayarları
4.Kanal Listesini Görüntüleme
5.Kanal Ekle
6.Kanal Silme
7.Kanal Sayısını Öğrenme
8.Rastgele Kanala Geçme
9.Televizyon Bilgileri

Çıkmak için 'q' ya basınız...


""")

while True:
    işlem = input ("Yapmak İstediğiniz İşlemi Seçin: ")
    if (işlem == "q"):
        print ("Program Sonlandırılıyor...")
        time.sleep(1)
        print ("Yine Bekleriz...\n (Coded By iboow37)")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        print ("Kanal Listeniz: ",kumanda.kanal_listesi)
    elif (işlem == "5"):
        print ("İptal Etmek İçin 'q' Giriniz...\n")
        kanal_isimleri = input("Kanal isimlerini ',' ile Ayırarak Giriniz: ")
        kanal_listesi = kanal_isimleri.split(",")
        if (kanal_isimleri == "q"):
            print ("İşlem İptal Edildi...")
        else:    
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "6"):
        print ("İptal Etmek İçin 'q' Giriniz...\n")
        kanal_isimleri = input("Silmek İstediğiniz Kanal isimlerini ',' Ayırarak ile Giriniz: ")
        kanal_listesi = kanal_isimleri.split(",")
        if (kanal_isimleri == "q"):
            print ("İşlem İptal Edildi...")
        else:    
            for silinecekler in kanal_listesi:
                kumanda.kanal_silme(silinecekler) 
    elif (işlem == "7"):
        print ("Kanal Sayısı :",len(kumanda))
    elif (işlem == "8"):
        kumanda.rastgele_kanal()
    elif (işlem == "9"):
        print (kumanda)
    else:
        print ("Geçersiz Bir İşlem Girdiniz...")
        break
