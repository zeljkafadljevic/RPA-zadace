from kspkerror import kspkerror

class ksp:
    def __init__(self):
        self.igrac1=None
        self.igrac2=None


    def play(self):
        self.igrac1=input('Igrač1 Unesite kamen, škare ili papir:')
        self.igrac2=input('Igrač2 Unesite kamen, škare ili papir:')

        if self.igrac1=='papir' and self.igrac2=='škare':
            print('igrac2 pobijedio')
        elif self.igrac1=='papir' and self.igrac2=='kamen':
            print('igrac1 pobijedio')
        elif self.igrac1=='papir' and self.igrac2=='papir':
            print('neriješeno')
        elif self.igrac1 =='škare' and  self.igrac2=='škare':
            print('neriješeno')
        elif self.igrac1=='škare' and  self.igrac2=='papir':
            print('igrac1 pobijedio')
        elif self.igrac1=='škare' and self.igrac2=='kamen':   
            print('igrac2 pobijedio')    
        elif self.igrac1=='kamen' and self.igrac2=='kamen':
            print('nerijšeno')
        elif self.igrac1=='kamen' and self.igrac2=='papir':
            print('igrac2 pobijedio')
        elif self.igrac1=='kamen' and self.igrac2=='škare':
            print('igrac1 pobijedio')
        else:
            raise kspkerror(101)       

if __name__ == "__main__":
    game = ksp()
    game.play()