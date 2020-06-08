import random
from rocket import Rocket
from ship import Ship
from tankError import tankError
class Tank(Rocket):
    # tank simulira ratni tenk na polju, ali zapravo koristi sve metode rakete
    # pa ga možemo zvati simulacija rakete
    def __init__(self, x=0, y=0, route = 0):
        super().__init__(x, y)
        self.route = route
    
    def display_title_bar(self):
        # prikazujemo glavni naslov igre korisniku
        print("\t****************************")
        print("\t*** Igra - Borba tenkova/brodova ***")
        print("\t****************************")
    
    def get_user_choice(self):
        # pokazujemo korisniku meni i pitamo ga što želi napraviti te vracamo aplikaciji njegov odgovor
        print("[1] Pokreni borbu tenkova.")
        print("[2] pokreni igru brodova")
        print("[x] Izlaz.")
        
        return input("Odaberite koju igru želite igrat:")
    
    def fight(self):
        # kreiram nekoliko tenkova i raketa s pozicijama slučajnog odabira (biblioteka random)
        # tenkovi imaju random broj odrađenih/napravljenih ruta na ratnom polju
        tankNum = int(input("Unesite broj tenkova na ratnom polju:")) # upisao broj 5
        tanks = []
        rockets = []
        for x in range(0,tankNum): # for petlja se vrti od 0 do 5
            x = random.randint(0,100)
            y = random.randint(1,100)
            self.route = random.randint(0,10)
            tanks.append(Tank(x,y,self.route))
        
        for x in range(0, tankNum): # for petlja se vrti od 0 do 5
            x = random.randint(0, 100)
            y = random.randint(1,100)
            rockets.append(Rocket(x, y))
        
        # prikazivanje/ispis napravljene rute svakog tenka u listi na ratnom polju
        for index, tank in enumerate(tanks):
            print("Tenk {} je napravio {} rutu/e".format(index+1, tank.route))
        
        print("\n")
        yourTank = int(input("Od {} tenkova, vaš tenk je pod brojem:".format(tankNum)))
        
        chosenTank = tanks[yourTank-1]
        # prikazivanje/ispis udaljenosti vašeg tenka ostalih tenkova
        for index, tank in enumerate(tanks):
            distance = chosenTank.get_distance(tank)
            print("Vaš tenk je udaljen {} kilometara od tenka broj {}.".format(distance, index+1))
        
        print("\n")
        # prikazivanje/ispis udaljenosti vašeg tenka od raketa u listi raketa
        for index, rocket in enumerate(rockets):
            distance = chosenTank.get_distance(rocket)
            print("Vaš tenk je udaljen {} kilometara od rakete broj {}.".format(distance, index+1))
        
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            # na temelju korisnikova odabira izvršavamo programsku logiku naše igrice ovisno o tome
            #što je korisnik odabrao
            self.display_title_bar()
            if choice == '1':
                self.fight()
            elif choice=='2':
                Ship().fight_ship()
            elif choice == 'x':
                print("\nHvala na igri i poštenoj borbi :) . Pozdrav.")
            else:
                raise tankError(101)
    
if __name__ == "__main__":
    game = Tank()
    game.play() 