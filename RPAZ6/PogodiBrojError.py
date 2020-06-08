# zadatak 6
# hvatanje izuzetaka

class PogodiBrojError(Exception):
    def__init__(self,code):
       self.error_message = ''
       self.error_dict = {
          000: "ERROR 000: Univerzalna greška",
          101: "ERROR 101: Unijeli ste pogrešan unos, molimo vas, unesite drugi" 
          }
        try:
             self.error_message += self.error_dict[code]
        except KeyError:
                   self.error_message += self.error_dict[000]
        self.error_message += '\n'
