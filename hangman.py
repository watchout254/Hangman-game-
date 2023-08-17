import random
import hangman_stages
import word_file
print("\t\t\tWozzah, Welcome folks to Hangman!!")
lives = 6
chosen_one = random.choice(word_file.words)
print(chosen_one)

#empty list
nishoo = []
for a in range(len(chosen_one)):
    nishoo += '-'
print(nishoo)

gameover = False
while not gameover:
        guess = input("Hey there! Guess a letter: ").lower()
        for position in range(len(chosen_one)):
            letter = chosen_one[position]
            if letter == guess:
                nishoo[position]=guess
        print(nishoo)

        if guess not in chosen_one:
            lives -= 1
            if lives ==0:
                gameover = True
                print("Ooopsies, You lose")

        if '-' not in nishoo:
            gameover = True
            print("You win")
        print(hangman_stages.stages[lives])



