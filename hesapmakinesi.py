print("""**********************************
işlemler;

1.Toplama işlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4. Bölme işlemi

********************************** """)

a= int(input("Birinci Sayı: "))
b= int(input("Îkinci Sayı: "))

işlemi= input("işlem Giriniz: ")

if işlemi  == 1:
    {
        print("{} ile {} in sonucu {}'dir.".format(a,b,a+b))
    }

elif işlemi  == 2:
    {
        print("{} ile {} in sonucu {}'dir.".format(a,b,a-b))
    }

elif işlemi  == 3:
    {
        print("{} ile {} in sonucu {}'dir.".format(a,b,a * b))
    }

elif işlemi  == 4:
    {
        print("{} ile {} in sonucu {}'dir.".format(a,b,a / b))
    }

else:
            print("Hatalı işlem Girdiniz.")
        