from abc import ABC, abstractmethod

class BeyazEsya(ABC):
    def __init__(self, marka, model, seri_no):
        self.marka = marka
        self.model = model
        self.seri_no = seri_no

    @abstractmethod
    def tur(self):
        pass

    @abstractmethod
    def ozellik(self):
        pass

    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def ara(self, marka, model, seri_no):
        pass

    @abstractmethod
    def listele(self):
        pass

class Televizyon(BeyazEsya):
    def __init__(self, marka, model, seri_no, ek_ozellik):
        super().__init__(marka, model, seri_no)
        self.ek_ozellik = ek_ozellik

    def tur(self):
        return "Televizyon"

    def ozellik(self):
        return f"{self.ek_ozellik} özellik"

    def ekle(self):
        # Televizyon ekleme işlemi
        pass

    def ara(self, marka, model, seri_no):
        # Televizyon arama işlemi
        pass

    def listele(self):
        # Televizyon listeleme işlemi
        pass

class Buzdolabi(BeyazEsya):
    def __init__(self, marka, model, seri_no, ek_ozellik):
        super().__init__(marka, model, seri_no)
        self.ek_ozellik = ek_ozellik

    def tur(self):
        return "Buzdolabı"

    def ozellik(self):
        return f"{self.ek_ozellik} özellik"

    def ekle(self):
        # Buzdolabı ekleme işlemi
        pass

    def ara(self, marka, model, seri_no):
        # Buzdolabı arama işlemi
        pass

    def listele(self):
        # Buzdolabı listeleme işlemi
        pass
