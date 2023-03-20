from random import randint

class RPS():

    """rock paper scissors"""

    def __init__(self) -> None:
        pass

    def game_play(self, play):
        # r = 0, p = 1, s = 2
        self.play = play

        while self.play:
            self.player = input("Rock(r), Paper(p), or Scissors(s)? 'quit' to quit  ")
            self.comp = randint(0,2)
            if self.player.lower() == "quit":
                self.play = False
                print("\nThank you for playing")
            elif self.player.lower() == 'r' and self.comp == 0:
                print("Game Tied")
            elif self.player.lower() == 'p' and self.comp == 1:
                print("Game Tied")
            elif self.player.lower() == 's' and self.comp == 2:
                print("Game Tied") 
            elif self.comp == 0 and self.player.lower() == 's':
                print("You Lose")
            elif self.comp == 1 and self.player.lower() == 'r':
                print("You Lose")
            elif self.comp == 2 and self.player.lower() == 'p':
                print("You Lose")
            elif self.player.lower() == 'r' and self.comp == 2:
                print("You Win!")
            elif self.player.lower() == 'p' and self.comp == 0:
                print("You Win!")
            elif self.player.lower() == 's' and self.comp == 1:
                print("You Win!")

    def run(self):
        self.prompt = True
        while self.prompt:
            self.start = input("\nWould you like to play a game?  ")
            self.game = False
            if self.start.lower() == 'yes':
                self.game = True
                self.prompt = False
                print("\nThank you for playing")
            elif self.start.lower() == 'no':
                print("\nIt is okay I will just be alone. :(")
                self.prompt = False
            else:
                print("\nI did not understand that")

            RPS.game_play(self, self.game)

rps = RPS()
rps.run()
