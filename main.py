from tkinter import *
from PIL import Image, ImageTk
import cv2 
from picamera import PiCamera

def take_photo():
    camera.capture("image.jpg")

camera = PiCamera()

window = Tk()

window.geometry("480x320")

# This command hides the title bar
#window.attributes('-type', 'dock')

pixel = PhotoImage(width = 1, height = 1)

label = Label(window)
label.config(width = 380, height = 288)
label.grid(row = 0, column = 1, rowspan = 2)
cap = cv2.VideoCapture(0)

button01 = Button(window, text="Cheeese!", image = pixel, width = 100, height = 128, compound = "c", command = take_photo)
button01.grid(row = 0, column = 0)

button02 = Button(window, text="Shutdown", image=pixel, width = 100, height = 128, compound = "c")
button02.grid(row = 1, column = 0)

def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)

show_frames()
window.mainloop()
