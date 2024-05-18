class Arac:
    __bilgi_kaydetme = []

    def __init__(self, marka, model, tc):
        self.marka = marka
        self.model = model
        self.__tc = tc

    def kaydet(self):
        sec = input("Kaydetmek istiyor musunuz (e/h)")  # Use input instead of print
        if sec.lower() == "e":
            data = (self.marka, self.model, self.__tc)
            self.__bilgi_kaydetme.append(data)
            print("Kaydettim")

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, TC: {self.__tc}"

class Sedan(Arac):
    def hiz(self):
        print("Sedan aracın maksimum hızı 250km/s")

class Spor_arac(Arac):
    def hiz(self):
        print("Spor arabanın maksimum hızı 300km/s")

class Suv(Arac):
    def hiz(self):
        print("Suvun maksimum hızı 220km/s")

a1 = Sedan("HONDA", "JAZZ", "123")
a1.kaydet()
a1.hiz()
print(a1)
