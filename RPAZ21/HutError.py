class HutError(Exception):
    def __init__(self,code):
        self.error_message = ''
        self.error_dict = {
            
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("\n Opis greške: {}".format(self.error_message))

class PrevelikBroj(Exception):
    def __init__(self):
        self.error_message=  "Kod 101: Uneseni broj je izvan zadanog raspona: Broj > 5"+'\n'
        print("Opis greke: {}" .format(self.error_message))

class BrojNula(Exception):
    def __init__(self):
        self.error_message=  "Kod 103: Uneseni broj je izvan zadanog raspona: Broj je 0" +'\n'
        print('Opis greške:{}'.format(self.error_message))

class Greska000(Exception):
    def __init__(self):
        self.error_message= "Kod 000: Nespecificirana greška u programskom kodu za klasu Hut"
        print('opis greške: {}'.format(self.error_message))

class NegativanBroj(Exception):
    def __init__(self):
        self.error_message= "Kod 102: Uneseni broj je izvan zadanog raspona: Broj nije pozitivan"
        print('Opis greke: {}'.format(self.error_message))
        
class NijeBroj(Exception):
    def __init__(self):
        self.error_message= "Kod 104: Unesena vrijednost nije broj"
        print('Opis Greške: {}'.format(self.error_message))