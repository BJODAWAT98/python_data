  # Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""

"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

"""
Challenge 3
Read the words from a file

"""

"""
Challenge 4
    Get the list of Internet after web scrapping
"""

a="bhavya"
b=a.count("a")


import random
words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon'
        ]

answer=random.choice(words)
gusses_list=[" _ "]*len(answer)
print(" _ "*len(answer))
lives=len(answer)*2
while lives>0:
    char_location,char=[],""
    
    input_character=input("enter characher one by one")
    if input_character=="quite":
        break
    
    elif len(input_character)>1:
        print("only one character is allowed")
    elif input_character in answer:
        lives-=1
        print("yey! you gusses one right character ",input_character,"|| remaining lives are",lives)

        char_location=[i for i,char in enumerate(answer) if char == input_character]  
        print(char_location)
        for location in char_location:
            gusses_list[location]=input_character
        print("".join(gusses_list))
        if ("".join(gusses_list)) == answer:
            print("you won!")
            break
        
    elif input_character not in answer:
        lives-=1
        print("you gusses wrong character : Try again ||",lives," remaining")
        
else:
    print("you loose the game")
        
        


























