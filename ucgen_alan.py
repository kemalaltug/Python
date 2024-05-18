'''Bi class olusturup ucgenin alanini
 hesaplayan, kullanicdan alinan bilgileri init fonks ile 
kaydedip classin icinde ucgenin 
alanini hesaplayip ekrana  yazdiran  ve dort işleme '''
class Alan:
    def __init__(self,taban,yükseklik):
        self.taban=taban
        self.yükseklik=yükseklik
    def alan(self):
        return (self.taban*self.yükseklik)/2
taban=float(input("Taban Giriniz"))
yükseklik=float(input("Yükseklik Giriniz:"))
alann=Alan(taban,yükseklik)
print("tabanı{}olan ve yüksekliği{}olan üçgenin alanı {}dir.".format(taban,yükseklik,alann.alan()))

    



        

