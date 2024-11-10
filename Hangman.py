win = False
numLetters = 0
usedLetters = [""]*26
solution = "DEER"
currentWordState = "_"*(len(solution))
lettersChanged = 0
guesses = 0


def getLetter(numLetters, usedLetters, guesses):
    letterAvalible = True
    guessedLetters = str(input("Please input your guess:")).upper()
    if numLetters > 0:
        for count in range(0, numLetters):
            if guessedLetters == usedLetters[count] and len(guessedLetters) == 1:
                letterAvalible = False
    if letterAvalible:
        usedLetters[numLetters] = guessedLetters
    else:
        print("LETTER ALREADY USED TRY AGAIN")
    guesses += 1
    return numLetters, usedLetters, guesses


def letterCheck(numLetters, usedLetters, solution, currentWordState, lettersChanged):
    startLetters = lettersChanged
    for count in range(0, len(solution)):
        if solution[count] == usedLetters[numLetters]:
            currentWordState = currentWordState[0:count] + usedLetters[numLetters] + currentWordState[count+1:]
            lettersChanged += 1
    if startLetters == lettersChanged:
        print("This letter is not in the word")
    return currentWordState, lettersChanged


while not win:
    print(currentWordState)
    numLetters, usedLetters, guesses = getLetter(numLetters, usedLetters, guesses)
    currentWordState, lettersChanged = letterCheck(numLetters, usedLetters, solution, currentWordState, lettersChanged)
    if lettersChanged == len(solution):
        win = True
    numLetters += 1
print(solution)
print("You Win! You did it in {0} moves!".format(guesses))
