print("Welcome to my Quiz")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")

print("")
score = 0

answer = input("What does 3D2Y stand for? ")
if answer == "3 Days 2 Years":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is Law's full name? ")
if answer == "Trafalgar D Water Law":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What is the name of Sanji's family organization? ")
if answer == "Germa 66":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What is the name of Nami's sister? ")
if answer == "Nojiko":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("Who separated the Straw Hats? ")
if answer == "Kuma":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

print("")
print("You got "+str(score) +" questions correct!")
print("")
print("You got "+str((score / 5) *100) +" %!")
