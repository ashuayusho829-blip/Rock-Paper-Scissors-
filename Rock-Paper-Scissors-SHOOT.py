import random

# I decided to add ASCII art for each choice and add a dictionary to store them and then print them out when the user and CPU make their choices. 
rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors_art = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Angela's tutorials did use integers which helped her get the following output but I wanted to see if it is possible to get similar output using strings.
Opponent = (
"rock", 
"paper", 
"scissors" )

# ASCII art dictionary I was talking about which helped me print the following image whenever I or the CPU choose one of the three options.
art = {
"rock": rock_art,
"paper": paper_art,
"scissors": scissors_art
}
print("Wasaaaaaapp! Welcome to Rock-Paper-Scissors!, Please type in your choice: rock, paper, or scissors. Any other input will result in IRS knowing ya IP adress.")
Your_turn = input("What would you like to present: ")
print(f"You chose: {Your_turn}")
print(art[Your_turn])


CPU = random.choice(Opponent)
print(f"CPU chose: {CPU}")
print(art[CPU])
# The CPU will randomly choose one of the three options and then the program will compare the user's choice with the CPU's choice and determine the winner.
if CPU == "rock" and Your_turn == "scissors":
    print("You lose! ")
elif CPU  == Your_turn:
    print("It's a Draw! ")
elif CPU == "rock" and Your_turn == "paper":
    print("You Win")
elif CPU == "paper" and Your_turn == "scissors":
    print("You Win")
elif CPU == "paper" and Your_turn == "rock":
   print("You lose! ")
elif CPU == "scissors" and Your_turn == "rock":
    print("You Win")
elif CPU == "scissors" and Your_turn == "paper":
    print("You lose! ")
elif Your_turn == "rock" and CPU == "paper":
    print("You Lose! ")
elif Your_turn == "rock" and CPU == "scissors":
    print("You Win")
elif Your_turn == "paper" and CPU == "rock":
    print("You Win")
elif Your_turn == "paper" and CPU == "scissors":
   print("You lose! ")
elif Your_turn == "scissors" and CPU == "rock":
    print("You lose")
elif Your_turn == "scissors" and CPU == "paper":
    print("You Win! ")


    




    

