#Homework 6
#Rebecca Moore RRM2738

#Question 1
def locker_puzzle():
#having 101 makes the length actually 1-100
#student one opened all lockers
    locker = [True] * 101
    ln = len(locker)
#this is where the second student closes every other locker
    student = 2
    n = student
#n is the locker number
    while n <= ln - 1:
        locker[n] = False

        n += student
#this loop covers student 3-100
    student = 3
    n = student
    while student <= ln - 1:
        n = student

        while n <= ln - 1:
            if locker[n] == False:
                locker[n] = True
            else:
                locker[n] = False
            n += student
        student += 1

    n = 1
#this prints all lockers that are open
    while n <= ln -1:
        if locker[n] == True:
            print(n)
        n += 1

#Question 2
def play_hangman():
#these are the variables used by the function
    word = "banjo"
    guessed = []
    dashes = "-" * len(word)
    guesses_left = 8

    print(dashes)
#this begins the loop that compares the user input to the word
    while guesses_left > 0 and not dashes == word:

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("That is not a letter. Enter a letter.")
#wont accept anything larger than one letter
        elif not guess.isalpha():
            print("That is not a letter. Enter a letter.")
#wont accept anything besides letters (no numbers or charecters)
        elif guess in guessed:
            print("You already guessed " + guess)
#tells the user if they have already guessed something
        elif guess in word:
            guessed.append(guess)
#adds the guess to the guessed variable to keep track of it
            dashes = update_dashes(word, guessed)
            print(dashes)
            print("You have", guesses_left, "tries remaining")
        else:
            guesses_left -= 1
            print(dashes)
            print("You have", guesses_left, "tries remaining")
        if '-' not in dashes:
            print("You win!")

        guessed.append(guess)
        if guesses_left == 0:
            print("You lose")


#this function changes the number of dashes printed based on the guesses
def update_dashes(word, guesses):
    result = ""

    for i in range(len(word)):
        if word[i] in guesses:
            result = result + word[i]
        else:
            result += '-'

    return result

#this function is used to call the other two functions 
def main():
    locker_puzzle()
    play_hangman()

main()
