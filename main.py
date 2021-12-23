# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
#from picamera import PiCamera

#camera = PiCamera()

# Create an instance of TKinter Window or frame
window = Tk()
window.poll = True

# Set the size of the window
window.geometry("700x350")
window.wm_attributes('-type', 'splash')

def take_photo():
    return_value, image = cap.read()
    cv2.imwrite("imgae.png", image)
    window.poll = False

def take_new_photo():
    window.poll = True
    show_frames()

def print_photo():
    print("Print!")

def shutdown():
    window.destroy()


pixel = PhotoImage(width = 1, height = 1)

#button_border = Frame(window, highlightbackground = "black", hightlightthickness = 2, bd = 0)

show_live_photo = True

button01 = Button(window, text="Cheeese!", image = pixel, width = 100, height = 147, compound = "c", command = take_photo, bg = "white", fg = "black", bd = 0, activebackground = "white", activeforeground = "black")
button01.grid(row = 0, column = 0)

button02 = Button(window, text="Shutdown", image=pixel, width = 100, height = 146, compound = "c", bg = "white", fg = "black", bd = 0, activebackground = "white", activeforeground = "black")
button02.grid(row = 1, column = 0)

# Create a Label to capture the Video frames
label =Label(window)
label.config(width = 350, height = 314)
label.grid(row = 0, column = 1, rowspan = 2)
cap= cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
    if window.poll:
        button01.configure(text = "Cheeese!", command = take_photo, bg = "white", fg = "black")
        button02.configure(text = "Shutdown", bg = "white", fg = "black", command = shutdown)
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        label.after(20, show_frames)
    else:
        photo = cv2.imread("image.png")
        label.configure(image = photo)
        button01.configure(text = "Print", command = print_photo, bg = "white", fg = "black")
        button02.configure(text = "Take new Photo", command = take_new_photo, bg = "white", fg = "black")


show_frames()
window.mainloop()
