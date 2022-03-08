from tkinter import *
#from PIL import ImageTk
#from PIL import Image
import PIL.Image
import PIL.ImageTk
import tkinter as tk

userName = input("What is your name? ")
#todaysChoice = input("What would you like to wear today " + userName +"? ")

userTask = input("Hi " + userName + ", what would you like to do today? \nA) Put an item in the closet \nB) Decide what to wear\n ")


def displayDress(self, p):
    
    dressPath = p
    # Create the canvas, size in pixels.
    canvas = tk.Canvas(width=1000, height=800, bg='black')
        
    # Pack the canvas into the Frame.
    canvas.pack(expand=YES, fill=BOTH)
        
    # Load the .gif image file.
    gif1 = tk.PhotoImage(file= 'dresses/' + dressPath + '.png')
        
    # Put gif image on canvas.
    # Pic's upper-left corner (NW) on the canvas is at x=50 y=50.
    canvas.create_image(50, 50, image=gif1, anchor=NW)
        
    # Run it...
    tk.mainloop()



while True:
    userChoice = input("Hey " + userName + " which dress would you like to try today [A/B/C/D/E or Q]: \nA) Red \nB) Blue \nC) Yellow \nD) Green \nE) Pink \nQ) Quit \n")
    if userChoice.lower() == "a":
        print("\nGood choice " + userName + " you look amazing in your red dress.\n")
        dressToDisplay = "red-dress"
        displayDress(userChoice, dressToDisplay)
        
    elif userChoice.lower() == "b":
        print("\nExcellent choice " + userName + " you look amazing in your blue dress.\n")
        dressToDisplay = "blue-dress"
        displayDress(userChoice, dressToDisplay)
        
    elif userChoice.lower() == "c":
        print("\nExcellent choice " + userName + "  you look amazing in your yellow dress.\n")
        dressToDisplay = "yellow-dress"
        displayDress(userChoice, dressToDisplay)
        
    elif userChoice.lower() == "d":
        print("\nExcellent choice " + userName + " you look amazing in your green dress.\n")
        dressToDisplay = "green-dress"
        displayDress(userChoice, dressToDisplay)
        
    elif userChoice.lower() == "e":
        print("\nExcellent choice " + userName + "  you look amazing in your pink dress.\n")
        dressToDisplay = "pink-dress"
        displayDress(userChoice, dressToDisplay) 
        
    elif userChoice.lower() == "q":
        print("\nYou will look amazing in any dress!\nHave a great day! \n")
        break