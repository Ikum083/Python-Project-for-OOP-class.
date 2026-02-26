# The script of the game goes in this file.

define e = Character("Eileen")
define g = Character("Goldship", who_color = "#e43131")

#default install = True


# function to resize sprite
transform zoomed:
    zoom 0.9
    xalign 0.4
    yalign 0.3

transform zoomed_left:
    zoom 0.9
    linear 1.0 xalign -0.2
    yalign 0.3

transform show_bigpic:
    zoom 0.5
    xalign 0.6
    yalign 0.2

transform show_smallpic:
    zoom 1.5
    yalign 0.3
    xalign 0.5

define bgm_loop = "audio/music/1syo1pai.mp3"
    

label start:
# setup scene
    scene classroom
    play music bgm_loop volume 0.3 loop

    show goldship idle at zoomed

    g "Welcome Trainer!"
    $ name = renpy.input("What is your name?")
    g "Welcome [name]!"

    hide goldship idle
    show goldship curious at zoomed
    g "What can I do with you today?"
    g "humu~ humu~"
    hide goldship curious
    show goldship idle at zoomed
    g "Ohhhh, you want to learn how to code in python, trainer?"
    g "Well you came to the right person!"

# Player picks the topic to be discussed
label ask:
    scene classroom
    show goldship idle at zoomed
    g "Please ask away!"
    menu:
        "Installation":
            jump Installation
        "Getting Started":
            jump Starting
        "User Input":
            jump Input
        "Arithmetic Equations":
            jump Arithmetic
        "Data types":
            jump Data
        "That's all for now...":
            jump Done

# tutorial about python installation
label Installation:
g "Installing python eh?"
g "That's easy Trainer [name]!"
g "First you go to the python website, it's{a=https://www.python.org/downloads/} https://www.python.org{/a}."
show install python at show_bigpic
hide goldship idle
show goldship idle at zoomed_left
g "Lookie here~"
g "See that button named 'Python install manager'?"
g "You press it."
hide install python
show python saved at show_smallpic
g "This will download the python installer."
g "Then you can install python!"
g "It's easy isn't it trainer [name]?"
jump ask

# tutorial about getting started with python
label Starting:
g "To get started!"
show hello world at show_smallpic
hide goldship idle
show goldship curious at zoomed_left
g "This trainer, is the basics of all programming."
g "The print command simply displays a text in your terminal"
g "Right now it is printing 'hello world'"
hide hello world
show print output at show_smallpic
g "This will be the output."
g "Pretty easy isn't it?"
jump ask

# Getting user input
label Input:
hide goldship idle
show goldship curious at zoomed
g "To get to input from your user, you need to use the 'input' function."
show python input at show_smallpic
hide goldship curious
show goldship curious at zoomed_left
g "The syntax is like this, you assign a key 'user' to contain a value given by the user."
hide python input
show input output at show_smallpic
g "This is what it looks like in the terminal when the code is runned."
hide input output
show print input at show_smallpic
g "You can also print the user's input."
hide print input
show print user input at show_smallpic
g "This is what that will look like in the terminal."
jump ask

label Arithmetic:
hide goldship idle
show goldship curious at zoomed
g "You can perform arithmetic equations in python!"
g "You can add, subtract, multiply and divide."
hide goldship curious
show goldship curious at zoomed_left
show python sum at show_smallpic
g "Here is an example of using python to add 4 and 5."
hide python sum
show sum output at show_smallpic
g "And the output will be 9"
g "It is important to remember that arithmetic equations only work when using integer data types."
g "We will talk about data types later."
g "For now let's talk about subtraction."
hide sum output
show python sub at show_smallpic
g "It is the same with addition, except this time you use a dash as the minus sign"
hide python sub
show sub output at show_smallpic
g "The output should look like this."
hide sub output
show python multi at show_smallpic
g "This is how you perform multiplication, by using an asterisk as the multiplication sign."
hide python multi
show multi output at show_smallpic
g "The output should look like this."
hide multi output
show python divide at show_smallpic
g "And this is how you divide two numbers, by using a dash as the division sign."
hide python divide
show divide output at show_smallpic
g "The output should look like this."
g "Now let me introduce you to two more unique arithmetic functions to use for python."
hide divide output
show python floor at show_smallpic
g "This here trainer is floor division, it is done by using double dashes."
hide python floor
show floor output at show_smallpic
g "This is similar to division but it rounds it down to the nearest integer."
g "In which our case turned 0.8 to 0"
hide floor output
show python modulus at show_smallpic
g "This here trainer is modulus, also similar to division but this time it outputs the remainder."
hide python modulus
show modulus output at show_smallpic
g "Lookie here~ dividing 4 by 5 results in a remainder 4, thus the output of our code."
g "That's all for arithmetic trainer, but there's still more operations you can just learn at your own!"
jump ask

label Data:
g "Now onto data types trainer!"
g "There are many different types of data used in python"
show goldship curious at zoomed_left
g "Lookie here~"
show python string at show_smallpic
g "This here trainer is a string, in simple terms it is a word."
g "You can identify a string by using single or double quotation marks."
hide python string
show string output at show_smallpic
g "This is what it would look like in the terminal."
hide string output
show python integer at show_smallpic
g "Next is integers, as you can guess trainer, it is a number."
g "Unlike strings, integers don't use quotation marks and are simply typed as is."
hide python integer
show integer output at show_smallpic
g "This is what it will look like in the terminal."
hide integer output
show python float at show_smallpic
g "This here is a float, it is simply a decimal value."
g "What seperates a float from an integer is the use of a decimal point and the decimal values."
hide python float
show float output at show_smallpic
g "This is what floats look like in the terminal."
g "Now I will teach you trainer about composite data types, there's many in python but I will focus on lists and dictionaries for now."
g "Composite data types are data types that contain multiple data."
g "Think of it like a box full of different items."
hide float output
show python list at show_smallpic
g "This here trainer is a lists, it's the most basic composite data type in python."
g "It is defined by a square bracket. It can contain different data types but for this example we will be using integers."
hide python list 
show list output at  show_smallpic
g "When you print it, this is how it looks like in the terminal."
g "You can print certain parts of the set by using an index."
g "An index is basically the number assigned to an element of a list and it is numbered starting from 0."
hide list output 
show python index at show_smallpic
g "To print out the first element we need to call out the index 0, meaning the first element from our list."
hide python index
show index output at show_smallpic
g "As you can see it will print out the first element from our list."
g "Next let's learn about dictionaries!"
hide index output
show python dictionary at show_smallpic
g "Dictionaries are a collection of key-value pairs."
g "Key-value pairs means it is a pair of data types that are dependent of each other."
g "Example, in our dictionary here we assigned the string 'First' to the integer 1."
hide python dictionary
show dictionary output at show_smallpic
g "When we print a dictionary it looks like this."
g "To call out certain values in dictionaries we need to call out the key."
hide dictionary output
show python dict key at show_smallpic
g "A key like our string 'First' can be used to call out the integer assigned to him, which in our case is 1."
hide python dict key
show dict key output at show_smallpic
g "When you print it, it shows the value assigned to key 'First'."
jump ask

label Done:
g "Ok trainer, what I taught you today is only the basics."
g "If you want to really take this to the next level, you should take an online course or watch a tutorial video on youtube."
g "Oh! Spe is calling me."
g "Well, see you next time trainer!"

return

