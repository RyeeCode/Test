import random
print("Lets play rock,paper,scissors")
option1 = "rock"
option2 = "paper"
option3 = "scissors"
user_answer = input("Rock?,Paper?,Scissors?")
if user_answer.lower() in option1:
    print("You have chosen rock")
elif user_answer.lower() in option2:
    print("You have chosen paper")
elif user_answer.lower() in option3:
    print("You have chosen scissors")
    
choices = ("rock","paper","scissors")
ai_choice = random.choice(choices)

print("The Ai has chosen",ai_choice)
if ai_choice.lower() == user_answer:
    print("Its a tie")
    
if (ai_choice == "scissors" and user_answer == "rock")or(ai_choice == "paper" and user_answer == "scissors")or(ai_choice == "rock" and user_answer == "paper"):
    print("You win")
if(ai_choice == "rock" and user_answer == "scissors")or(ai_choice == "scissors" and user_answer == "paper")or(ai_choice == "paper" and user_answer == "rock"):
    print("You lose:(")