# Put your code here
import random


name = raw_input("What is your name?: ")
print "Hello %s! I am thinking of a number between 1 and 100." % name

number = random.randint(1, 100)

num_guesses = 0

while True:
    guess = int(raw_input("Try and guess my number: "))
    if guess > 100 or guess < 1:
        print "Silly! That number's not in our range!"
    # if type(guess) != int:
    #     print "That's not even a number!"
    if guess != number:
        if guess > number:
            print "Too high!"
        elif guess < number:
            print "Too low!"
        num_guesses += 1

    else:
        print "Congratulations %s! %s is the number" % (name, guess)
        print "You found my number in %s guesses" % num_guesses
        break
