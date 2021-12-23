# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
window = Tk()

# Set the size of the window
window.geometry("700x350")


pixel = PhotoImage(width = 1, height = 1)

button01 = Button(window, text="Cheeese!", image = pixel, width = 100, height = 128, compound = "c")
button01.grid(row = 0, column = 0)

button02 = Button(window, text="Shutdown", image=pixel, width = 100, height = 128, compound = "c")
button02.grid(row = 1, column = 0)

# Create a Label to capture the Video frames
label =Label(window)
label.config(width = 380, height = 288)
label.grid(row = 0, column = 1, rowspan = 2)
cap= cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)

show_frames()
window.mainloop()