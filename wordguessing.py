import random

name = input("Cual es tu nombre? ")

print("Buena suerte ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


word = random.choice(words)

guesses = ""

turns = 12

while turns > 0:
    
    failed = 0
    
    for char in word: 

        if char in guesses:
            print(char, end=" ")
    
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("Ganaste!")
        print("La palabra es: ", word)
        break
    
    print()
    guess = input("adivina un caracter: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

        print("Tienes ", turns, "turnos")

        if turns == 0:
            print("Perdiste")
