
class KartaskaIgra (Exception):
    def__init__(self,code= 000):
       self.error_message = ''
       self.error_dict = {
          000: "ERROR 000: Univerzalna greška",
          101: "ERROR 101: Unijeli ste pogrešan unos, molimo vas, unesite drugi",
          102: "ERROR 102: Greška povezana s neispravnim unos broja u tekst" 
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n")