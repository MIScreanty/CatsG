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
    tag = e.get()
    new_url_tag = f"https://cataas.com/cat/{tag}" if tag else f"https://cataas.com/cat"
    img = get_cat(new_url_tag)
    if img:
        new_win = Toplevel()
        t_m = Label(new_win, image=img)
        t_m.image = img
        t_m.pack()
        #t_m.config(image=img)
        #t_m.image = img

def close_window():
    window.destroy()

window = Tk()
window.title("Caats")
window.geometry(f"500x440+{window.winfo_screenwidth()//2-250}+{window.winfo_screenheight()//2-220}")
window.iconbitmap("cat_icon_138789.ico")

#исправим код чтобы получать котов в новом окне
#t_m = Label(window)
#t_m.pack()

#сделаем меню вместо кнопки
#btn = Button(window, text="Get new cat", command=get_new_cat)
#btn.pack()

#ввод тэга
e = Entry()
e.pack()

#Создаем меню
main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Get cat", command=get_new_cat)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_window)

window.mainloop()