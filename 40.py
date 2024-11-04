import random

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

class RockPaperScissors:
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
        self.result = None
        self.ROCK = 1
        self.PAPER = 2
        self.SCISSORS = 3

    def play(self):
        while True:
            try:
                self.user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
                if self.user_choice not in choices:
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def get_computer_choice(self):
        self.computer_choice = random.randint(1, 3)

    def determine_winner(self):
        if self.user_choice == self.ROCK and self.computer_choice == self.SCISSORS:
            self.result = "You win!"
        elif self.user_choice == self.ROCK and self.computer_choice == self.PAPER:
            self.result = "You lose!"
        elif self.user_choice == self.PAPER and self.computer_choice == self.ROCK:
            self.result = "You win!"
        elif self.user_choice == self.PAPER and self.computer_choice == self.SCISSORS:
            self.result = "You lose!"
        elif self.user_choice == self.SCISSORS and self.computer_choice == self.PAPER:
            self.result = "You win!"
        elif self.user_choice == self.SCISSORS and self.computer_choice == self.ROCK:
            self.result = "You lose!"
        else:
            self.result = "It's a tie!"

    def print_result(self):
        print(f"You chose {choices[self.user_choice]}.")
        print(f"The computer chose {choices[self.computer_choice]}.")
        print(self.result)

    def play_game(self):
        self.play()
        self.get_computer_choice()
        self.determine_winner()
        self.print_result()


class TicTacToe:
    def __init__(self):
        self.Spaces = [' '] * 9
        self.Player = 'X'
        self.Computer = 'O'

    def draw_board(self):
        print(self.Spaces[0] + '|' + self.Spaces[1] + '|' + self.Spaces[2])
        print('-----')
        print(self.Spaces[3] + '|' + self.Spaces[4] + '|' + self.Spaces[5])
        print('-----')
        print(self.Spaces[6] + '|' + self.Spaces[7] + '|' + self.Spaces[8])

    def player_move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move >= 9 or self.Spaces[move] != ' ':
                    raise ValueError
                self.Spaces[move] = self.Player
                break
            except ValueError:
                print("Invalid move. Please try again.")

    def computer_move(self):
        while True:
            move = random.randint(0, 8)
            if self.Spaces[move] == ' ':
                self.Spaces[move] = self.Computer
                break

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if self.Spaces[combo[0]] == self.Spaces[combo[1]] == self.Spaces[combo[2]] != ' ':
                return self.Spaces[combo[0]]
        if ' ' not in self.Spaces:
            return 'Tie'
        return None

    def start_game(self):
        while True:
            self.draw_board()
            self.player_move()
            winner = self.check_winner()
            if winner:
                self.draw_board()
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"{winner} wins!")
                break
            self.computer_move()
            winner = self.check_winner()
            if winner:
                self.draw_board()
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"{winner} wins!")
                break

class Quiz:
    def __init__(self):
        self.Questions={1:"What is the capital of France?",2:"Which element has the atomic number 1?",3:"Who wrote 'Pride and Prejudice?' ",4:"What is the largest planet in our solar system?",5:"Which of the following is a prime number?",6:"In which year did World War II end?",7:"What is the hardest natural substance on Earth?",8:"Which planet is closest to the Sun?",9:"Who painted the 'Mona Lisa'?",10:"What is the powerhouse of the cell?"}
        self.Answers={1:"Paris",2:"Hydrogen",3:"Jane Austin",4:"Jupiter",5:"2",6:"1945",7:"Diamond",8:"Mercury",9:"Leonardo da Vinci",10:"Nucleus"}
        self.Options={1:["Madrid","Rome","Paris","Berlin"],2:["Oxygen","Helium","Carbon","Hydrogen"],3:["Jane Austin","Charles Dickens","George Orwell","Leo Tolstoy"],4:["Earth","Venus","Jupiter","Mars"],5:["2","5","7","9"],6:["1914","1945","1990","2000"],7:["Copper","Gold","Silver","Diamond"],8:["Saturn","Mars","Venus","Mercury"],9:["Michelangelo","Van Gogh","Picasso","Leonardo da Vinci"],10:["Nucleus","Ribosome","Mitochondria","Cytoplasm"]}
        self.marks=0
    def generate_question(self):
        self.rand=random.sample(range(1,len(self.Questions)+1), len(self.Questions))
    def qna(self):
        for i in self.rand:
            print(self.Questions[i])
            for idx,options in enumerate(self.Options[i]):
                print(f"{idx+1}. {options}")
            user_answer=int(input("Enter your answer: "))-1
            if self.Options[i][user_answer]==self.Answers[i]:
                print("Correct")
                self.marks+=1
            else:
                print(f"Wrong! The correct answer was {self.Answers[i]}.")

    def display_score(self):
        print(f"Your score is {self.marks}/{len(self.Questions)}")

    def play(self):
        self.generate_question()
        self.qna()
        self.display_score()

def main():
    while True:
        game_choice = int(input("Enter 1 for Rock-Paper-Scissors or 2 for Tic-Tac-Toe or 3 for Quiz: "))
        if game_choice == 1:
            rps_game = RockPaperScissors()
            rps_game.play_game()
        elif game_choice == 2:
            ttt_game = TicTacToe()
            ttt_game.start_game()
        elif game_choice == 3:
            quiz = Quiz()
            quiz.play()
        else:
            print("Invalid choice. Try again.")

        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            break

if __name__ == "__main__":
    main()
