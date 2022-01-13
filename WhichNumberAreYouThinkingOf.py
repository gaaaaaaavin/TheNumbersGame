import os                                           # needed to end script
import time                                         # timer

def quit():
    print("\n[CLOSING SCRIPT IN 10 SECONDS]")
    time.sleep(10)
    os._exit(0) 
def trueOrFalse(x,y):
    if x==True and y==True:
        return "a"                                  # (01,03,05,07,09)
    elif x==True and y==False:
        return "b"                                  # (02,04,06,08,10)
    elif x==False and y==False:
        return "c"                                  # (12,14,16,18,20)
    elif x==False and y==True:
        return "d"                                  # (11,13,15,17,19)
def inputAnswer(x):                 # returns True or False depending on question
    x=x.upper()[0]                  # .upper() and [0] to simplify user's input
    if x=="Y":
        return True
    elif x=="N":        
        return False
    else:
        print("Opps, could you retype that?")
        wrongInput=input("")[0]
        wrongInput=wrongInput.upper()
        if wrongInput=="Y":
            return True
        elif wrongInput==("N"):
            return False
        else:
            print("I dont want to play this game")
            print("with you any more. bye.")
            quit()

rule1="\n- the first rule of FIGHT CLUB is,\n you do not talk about FIGHT CLUB."
rule2="\n- the second rule of FIGHT CLUB is,\n YOU DO NOT TALK ABOUT FIGHT CLUB!"
rule3="\n- the third rule is,\n the number has to be between 1 and 20."
print("Welcome to my first game using python,")
print("- WHICH NUMBER ARE YOU THINKING OF -\n                   By Gavin D'Souza")
time.sleep(3)
print("Before we begin the game,")
print("a simple 'y' for yes or 'n' for no will suffice.\n")
time.sleep(2)
yn=input("did you understand? (y / n)\n")
yn=inputAnswer(yn)
if yn!=True:
    print("you can type 'yes' for yes instead of 'y'")
    print("and 'no' for no instead of 'n'")
    time.sleep(1)
else:
    print("Okay great, lets move on to the rules:\n")
time.sleep(1)
print("RULES:")                                     # rules
time.sleep(2)
print(rule1)
time.sleep(3)
print(rule2)
time.sleep(3)
print(rule3)
time.sleep(1)
input("press ENTER to continue...\n")
print("Think of number between 1 and 20\n")
time.sleep(3)
print("Thought of a number?\n")
time.sleep(1)
print("Okay then, lets get started...")
time.sleep(0.5)

isItDivisible7=input("Can it be divided by 7? (y / n)\n")
isItDivisible7=inputAnswer(isItDivisible7)
if isItDivisible7==True:
    is7=input("Is it 7? (y / n)\n")
    is7=inputAnswer(is7)
    if is7==True:                                   # True for  07
        print("Thanks for playing!")
        quit()
    else:                                           # False for 14
        print("I knew it was 14!")
        time.sleep(1)
        print("Thanks for playing!")
        quit()

tenOrBelow=input("Is your number 10 or below? (y / n)\n")
tenOrBelow=inputAnswer(tenOrBelow)
isItOdd=input("Is it an ODD number? (y / n)\n")
isItOdd=inputAnswer(isItOdd)
isItDivisible5=input("Can it be divided by 5? (y / n)\n")
isItDivisible5=inputAnswer(isItDivisible5)
isItDivisible3=input("Is your number divisible by 3? (y / n)\n")
isItDivisible3=inputAnswer(isItDivisible3)
isVowel=input("Does it start with a vowel? (y / n)\n")
isVowel=inputAnswer(isVowel)
trueOrFalse=trueOrFalse(tenOrBelow,isItOdd)

if trueOrFalse=="a":
    if isVowel==True:                               # True for  01
        print("Your number is 1!")
        time.sleep(1)
        print("thanks for playing")
        quit()
    elif isItDivisible3==True:
        is9=input("Is your number 9? (y / n)\n")
        is9=inputAnswer(is9)
        if is9==True:                               # True for  09
            print("Thanks for playing!")
            quit()
        else:                                       # False for 03
            print("My next guess was 3")
            time.sleep(1)
            print("Thanks for playing!")        
            quit()
    elif isItDivisible5==True:                      # True for  05
        print("It's 5, isn't is.")
        time.sleep(1)
        print("Thanks for playing!")
        quit()
elif trueOrFalse=="b":
    if isItDivisible3==True:                        # True for  06
        print("Your number is 6!")
        time.sleep(1)
        print("Congratulations on typing Ys and Ns.")
        quit()
    elif isItDivisible5==True:                      # True for  10
        print("Did you really pick 10?")
        time.sleep(1)
        print("Oh well, hope you had as much fun as")
        print("i had writing this!")
        quit()
    elif isVowel==True:                             # True for  08
        print("8? That was easy...")
        time.sleep(1)
        quit()
    else:
        is4=input("It's 4! It has to be 4. (y / n)\n")
        is4=inputAnswer(is4)
        if is4==True:                               # True for  04
            print("I knew it.\nThanks for playing!")
            quit()
        else:                                       # False for 02
            print("Should've know it was 2.")
            time.sleep(1)
            print("Wasn't that fun?")
            time.sleep(4)
            print("No?")
            time.sleep(5)
            print("[scrapping system for bank details]")
            time.sleep(1.5)
            print("[payload secured]")
            time.sleep(1)
            print("[exiting script now]")
            quit()     
elif trueOrFalse=="c":
    if isItDivisible3==True:
        if isVowel==True:                           # True for  18
            print("Your number is 18!")
            time.sleep(1)
            print("Thanks for playing!")
            quit()
        else:                                       # True for  12
            print("Your number is 12!")
            time.sleep(1)
            print("Thanks for playing!")
            quit()
    elif isItDivisible3==False:                     # True for  20
        if isItDivisible5==True:
            print("Your number is 20!")
            time.sleep(1)
            print("Thanks for playing!")
            quit()
        else:                                       # False for 16
            print("Well that leaves 16? (y / n)\n")
            time.sleep(1)
            print("I hope that was right...")
            quit()
elif trueOrFalse=="d":
    is13=input("It's 13 right? (y / n)\n")
    is13=inputAnswer(is13)
    if is13==True:                                  # True for  13
        print("First try.")
        quit()
    elif isItDivisible3==True:                      # True for  15
        print("Your number is 15!")
        time.sleep(1)
        print("Thanks for playing!")
        quit()
    elif isVowel==True:                             # True for  11
            print("Your number is 11!")
            time.sleep(1)
            print("Thanks for playing!")
            quit()
    else:
        is17=input("that leaves 17. Right? (y / n)\n")
        is17=inputAnswer(is17)
        if is17==True:                              # True for  17
            print("I knew it from the start,")
            print("I just like wasting your time.")
            quit()
        else:                                       # False for 19
            print("I knew it was 19 right from the beginning...")
            time.sleep(3)
            print("just needed time scrapping your system")
            print("for any personal infomation.")
            quit()
else:
    print("How'd you reach here?")
    time.sleep(1)
    print("end of script")
    
#GAVIN D'SOUZA
