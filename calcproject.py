#coding: utf-8
#   Modules

from math import *
from time import *
from site import *
from sympy import *
from string import *
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

#   Welcome Part

print ("Welcome to Calculus Centre! \n")
print ("By Yanwen Xu, for the Calculus Final Project\n")
print ("-------------------------------------------------\n")
sleep(1)
print ("Main Menu\n")
sleep(0.2)
print ("Available functions:\n")
sleep(0.2)
print ("a. Take Derivatives (Multi-terms)\n")
sleep(0.2)
print ("b. Take Derivatives (Single-term simple power-rule ones)\n")
sleep(0.2)
print ("c. Take Integrals\n")
sleep(0.2)
print ("d. Do Limits\n")
sleep(0.2)
print ("e. Series Expansion\n")
sleep(0.2)
print ("f. Do Polymonials\n")
sleep(0.2)
print ("g. The Potato and The Rock\n")
sleep(0.2)
print ("h. Help\n")
sleep(1)
menuMain = raw_input("Enter the letter before the options: ")

#   De-casesensitive

menuMain = menuMain.upper()

#   Key function defs

def a():
    xyz = input("Take derivative in respect to? ")
    fxDiff = input("Input the function here: ")
    e = exp
    diffans = diff(fxDiff, xyz)
    print (diffans)
    
def b():
    print ("Input your term here: ")
    singleDiffNumb = input("Input your number part of the main body part of the term: ")
    singleDiffPwer = input("Input the power of your term: ")
    singleDiffVari = raw_input("In respect to? ")
    singleDiffNumb = singleDiffNumb * singleDiffPwer
    singleDiffPwer = singleDiffPwer - 1
    print ("%s %s ^ %s"%(singleDiffNumb, singleDiffVari, singleDiffPwer))
    
def c():
    intfx = input("function to integrate?")
    xyz = input("in respect to?")
    boundLower = input("Left bound?")
    boundHigher = input("Right bound?")
    intans = integrate(intfx, (xyz, boundLower, boundHigher))
    print (intans)
def d():
    limfx = input("function?")
    xyz = raw_input("variable?")
    limnum = input("%s -> ?"%(xyz))
    limans = limit(limfx, xyz, limnum)
    print (limans)
def e():
    print ("Under development")
def f():
    print ("Under development")
def g():
    print ("The Rock is better than the potatoes boiled in water with temperature of 91 degree C!\n")
def h():
    print ("Help en route...")
def exit():
    sleep(0.5)
    sys.exit("\n-- Thank you, see you again at Calculus Centre! --\n")

#   Main Menu Options
def optionMain():

    if menuMain == "A":
        a()
        exit()
    if menuMain == "B":
        b()
        exit()
    if menuMain == "C": 
        c()
        exit()
    if menuMain == "D":
        d()
        exit()
    if menuMain == "E":
        e()
        exit()
    if menuMain == "F":
        f()
        exit()
    if menuMain == "G":
        print ("More options coming soon! (if at all)\n")
    if menuMain == "H":
        h()
        exit()
    else :
        sleep(0.2)
        sys.exit("Error in option input, please restart the program. \n")
#   Call functions here 

optionMain()

#   Debug

print (menuMain)

#   End of Program


#   Stuff
