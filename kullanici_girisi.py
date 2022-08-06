
sys_kullanıcı_adı = "ibo"
sys_parola = "ibo"

kullanıcı_adı= input("Kullanıcı adı:")
parola = input("Parola:") 

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    {
        print ("parola hatalı!")
    }
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    {
        print ("Kullanıcı adı hatalı!")
    }
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    {
        print ("Hatalı kullanıcı adı ve parola girdiniz...")
    }
else:
    print ("Sisteme Başarıyla Giriş Yapıldı...")
