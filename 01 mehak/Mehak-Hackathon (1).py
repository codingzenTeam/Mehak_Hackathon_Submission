import turtle

import random



movies = ["AVATAR", "TITANIC", "THE PURSUIT OF HAPPYNESS", "JURASSIC PARK", "THE INTERN"]

songs = ["UPTOWN FUNK", "SHAPE OF YOU", "BOHEMIAN RHAPSODY", "NOVEMBER RAIN", "HOTEL CALIFORNIA"]

countries = ["UNITED STATES OF AMERICA", "JAPAN", "BRAZIL", "UNITED KINGDOM", "GERMANY"]



themes = {

    "MOVIES": movies,

    "SONGS": songs,

    "COUNTRIES": countries,

}



theme = turtle.textinput("Hangman Game", "Choose a theme: movies, songs, or countries")

theme = theme.upper()



while theme not in themes:

    theme = turtle.textinput("You have chosen an invalid theme. Kindly choose a theme from movies, songs, or countries.")



word = random.choice(themes[theme.upper()])

t = turtle.Turtle()

t.speed(0)

t.penup()

t.hideturtle()

t.goto(-100, 0)



turtle.bgcolor("lightblue")

turtle.title("Hangman Game")

turtle.setup(width=800, height=600)

t.goto(0, 200)

t.write("Hangman Game", align="center", font=("Calibri", 24, "bold"))

t.goto(0, 150)

t.write("_ " * len(word), align="center", font=("Calibri", 16, "normal"))



guessed = []
def draw_hangman(incorrect_guesses):

    if incorrect_guesses == 1:

        # Draw the horizontal bar

        t.penup()

        t.goto(-150, -200)

        t.pendown()

        t.forward(300)

        t.penup()



    if incorrect_guesses == 2:

        # Draw the vertical bar

        t.goto(0, -200)

        t.pendown()

        t.right(90)

        t.forward(400)

        t.penup()



    if incorrect_guesses == 3:

        # Draw the rope

        t.goto(-50, 200)

        t.pendown()

        t.forward(150)

        t.penup()



    if incorrect_guesses == 4:

        # Draw the head

        t.goto(-25, 150)

        t.pendown()

        t.circle(25)

        t.penup()



    if incorrect_guesses == 5:

        # Draw the body

        t.goto(0, 150)

        t.pendown()

        t.forward(150)

        t.penup()



    if incorrect_guesses == 6:

        # Draw the left arm

        t.goto(0, 100)

        t.pendown()

        t.right(45)

        t.forward(75)

        t.penup()



    if incorrect_guesses == 7:

        # Draw the right arm

        t.goto(0, 100)

        t.pendown()

        t.left(90)

        t.forward(75)

        t.penup()



    if incorrect_guesses == 8:

        # Draw the left leg

        t.goto(0, 0)

        t.pendown()

        t.right(45)

        t.forward(75)

        t.penup()



    if incorrect_guesses == 9:

        # Draw the right leg

        t.goto(0, 0)

        t.pendown()

        t.left(90)

        t.forward(75)

        t.penup()



    if incorrect_guesses == 10:

        # Draw the rope attached to the neck

        t.goto(-50, 200)

        t.pendown()

        t.left(90)

        t.forward(50)

        t.penup()





incorrect_guesses = 0

max_wrong_guesses = 11



while incorrect_guesses < max_wrong_guesses:

    letter = turtle.textinput("Hangman Game", "Enter a letter: \n (You have 6 guesses in total) ").upper()

    

    if letter in guessed:

        turtle.goto(0, -250)

        turtle.write("You already guessed that letter.", align="center", font=("Calibri", 16, "normal"))

        continue



    guessed.append(letter)



    if letter in word:

        display_word = ""

        for char in word:

            if char in guessed:

                display_word += char + " "

            else:

                display_word += "_ "

        

        t.goto(0, 150)

        t.clear()

        t.write(display_word, align="center", font=("Calibri", 16, "normal"))

        

        if "_" not in display_word:

            turtle.goto(0, -270)

            turtle.write("Congratulations, you guessed the word!", align="center", font=("Calibri", 16, "bold"))

            break



    else:

        incorrect_guesses += 1

        draw_hangman(incorrect_guesses)



if incorrect_guesses == max_wrong_guesses:

    turtle.goto(0, -250)

    turtle.write("Sorry, you ran out of guesses. The word was " + word, align="center", font=("Calibri", 16, "bold"))



turtle.done()