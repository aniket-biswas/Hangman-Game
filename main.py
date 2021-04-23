import HangmanTurtle


def getWord():
    from wordfile import words
    import random
    return random.choice(words)


word = getWord()


HangmanTurtle.rectangle()
HangmanTurtle.hanger()
wrong = 0
word = list(word)

print("You have to guess this word.\n", "- " * len(word))
s = set()

answer = "_" * len(word)
answer = list(answer)
while (wrong < 6):
    if answer == word:
        print("You completed the word, Hurray!!")
        break

    guess = input("Enter your guess: ")
    if guess not in s:
        s.add(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    answer[i] = guess
                    print("Correct guess")
                    print(" ".join(answer))
        else:
            wrong += 1
            if wrong == 1:
                HangmanTurtle.circle()
            elif wrong == 2:
                HangmanTurtle.neck()
            elif wrong == 3:
                HangmanTurtle.rhand()
            elif wrong == 4:
                HangmanTurtle.lhand()
            elif wrong == 5:
                HangmanTurtle.rleg()
            elif wrong == 6:
                HangmanTurtle.lleg()
            print("Wrong guess, Try again")
    else:
      print("you have already guessed this character")                                                                                
