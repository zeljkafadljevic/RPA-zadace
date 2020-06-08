class tankError(Exception):
    def __init__(self,code):
        self.error_message=''
        self.error_dict={
            000: "ERROR 000: Univerzalna greška",
            101: "ERROR 101: Unijeli ste pogrešan iznos, molimo unesite drugi"
            }
        try:
            self.error_message+=self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]