from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

h = 0
w = 0
scale = 0
position = (0, 0)


def browse_file():
    global h
    global w
    global scale
    global photo
    global new_pic
    file_path = filedialog.askopenfilename(initialdir='/',
                                           title='Select a Photo')

    new_pic = Image.open(file_path)

    h = new_pic.height
    w = new_pic.width
    scale = w/h

    if w > h:
        resized = new_pic.resize((int(1920/scale), int(1080/scale)), Image.LANCZOS)
    else:
        resized = new_pic.resize((int(270/scale), int(480/scale)), Image.LANCZOS)

    photo = ImageTk.PhotoImage(resized)
    image_label.config(image=photo)

    insert_btn.config(text='Insert Logo', command=insert_logo)


def insert_logo():
    global h
    global w
    global scale
    global new_logo
    global logo_photo
    global logo_label
    global logo_w_position
    global logo_h_position
    global logo_w
    global logo_h
    global position
    file_path = filedialog.askopenfilename(initialdir='/',
                                           title='Select a Logo')

    new_logo = Image.open(file_path)

    logo_w = int(w*20/100)
    logo_h = int(h*20/100)

    if w > h:

        if new_logo.width > new_logo.height:
            logo_w_position = int(1920 / scale) - int(1920 * 10 / 100)
            logo_h_position = int(1080 / scale) - int(1080 * 10 / 100)
            dimension = (int(1920*10/100), int(1080*10/100))
        else:
            logo_w_position = int(1920 / scale) - int(1080 * 10 / 100)
            logo_h_position = int(1080 / scale) - int(1920 * 10 / 100)
            dimension = (int(1080*10/100), int(1920*10/100))

    else:
        if new_logo.width < new_logo.height:
            logo_w_position = int(270 / scale) - int(675*10/100)
            logo_h_position = int(480 / scale) - int(1105*10/100)
            dimension = (int(675*10/100), int(1105*10/100))
        else:
            logo_w_position = int(270 / scale) - int(1105 * 10 / 100)
            logo_h_position = int(480 / scale) - int(675 * 10 / 100)
            dimension = (int(1105 * 10 / 100), int(675 * 10 / 100))

    resized_logo = new_logo.resize(dimension, Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(window, image=logo_photo)

    logo_label.place(x=logo_w_position, y=logo_h_position)

    insert_btn.destroy()
    right_top_btn.grid(column=1, row=2, pady=5)
    right_bottom_btn.grid(column=1, row=3, pady=5)
    left_top_btn.grid(column=2, row=2, pady=5)
    left_bottom_btn.grid(column=2, row=3, pady=5)
    save_btn.grid(columnspan=2, column=1, row=4)

    logo_label.place(x=logo_w_position, y=logo_h_position)
    if new_pic.width > new_pic.height and new_logo.width < new_logo.height:
        position = (w - logo_h, int(h - logo_h))
    elif new_pic.width > new_pic.height and new_logo.width > new_logo.height:
        position = (w - logo_w, int(h - logo_h))
    elif new_logo.width > new_logo.height:
        position = (w - logo_w, int(h - logo_h / 2))
    else:
        position = (w - logo_w, h - logo_h)
    return position


def right_top():
    global position
    logo_label.place(x=0, y=0)
    position = (0, 0)
    return position


def right_bottom():
    global position
    logo_label.place(x=0, y=logo_h_position)
    if new_pic.width > new_pic.height and new_logo.width < new_logo.height:
        position = (0, int(h - logo_h))
    elif new_pic.width > new_pic.height and new_logo.width > new_logo.height:
        position = (0, int(h - logo_h))
    elif new_logo.width > new_logo.height:
        position = (0, int(h-logo_h/2))
    else:
        position = (0, h-logo_h)
    return position


def left_top():
    global position
    logo_label.place(x=logo_w_position, y=0)
    if new_pic.width > new_pic.height and new_logo.width < new_logo.height:
        position = (w - int(logo_h), 0)
    else:
        position = (w - logo_w, 0)
    return position


def left_bottom():
    global position
    logo_label.place(x=logo_w_position, y=logo_h_position)
    if new_pic.width > new_pic.height and new_logo.width < new_logo.height:
        position = (w - logo_h, int(h - logo_h))
    elif new_pic.width > new_pic.height and new_logo.width > new_logo.height:
        position = (w - logo_w, int(h - logo_h))
    elif new_logo.width > new_logo.height:
        position = (w - logo_w, int(h-logo_h/2))
    else:
        position = (w - logo_w, h - logo_h)
    return position


def save():

    copied_image = new_pic.copy()
    crop_logo = new_logo.copy()
    size = (logo_w, logo_h)
    crop_logo.thumbnail(size)
    copied_image.paste(crop_logo, position)

    export_file_path = filedialog.asksaveasfilename(initialdir='Image_with_watermark', defaultextension='.png')
    copied_image.save(export_file_path)
    copied_image.show()


window = Tk()
window.title('Watermarking')
window.config(padx=50, pady=50)

logo_img = ImageTk.PhotoImage(file='logo.png')

image_label = Label(window, image=logo_img)
image_label.grid(column=1, row=0, columnspan=2)

insert_btn = Button(text='Insert Image', width=25, command=browse_file)
insert_btn.grid(column=1, row=1, columnspan=2)

right_top_btn = Button(text='Top Right', width=15, command=right_top)
right_bottom_btn = Button(text="Bottom Right", width=15, command=right_bottom)

left_top_btn = Button(text="Top Left", width=15, command=left_top)
left_bottom_btn = Button(text="Bottom Left", width=15, command=left_bottom)

save_btn = Button(text="Save", width=30, command=save)


window.mainloop()
