import random
import sys

from GameUnitError import GameUnitError
from GameUnitError import HealthMeterException
from HutError import HutError
from HutError import PrevelikBroj
from HutError import BrojNula 
from HutError import Greska000
from HutError import NegativanBroj
from HutError import NijeBroj
from Napaderror import Napaderror

def weighted_random_selection(obj1, obj2):
    """ Slucajan odabir: 
        odaberi s vjerojatnošću 0.3 ranjavananja Taliona, inače, neprijatelja 
    """

    # nacini listu 3x referencu na obj1, i 7x referenci na obj2
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)] 
    selection = random.choice(weighted_list)

    # vrati obj1 ako si odabrao id(obj1) inače obj2
    return obj1 if selection == id(obj1) else obj2
    

# formatiranje ispisa
def print_bold(msg, end='\n'):
    print("\033[1m  {} \033[0m".format(msg),end='\n')



# bazna klasa
class GameUnit:
    """Bazna klasa za stvaranje likova u igri"""
    def __init__(self, name=''):
        self.max_hp = 0 # max. udarni bodovi
        self.health_meter = 0 # zdravometar :-) 
        self.name = name      # ime jedinice
        self.neprijatelj = None  # je li jedinica neprijatelj?
        self.unit_type = None    # tip jedinice

    def info(self):
        pass

    def attack(self, neprijatelj):
        """
            Metoda za odredivanje stupnja ozljede
        """
        injured_unit = weighted_random_selection(self, neprijatelj) # odaberi GameUnit objekt ili neprijatelja
        injury = random.randint(10, 15) # kolicina ozlijede
        # azuriraj kolicinu ozlijede
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)        
        print("NAPAD! ", end='')
        # ispisi stanje zdravlja sebe i neprijatelja
        self.show_health(end='  ')
        neprijatelj.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """
        metoda za ozravljanje lika
        """
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
            # nasa iznimka
            if self.health_meter > self.max_hp:
                raise HealthMeterException()

        print_bold("Izliječen si!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Resetiranje mjeraca zdravlja"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        msg = "Zdravlje: {}: {}".format(self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)


class Knight(GameUnit):
    """ Klasa koja predstavlja Viteza, lika u igri
    """
    def __init__(self, name='Vitez Talion'):
        super().__init__(name=name) # poziv konstruktora bazne klase
        # ili ...
        # GameUnit.__init__(self,name)
        self.max_hp = 40 # definiraj max hit points
        self.health_meter = self.max_hp  # postavi zdravometar :-) 
        self.unit_type = 'prijatelj'  # status jedinice

    def info(self):
        print("Ja sam vitez!")

    def acquire_hut(self, hut):
        """Borba za kucicu
       """
        print_bold("Ulazim u kucicu broj %d..." % hut.number, end=' ')
        is_neprijatelj = (isinstance(hut.occupant, GameUnit) and
                    hut.occupant.unit_type == 'neprijatelj')
        continue_attack = 'd'
        if is_neprijatelj:
            print_bold("Neprijatelj na vidiku!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')
            while continue_attack:
                continue_attack = input(".......nastavi s napadom? (d/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break
                # napadaj dok je 'd' upisan
                elif continue_attack == 'd':
                    self.attack(hut.occupant)
                    # ukoliko zdravlje neprijatelja padne na 0 ili manje
                    if hut.occupant.health_meter <= 0:
                        print("")
                        # zauzmi kucicu
                        hut.acquire(self)
                        break
                    if self.health_meter <= 0:
                        print("")
                        break
                else: 
                    raise Napaderror()
                         
        else:
            if hut.get_occupant_type() == 'slobodna':
                print_bold("Kućica je slobodna")
            else:
                print_bold("Prijatelj na vidiku!")
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """Metoda za napustanje borbe
        """
        print_bold("BJEZANJE...")
        self.neprijatelj = None


class OrcRider(GameUnit):
    """Klasa koja predstavlja lika Orc Rider"""
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'neprijatelj'
        self.hut_number = 0

    def info(self):
        print("Grrrr..Ja sam Orc Wolf Rider.")


class Hut:
    """Klasa za kreiranje kucica"""
    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """Azuriranje okupanta u kucici"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("Kucica broj {} zauzeta".format(self.number))

    def get_occupant_type(self):
        """Vraca tekst s opisom je li je kucica zauzeta ili slobodna"""
        if self.is_acquired:
            occupant_type = 'ZAUZETA'
        elif self.occupant is None:
            occupant_type = 'slobodna'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type


class AttackOfTheOrcs:
    """Glavna klasa za igru napad orkova"""
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        """Vraca listu okupanata za sve kucice
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Ispis misije igre"""
        print_bold("Misija:")
        print("  1. Bori se s neprijateljem.")
        print("  2. Stavi sve kucice pod svoju kontrolu")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self):  # zasticena metoda
        """metoda za obradu korisnickog unosa broja kucice"""
        verifying_choice = True
        idx = 0
        print("Trenutni okupanti: {}". format(self.get_occupants()))
        while verifying_choice:
            user_choice = input("Odaberite broj kucice (1-5): ")
            # hvataj iznimku ako se ne unese broj            
            try:
                idx = int(user_choice)    
            except ValueError:
                raise NijeBroj
            
            if idx > 5:
                raise PrevelikBroj()
            if idx == 0:
                raise BrojNula()
            if idx < 0:
                raise NegativanBroj()
            # hvataj iznimku ako se unese neodgovarajuci indeks
            try:
                if self.huts[idx-1].is_acquired:
                    print("Ova kucica je vec pod vasom kontrolom. Pokusajte ponovno."
                        "<INFO: Ne možete ozdraviti u kucici koja je vec pod vasom kontrolom.>")
                else:
                    verifying_choice = False
            except IndexError:
                print('Krivi unos: ',idx)
                print('Broj mora biti u rasponu 1-5. Pokušaj ponovno!')

        return idx


    def _occupy_huts(self):
        """Metoda koja koristi random funkciju za nastambu kucica s prijatelj, neprijatelj ili 'None'"""
        for i in range(5):
            choice_lst = ['neprijatelj', 'prijatelj', None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'neprijatelj':
                name = 'neprijatelj-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'prijatelj':
                name = 'vitez-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def play(self):
        """Metoda za pokretanje igre
        """
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            try:
                idx = self._process_user_choice()
                self.player.acquire_hut(self.huts[idx-1])

                if self.player.health_meter <= 0:
                    print_bold("Izgubili ste  :(")
                    break

                if self.huts[idx-1].is_acquired:
                    acquired_hut_counter += 1
            except KeyboardInterrupt:
                print('nKorisnik je izašao iz igre.')
                # izadji iz programa
                sys.exit(1)

        if acquired_hut_counter == 5:
            print_bold("Cestitke! Pobijedili ste!!!")


if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()