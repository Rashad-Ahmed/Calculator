import time
import pyautogui
import datetime
import tkinter as tk

def screenShot():
    date=datetime.datetime.today().strftime("%b_%d_%Y_%H_%M_%S")
    name='D:/Python/Screenshots data/{}.png'.format(date)
    img=pyautogui.screenshot(name)
    img.show()


root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(
    frame,
    text="Take Screenshot",
    command=screenShot
)

button.pack(side=tk.LEFT)

close=tk.Button(
    frame,
    text="Quit",
    command=quit
)

close.pack(side=tk.RIGHT)

root.mainloop()