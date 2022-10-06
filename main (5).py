print("This is game two of 3. it is a bit more complex, though still not too much!")
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 5:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 5:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the father fact")
guess1 = input("how many fathers are there in the world? ")
check_guess(guess1, "1.5 billion")
guess2 = input("how many fathers in the usa")
check_guess(guess2, "66 million")
guess3 = input("which year was fathers day recognized a national holiday")
check_guess(guess3, "1972")
guess4 = input("which country is fathers day all about lighters")
check_guess(guess4, "France")
guess5 = input("which president made fathers day official")
check_guess(guess5, "Woodrow Wilson")
print("Your Score is" + str(score))