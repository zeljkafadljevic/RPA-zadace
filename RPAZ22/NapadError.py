class NapadError (Exception):
    def __init__(self):
        self.error_message='NAPAD ERROR: Unesena pogrešna vrijednost'
        print("\n Opis greške: {}".format(self.error_message))