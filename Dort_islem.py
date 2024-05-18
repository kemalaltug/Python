#Sınıf yapısı kullanarak girilen iki adet sayıyı çıkarma toplama çarpma bölme işlemlerini yapan
# ve bir işlem sınıfı oluşturan program
class Islem:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def toplama(self):
        return self.sayi1 + self.sayi2

    def cikarma(self):
        return self.sayi1 - self.sayi2
    
    def bölme(self):
        if self.sayi2 !=0:
            return self.sayi1 / self.sayi2
        else:
            print("sıfıra bölünemez")

        return self.sayi1 / self.sayi2
    def carpma(self):
        return self.sayi1 * self.sayi2
sayi1= float(input("Birinci Sayıyı gir:"))
sayi2= float(input("İkinci sayıyı gir:"))

islemler= Islem(sayi1,sayi2)

print("Toplama={}".format(islemler.toplama()))
print("Çıkarma={}".format(islemler.cikarma()))
print("Çarpma={}".format(islemler.carpma()))
print("Bölme={}".format(islemler.bölme()))
    

    

    









   

    

        


