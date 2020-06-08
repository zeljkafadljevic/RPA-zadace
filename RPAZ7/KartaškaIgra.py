# kartaška igra
# igrač vs. računalo

import random 
class KartaskaIgra:
    def__init__(self):
       self.deck = [2,3,4,5,6,7,8,9,10,10,10,10,10]*4

    def display_title_bar(self):
        print("\t***********************")
        print("\t***  Kartaška igra 2  ***")
        print("\t***********************")

    def get_user_choice(self):
        print("\n[1] Igraj kartašku igru 2.")
        print("[x] Izlaz")
        return input("Što želite napraviti?")

       random.shuffle(self.deck)
       self.player_score = 0
       self.computer_score = 0
       self.player_cards = 0
       self.computer_cards = 0
       self.round = 0
  
    def start_game(self):
        while True:
            self.player_cards = self.player_cards + self.deck.pop(0) + self.deck.pop(0)
            self.computer_cards = self.computer_cards + self.deck.pop(0) + self.deck.pop(0)
            if self.player_cards > self.computer_cards:
                self.player_score = self.player_score + 1
            elif self.player_cards < self.computer_cards:
                self.computer_score = self.computer_score + 1
            self.round = self.round + 1
            if round == 1:
                if self.player_score > self.computer_score:
                    print("Pobijedio je igrač (vi)!")
                    game = Karte()
                    game.play()
                elif self.player_score < self.computer_score:
                    print("Pobijedilo je računalo!")
                    game = Karte()
                    game.play()
                else:
                    print("Igra je neriješena!")
                    game = Karte()
                    game.play()
    def play(self):
        choice = ''
        self.display_title_bar
        while choice != 'x'
        choice = self.get_user_choice()
        self.display_title_bar()
        if choice == '1':
            def.start_game()
        elif choice == 'x':
            print("\nHvala na poštenoj igri! Pozdrav!")
        else:
            print("Hvatanje izuzetaka")

if__name__ == "__main__":
   game = Karte()
   game.play()               
    


