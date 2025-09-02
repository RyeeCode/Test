import random
list = "abcdefghijklmnopqrstuvwxyz"
password = ("dcaz")
attempts = 0
while True:
    attempts = attempts + 1
    Letter1 = random.choice(list)
    Letter2 = random.choice(list)
    Letter3 = random.choice(list)
    guess = Letter1 + Letter2 +Letter3
    if guess == password:
        print(guess)
        print("password cracked")
        print(attempts)
        break
