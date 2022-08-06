
print ("""
Final Notu Hesaplama Aracı \n

Vize1 toplam notun %30'una etki edecek.
Vize2 toplam notun %30'una etki edecek.
Final toplam notun %40'ına etki edecek.\n

""")

vize1 = int (input ("Birinci Vize Notunuz: "))
vize2 = int (input ("İkinci Vize Notunuz: "))
final = int (input ("Final Notunuz: "))
genel_not =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10


while True:
    if genel_not >= 90:
        print ("AA")
    elif genel_not >= 85:
        print ("BA")
    elif genel_not >= 80:
        print ("BB")
    elif genel_not >= 75:
        print ("CB")
    elif genel_not >= 70:
        print ("CC")
    elif genel_not >= 65:
        print ("DC")
    elif genel_not >= 60:
        print ("DD")
    elif genel_not >= 55:
        print ("FD")
    else:
        print ("FF")
    break