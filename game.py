# Put your code here
import random


name = raw_input("What is your name?: ")
print "Hello %s! I am thinking of a number between 1 and 100." % name

number = random.randint(1, 100)

num_guesses = 0
best_score = None

while True:
    user_guess = raw_input("Try and guess my number: ")
    try:
        guess = int(user_guess)
    except ValueError:
        print "That's not an integer!"
        continue
    if guess > 100 or guess < 1:
        print "Silly! That number's not in our range!"
    if guess != number:
        if guess > number:
            print "Too high!"
        elif guess < number:
            print "Too low!"
        num_guesses += 1

    else:
        print "Congratulations %s! %s is the number" % (name, 
                                                        guess)
        print "You found my number in %s guesses" % num_guesses

        # records if new best score and alerts user

        if best_score is None or num_guesses < best_score:
            print "Wow! That was your best game yet! New best score!"
            best_score = num_guesses
        else:
            print "Your best score was %s, try and beat it!" % (best_score)

        #checks if user wants to play again and if so resets number and guesses

        play_again = ''
        while True:
            play_again = raw_input("Would you like to play again?: y/n \n")\
            .lower()
            if play_again == "y" or play_again == "n":
                break
            else:
                print "not a valid input"
                continue
        if play_again == "y":
            number = random.randint(1, 100)
            num_guesses = 0
            continue
        else:
            break

