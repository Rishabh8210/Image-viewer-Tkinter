from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image Viewer App")
root.geometry("900x550")
 
frame = tk.Frame(root)
frame.pack(pady=10)

img_1 = ImageTk.PhotoImage(Image.open("A.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("B.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("C.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("D.jpg"))
List_img = [img_1, img_2, img_3, img_4]

j = 0
img_label = Label(frame, image=List_img[j])
img_label.pack()


def next_img():
    global j
    j = j + 1
    try:
        img_label.config(image=List_img[j])
    except:
        j = -1
        next_img()


def prev():
    global j
    j = j - 1
    try:
        img_label.config(image=List_img[j])
    except:
        j = 0
        prev()


frame1 = tk.Frame(root)
frame1.pack(pady=5)
Prev = tk.Button(frame1, text="Previous", command=prev)
Prev.pack(side="left", padx=10)
Next = tk.Button(frame1, text="Next", command=next_img)
Next.pack(side="right", padx=10)

frame2 = tk.Frame(root)
frame2.pack(pady=5)
Exit = tk.Button(frame2, text="Exit", command=root.quit)
Exit.pack(side="bottom")

root.mainloop()