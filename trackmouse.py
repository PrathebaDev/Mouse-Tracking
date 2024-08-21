import pyautogui
import keyboard
import pyperclip
from tkinter import *

win = Tk() # it is equal to the main window
win.title("Mouse Coordinates by Tech-Titans")# wndow title
win.geometry("350x150")
win.config(bg="#E3D5CA")

coords_label = Label(win,text="X,Y Coordinates")
#coords_label.grid() #grid()=>shows the place where we want the label rows and columsn to appear
coords_label.config(bg="#E3D5CA",fg="white",font=("Lexend Mega",25))#fg=foregrounf=>color of the letters
coords_label.pack() # pack()=> puts the widget in any first available spot

instruction_label = Label(win,text="Press 'f2' to copy the coordinates.")
instruction_label.config(bg="#E3D5CA",fg="white",font=("Calibri",20))
instruction_label.pack() 
"""while True:
    pos_x,pos_y = pyautogui.position()
    coords_label.config(text= str(pos_x)+" "+str(pos_y))
    win.update()
    if keyboard.is_pressed("f2"):
        pyperclip.copy(str(pos_x)+" "+str(pos_y))"""

#update_coordinates()
win.mainloop()# keep the window up and keeps updating it

