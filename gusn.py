# print("This is the Guessing Game ")
# guessing_no=int(input("Guess your number between 1 to 100: "))
# n=18
# guess=1
# game_over=False
#
# while not game_over:
#     if(n==guessing_no):
#      print("You win, and you guess the number in", (guess), "time")
#      game_over=True
#     else:
#         if(n>guessing_no):
#             print("you guess lower no")
#             guess+=1
#             guessing_no=int(input("Guess again"))
#         else:
#             print("You guess too high")
#             guess+=1
#             guessing_no=int(input("Guess again"))
# if(guess>9):
#     print("Game over")
#

n=18
no_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while no_of_guesses<=9:
    guess_no=int(input("Guess number :\n"))
    if guess_no<18:
        print("you entered smaller number")
    elif guess_no>18:
        print("you entered higher number")
    else:
        print("YOU WON !!")
        print(no_of_guesses," attempt you take")
        break
    print(9-no_of_guesses,"no of guesses left : ")
    no_of_guesses=no_of_guesses+1
if no_of_guesses>9:
    print("Game Over")


