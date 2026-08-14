import random 
secret_number=random.randint(1,100)

print("I am thinking of number between 1 to 100")
guess=int(input("Guess a Number: "))
while guess !=secret_number:
    if guess>secret_number:
        print("Too High")
    elif guess<secret_number:
        print ("Too Low")
    guess=int(input("Guess a Number: "))
print ("Your guess is correct ")
