import random
words = ["max", "harison"]
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wordslen = len(words)

randomwordd = random.randint(0, wordslen -1)
randomword = words[randomwordd]
randomwordlen = len(randomword)
hangman = []

for x in range(randomwordlen):
    hangman.append("-")

print(hangman)
for x in range(100):
    guess = input("Please enter your guess: ")
    # check if guess has any letters in it from the random word
    if guess in randomword:
        # if it does find the index of the letter
        index = randomword.find(guess)
        # replace the dash with the letter
        hangman[index] = guess
        # if array join together to make the word then you win
        if randomword == ''.join(hangman):
            print("The word was: ", randomword)
            print("You win!")
            break
    else:
        print("Wrong!")
       
        print(hangman)
       
