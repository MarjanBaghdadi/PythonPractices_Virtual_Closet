from tkinter import *
#from PIL import ImageTk
#from PIL import Image
import PIL.Image
import PIL.ImageTk
import tkinter as tk
#from vcCommunication import userChoice


class VCDisplay:
    
    def __init__ (self, userChoice):
        self.userChoice = userChoice

        
    def display(self):
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(width=1000, height=1000, bg='black')
        
        # Pack the canvas into the Frame.
        canvas.pack(expand=YES, fill=BOTH)
        
        # Load the .gif image file.
        gif1 = tk.PhotoImage(file='red-dress.png')
        
        # Put gif image on canvas.
        # Pic's upper-left corner (NW) on the canvas is at x=50 y=10.
        canvas.create_image(10, 10, image=gif1, anchor=NW)
        
        # Run it...
        tk.mainloop()
    



#img = PIL.Image.open("red-dress.png")
#img.show()
#new_image = img.resize((400, 400))
#new_image.show()