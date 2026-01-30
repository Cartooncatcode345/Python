import random
attempt_list = []
def show_score():
    if len(attempt_list) <= 0:
        print("There is currently no high score, its yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempt_list)))


def start_game():
    random_number=int(random.randint(1,10))
    print("Hey There! Welcome to the game of guesses! ")
    player_name = input("Enter your name!: ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts=0
    show_score()
    while wanna_play.lower()=="yes":
        try:
            guess = input("pick a number from 1 to 10 ")
            if int(guess) <1 or int(guess)>10:
                raise ValueError("Please guess a number within the given range")
            if int(guess)==random_number:
                print("Congrats! You guessed it right!")
                attempts+1
                attempt_list.append(attempts)
                print("It too you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts=0
                show_score()
                random_number=int(random.randint(1,10))
                if  play_again.lower()=="no":
                    print("Thats cool!Have a nice day")
                    break
            elif int(guess) < random_number:
                print("its lower")
                attempts+1
            elif int(guess) > random_number:
                print("It higher")
                attempts+1
        except ValueError as  err:
            print("Oh!, that is not a valid value.Try again...")
            print("({})".format(err))
    else:
        print("That's cool,Have a nice day!")


if __name__ =='__main__':
    start_game()
