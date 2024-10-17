import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

def get_cat(url):
    info_image = requests.get(url)
    image = BytesIO(info_image.content)
    img = Image.open(image)
    img.thumbnail((500,400))
    img_tk = ImageTk.PhotoImage(img)
    return img_tk

def get_new_cat():
    img = get_cat(url)
    if img:
        t_m.config(image=img)
        t_m.image = img


window = Tk()
window.title("Caats")
window.geometry(f"500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}")
window.iconbitmap("cat_icon_138789.ico")

url = "https://cataas.com/cat"

t_m = Label(window)
t_m.pack()

btn = Button(window, text="Get new cat", command=get_new_cat)
btn.pack()

window.mainloop()