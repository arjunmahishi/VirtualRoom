#Cryptological RPG\

import time
import os

def aText(s,n):
    for e in s:
        print (e, end=''),
        time.sleep(n)


def mainMenu():
    print ("\t\t\t\t",end='')
    aText("CIPHER",0)
    print ("\n\n\n")
    aText("1. New game \n2. Load game ",0)
    return int(input("\n\tChoice : "))- 1 

def newGame():
    os.system("cls")
    name = input("Please enter your charecter name : ")
    print ("\nHello " + name + " welcome to CIPHER. We hope you enjoy the game.",0.1)
    input()
    return name

def scene1(name):
    os.system("cls")
    print ("Here I am walking home from school on a normal day.")
    print ("It was the last day of school.")
    print ("....")
    input()
    print ("Shit!! there are 3 bullies catching up to me!!")
    print ("BULLY 1: Cough up the money,nerd!")
    print ("....")
    input()
    os.system('cls')
    print ("A few minutes later,I am lying on the ground surrounded by the 3 hairy gaints.")
    print ("I ended up on the ground because I wasn't ready to give them money and sombody dosen't handle rejections too well.")
    input("....")
    print("Right now my options are :\n1. Try to run away \n2. Try to negotiate ")
    c = input("\n\tChoice : ")
    if c == '1':
        os.system('cls')
        print ("I just start to run away from them.")
        print ("But almost immedeatly they grab on to my hood and yank me back.")
        print ("One of them punched me in the face and yelled \"Don't you try to fool us!!\"")
        input ("....")
        print ("\"Trust me, I wouldn't need to work that hard to fool you\" I sneered in a low tone.")
        input ("....")
        print ("As they prepared to give me a black eye, all of our phones beeped.")
        print ("The hair monsters stopped and started to see thair phones, I checked mine too.")
        input ("...")
        print ("We all had weird displays on our phones.")
        print ("The screen had a couple of random charecters, a couple of blanks to fill in,a submit button and an exit button.")
        print ("One of the bullies thought his phone was broken.")
        input ("....")
        print ("I think sombody has remotely launched this on everybody's phones...")
        print ("This must be some kind of a test...")
        print ("The random charecters are: DJQIFS")
        print ("there are exactly 6 blanks...same as the number of charecters.")
        input ("....")
        print ("maybe I should rearrange the letters and fill in the blanks...")
        print ("6 unique charecters...720 possiblities...but none of them make sense.")
        print ("Think!!")
        input ("....")
        print ("ENCRYPTION!! maybe the text is encrypted.")
        print ("on applying a simple 'ceasar cipher', the text \"DJQIFS\" turns into the word \"CIPHER\".")
        input ("SUBMIT...")
        print ("It worked!!!")
        input ()
    

c = mainMenu()
print (c)
if c == 0:
    scene1("warlock")
