from dataclasses import replace
import torch
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import glob
import time


def find_plastic(img_path):
    global img1, img2, replaced1, replaced2
    scanned = recycler(img_path)
    scanned.save()
    image_name = os.path.basename(img_path)
    scanned_path = f'C:/Users/thesc/Desktop/trashrecycler/runs/detect/exp/{image_name}'
    img1 = Image.open(img_path)
    img1 = img1.resize((500,300))
    replaced1 = ImageTk.PhotoImage(img1)
    img2 = Image.open(scanned_path)
    img2 = img2.resize((500,300))
    replaced2 = ImageTk.PhotoImage(img2)
    imageholder1.configure(image=replaced1)
    imageholder2.configure(image=replaced2)
    os.remove(f"C:/Users/thesc/Desktop/trashrecycler/runs/detect/exp/{image_name}")
    os.rmdir("C:/Users/thesc/Desktop/trashrecycler/runs/detect/exp")

def get_image():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    find_plastic(filename)
    

root = Tk()
root.title("Trash recycler")
root.geometry("1000x300")

image_loader = Button(root, height=1, width=5, bg="white", text="Search", anchor=CENTER, command=get_image)
image_loader.grid(row=0, column=0, columnspan=2)

placeholder = Image.open("placeholder.png")
placeholder = placeholder.resize((500,300))

img = ImageTk.PhotoImage(placeholder)

imageholder1 = Label(root, image=img)
imageholder1.grid(row=1, column=0)
imageholder2 = Label(root, image=img)
imageholder2.grid(row=1, column=1)

recycler = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
root.mainloop()
