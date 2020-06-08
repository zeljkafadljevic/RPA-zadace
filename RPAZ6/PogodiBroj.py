# igra pogađanja broja
# igrač slučajnim odabirom uzima jedan broj između 1 i 100
# broj pokušaja je 10
import random
class PogodiBroj:
    def__init__(self):
       self.pokusaj = 0
# početni naslov igre
    def display_title_bar(self):
        print("\t*********************")
        print("\t***  Pogodi broj  ***")
        print("\t*********************")
# odabir unutar izbornika
    def get_user_choice(self):
        print("\n [1] Igraj pogađanje broja.")
        print("[x] Izlaz")
        return input ("Što želite napraviti/odabrati?")
    def start_game(self):
        while True:
            print("Vaš rezultat je {}".format(self.score))
            print("\nVaša karta je {}".format(self.card1[1]))
            while True:
                choice = input("Pogodi broj")
                if choice[0].lower() in ["v", "n"]
                break
            self.card2 = self.deck.pop(0)
            print("Sljedeća karta je {}".format(self.card2))

            if choice[0] < number:
                print("Broj je manji od mogućeg!")
                count = count + 1
            elif choice[0] > number:
                print("Broj je veći od mogućeg!")
                count = count + 1
            elif choice[0] == self.number:
                print("Pogodak!!")
                game = PogodiBroj()
                game.play()
            if count == 10:
                print("Isprobali ste sve odabire, željeni broj je {}".format(self.number))
                game = PogodiBroj()
                game.play()

            
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x'
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                def.start_game()
            elif choice == 'x':
                print("\nHvala vam na pošteno igri. Pozdrav!")
            else:
                print("Hvatanje izuzetaka")


if__name__ == "__main__":
    game = PogodiBroj()
    game.play()