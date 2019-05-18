from PIL import ImageTk
from PIL import Image
from PIL import *
from tkinter import filedialog, Label, Menu, Tk, Entry, Button, Toplevel

def pixelate(image, pixel_size=9, draw_margin=False):
    #margin_color = (0, 0, 0)

    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    #pixel = image.load()

    ## Draw black margin between pixels
    #if draw_margin:
    #    for i in range(0, image.size[0], pixel_size):
    #        for j in range(0, image.size[1], pixel_size):
    #            for r in range(pixel_size):
    #                pixel[i+r, j] = margin_color
    #                pixel[i, j+r] = margin_color

    return image

def openfile():
    op = filedialog.askopenfilename(initialdir="C:/Users/MikeY/PycharmProjects/Pixel/image")
    window = Toplevel()
    window.title("Исходное изображение")
    window.geometry('1000x1000')
    image = Image.open(op)
    photo = ImageTk.PhotoImage(image)
    label = Label(window, image=photo)
    label.image = photo  # keep a reference!
    label.pack(expand="yes", fill="both", side="left")

def opentopixel():
    op = filedialog.askopenfilename(initialdir="C:/Users/MikeY/PycharmProjects/Pixel/image")
    window = Toplevel()
    window.title("Исходное изображение")
    window.geometry('1000x1000')
    image = Image.open(op).convert("RGB")
    i = counter()
    pixelPhoto = pixelate(image, pixel_size=i)
    pixelPhoto.save('image/output_{}.jpg'.format(i))
    photo = ImageTk.PhotoImage(pixelPhoto)
    label = Label(window, image=photo)
    label.image = photo  # keep a reference!
    label.pack(expand="yes", fill="both", side="left")

def counter():
    info = Field.get()
    data = int(info)
    return data

root = Tk()  # создать окно верхнего уровня приложения
root.title("Опорные точки")
m = Menu(root)  # создать объект Меню в главном окне
root.config(menu=m)  # сконфигурировать окно с указанием меню

Field = Entry(width=50)
Button = Button(text="Ввод порога", command = counter)
Field.pack()
Button.pack()

fm = Menu(m)  # создать пункт Меню с размещением в основном Меню (m)
m.add_cascade(label="Файл", menu=fm)  # пункт располагается в основном меню (m)
fm.add_command(label="Открыть", command=openfile)  # формируется команда открытия файла
fm.add_command(label="Пикселизировать", command=opentopixel)
fm.add_command(label="Закрыть", command=root.destroy)  # формируется команда выхода
root.mainloop()  # цикл обработки сообщений