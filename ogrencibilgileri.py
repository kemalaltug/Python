class Ogrenci:
    def __init__(self, ad, soyad, numara, ders, vize, final):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.ders = ders
        self.vize = vize
        self.final = final

    def hesapla_basari_durumu(self):
        if isinstance(self, YuksekLisans):
            return self.vize * 0.3 + self.final * 0.7 >= 70
        else:
            return self.vize * 0.4 + self.final * 0.6 >= 50

class Onlisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, program):
        super().__init__(ad, soyad, numara, ders, vize, final)
        self.program = program

class Lisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, bolum):
        super().__init__(ad, soyad, numara, ders, vize, final)
        self.bolum = bolum

class YuksekLisans(Ogrenci):
    def __init__(self, ad, soyad, numara, ders, vize, final, anabilim_dali):
        super().__init__(ad, soyad, numara, ders, vize, final)
        self.anabilim_dali = anabilim_dali

def ogrenci_bilgilerini_listeye_kaydet(ogrenci, ogrenci_listesi):
    ogrenci_listesi.append(ogrenci)

def basari_durumunu_goster(ogrenci):
    if ogrenci.hesapla_basari_durumu():
        return "Geçti"
    else:
        return "Kaldı"

def mevcut_ogrenci_bilgilerini_listele(ogrenci_listesi):
    for ogrenci in ogrenci_listesi:
        print(f"{ogrenci.ad} {ogrenci.soyad} - {basari_durumunu_goster(ogrenci)}")

# Örnek Kullanım
onlisans1 = Onlisans("Ali", "Veli", "123", "Matematik", 40, 60, "Bilgisayar Programcılığı")
lisans1 = Lisans("Ayşe", "Fatma", "456", "Fizik", 50, 70, "Fizik Mühendisliği")
yukseklisans1 = YuksekLisans("Mehmet", "Mustafa", "789", "Kimya", 30, 80, "Organik Kimya")

ogrenci_listesi = []
ogrenci_bilgilerini_listeye_kaydet(onlisans1, ogrenci_listesi)
ogrenci_bilgilerini_listeye_kaydet(lisans1, ogrenci_listesi)
ogrenci_bilgilerini_listeye_kaydet(yukseklisans1, ogrenci_listesi)

mevcut_ogrenci_bilgilerini_listele(ogrenci_listesi)