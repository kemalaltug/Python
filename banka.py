kadi1 = "gorkem"
sifre1 = "1234"
bakiye = 100

print("{:-<50s}".format("-"))
print("{:^50s}".format("GÖRKEM BANKASI"))
print("{:-<50s}".format("-"))

for i in range (3):

    kadi = input("Kullanici Adini Giriniz: ")
    sifre = input("Şifreyi Giriniz: ")

    if kadi == kadi1 and sifre == sifre1:
        print("Doğru")
    
    elif kadi == kadi1 or sifre != sifre1:
        
        while True:
            print("{:-<50s}".format("-"))

            secenek = input("""
                1- Para Çekme
                2- Para Yatirma
                3- Bakiye Sorgula
                X- Çikiş
                Yapacağiniz İşlemi Seçin: """)
            
            print("{:-<50s}".format("-"))


            if secenek == "1":

                print("Bakiyeniz: {}".format(bakiye))
                paracek = float(input("Çekilecek Parayi Giriniz: "))
                if paracek <= bakiye:
                    bakiye -= paracek
                    print("Yeni Bakiyeniz: {}".format(bakiye))
                    secenek1 = input("1- Ana Menü\n2- Çikiş")
                    if secenek1 == "2":
                        quit("Çikiş Yapildi")
                else:
                    print("Bakiyeniz Yetersiz")


            elif secenek == "2":

                print("Bakiyeniz: {}".format(bakiye))
                parayat = float(input("Yatirilacak Parayi Giriniz: "))
                bakiye += paracek
                print("Yeni Bakiyeniz: {}".format(bakiye))
                secenek1 = input("1- Ana Menü\n2- Çikiş")
                if secenek1 == "2":
                    quit("Çikiş Yapildi")

            
            elif secenek == "3":
                print("Bakiyeniz: {}".format(bakiye))
                secenek1 = input("1- Ana Menü\n2- Çikiş")
                if secenek1 == "2":
                    quit("Çikiş Yapildi")
                


            elif secenek.upper() == "X":
                print("Çikiş Yapildi")
                
    else:

        print("Yanlis")
        print("{} Hakkiniz Kaldi".format(2-i))

print("Bloke Oldu")