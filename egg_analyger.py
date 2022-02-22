from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk,ImageDraw
import cv2
import os,time
from datetime import datetime

fps = 1
cap = None 
CAMERA_PORT = 0
count = 0
interval = 15
last_min = 0


if not os.path.exists('images'):
  # Create a new directory because it does not exist 
  os.makedirs('images')
  print("The new directory is created!")

def scan():
    global cap,count,fps,interval,last_min
    if cap is None:
        cap = cv2.VideoCapture(CAMERA_PORT)

    ret, img = cap.read()
    now = datetime.now() 
    image_name = now.strftime("images/%Y_%m_%d_%H_%M_%S_%f.jpg")

    if ret:
        orginal_img = img.copy()
        
        #for display and grid
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(img)
        #img = img.resize((150,150)) # new width & height
        img = ImageTk.PhotoImage(image=img)
     
        #display frame on gui 
        camera_panel.config(image=img)
        camera_panel.tkimg = img #

        
        a = datetime.now().minute
        if a > last_min:  # every 15 seconds
            cv2.imwrite(image_name, orginal_img)
            print("saved "+image_name)
            last_min = a


        
        count = count+1

    camera_panel.after(fps, scan) # change 25 to other value to adjust FPS


###########################
### GUI START
###########################

root = Tk()
root.title('EGG ANALYZE')
#root.geometry('1000x600')
# root.attributes('-fullscreen', True)

#getting screen width and height of display
#width= root.winfo_screenwidth() 
#height= root.winfo_screenheight()

# #setting tkinter window size
root.geometry("%dx%d" % (600, 400))

# camera frame start 
camera_frame =Frame(root,bg="gray")
camera_frame.pack()

#add new camera panel
camera_panel = Label(camera_frame)
camera_panel.pack()

#camera frame end
scan()
#root.iconbitmap('/home/baset/Activity/clarkson/gui/final/icon.ico')
#root.iconphoto(False, PhotoImage(file='asset/icon.png'))
root.mainloop()

if cap:
    cap.release()