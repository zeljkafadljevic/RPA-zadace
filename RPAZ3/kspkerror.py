class kspkerror(Exception):
    def __init__(self,code):
        self.error_message = ''
        self.error_message = '~'*50+'\n'
        self.error_dict = {
            000: 'ERROR 000-:Nespecificirana pogreška',
            101: 'ERROR-101: Greška povezana s unosom igraca1!',
            102: 'ERROR-101: Greška povezana s unosom igraca2!',
            103:'ERROR-103:Greška pri računjanju'
        }
        try:
            self.error_message += self.error_dict[code] 
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n'