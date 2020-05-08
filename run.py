"""
Algo.py - MinMax - Find Min & Max Values
Version : 1.0.0
Author : Seyyed Ali Mojatabvi
Repository : 

"""
import os
import platform 
import sys
from  iterative import iterative_binarysearch

from input import array

platform_system = platform.system()

def clear_screen():
    if platform_system == 'Linux':
        os.system('clear')
    elif platform_system == 'Windows':
        os.system('cls')


while True:
    clear_screen()
    print("MinMax Algorithms: ")
    print(" Methods: ")
    print("     1- Iterative ")
    print("     2- Recursive ")
    print("         Coming Soon ... \n ")
    print("     0- Exit ")
    try:
        option = int(input("Enter a method: "))
        x = int(input("Enter a number to Fine: "))
        if option < 0 or option > 4:
            raise Exception
    except:
        continue

    break

    
 

if option == 0:
    sys.exit(0)


value = False 

if option == 1:
    value = iterative_binarysearch(0,(len(array)-1),array,x)

if not(value):
    print("Your Number NOT Exists")
else:
    print("hey I Found Your Number")
