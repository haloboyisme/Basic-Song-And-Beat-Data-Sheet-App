import os
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import filedialog


# read the database location from a text file
with open("../music app try/settings.txt") as f:
    db_location = f.readlines()[2].strip()
    db_Name = db_location.split("/")[-1].split(".")[1]

def btn_clicked():
    # get the values from the Entry widgets
    songName_val = entry0.get()
    artistName_val = entry1.get()
    featName_val = entry2.get()
    writerSong_val = entry3.get()
    wavFile_val = entry4.get()
    coverImage_val = entry5.get()
    songStatus_val = entry6.get()
    extraImage_val = entry7.get()
    verison_val = entry8.get()
    extraNotes_val = entry9.get("1.0", "end-1c")


    # check if any entry is empty
    if not all([songName_val, artistName_val, featName_val, writerSong_val, wavFile_val, coverImage_val, songStatus_val, extraImage_val, verison_val, extraNotes_val]):
        messagebox.showerror("Error", "Please fill in all entries")
        return

    # check if the database exists
    if not os.path.exists(db_location):
        messagebox.showerror("Error", "Database not found. Please create a new database in settings")
        return

    # connect to the database
    conn = sqlite3.connect(db_location)
    c = conn.cursor()

    # add the values to the database
    try:
        c.execute("INSERT INTO users (artist_name, feat_name, writer, wav, cover_image, song_name, song_status, extra_img, verison, extra_notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (artistName_val, featName_val, writerSong_val, wavFile_val, coverImage_val, songName_val, songStatus_val, extraImage_val, verison_val, extraNotes_val))
        conn.commit()
        messagebox.showinfo("Success", "Data added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding data: {str(e)}")

    # close the connection
    conn.close()
    window.destroy()


 
def btn2_clicked():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("WAV files", "*.wav*"), ("all files", "*.*")))
    entry4.delete(0, END)
    entry4.insert(0, filename)
    print("Button Clicked2")

def btn3_clicked():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    entry5.delete(0, END)
    entry5.insert(0, filename)
    print("Button Clicked3")


def btn4_clicked():
    filenames = filedialog.askopenfilenames(initialdir = "/", title = "Select Zip Files", filetypes = (("Zip files", "*.zip"), ("All files", "*.*")), multiple = True)
    for filename in filenames:
        entry7.insert(END, filename + '\n')
    print("Button Clicked4")


    
def btn1_clicked():
    print("Close")
    window.destroy()

window = Tk()

window.geometry("1080x720")
window.configure(bg = "#65079e")
canvas = Canvas(
    window,
    bg = "#65079e",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"AddBeatPage/background.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"AddBeatPage/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 890, y = 459,
    width = 190,
    height = 74)

img1 = PhotoImage(file = f"AddBeatPage/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b1.place(
    x = 890, y = 556,
    width = 190,
    height = 74)

entry0_img = PhotoImage(file = f"AddBeatPage/img_textBox0.png")
entry0_bg = canvas.create_image(
    519.0, 110.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 296, y = 93,
    width = 446,
    height = 33)


entry1_img = PhotoImage(file = f"AddBeatPage/img_textBox1.png")
entry1_bg = canvas.create_image(
    519.0, 157.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 296, y = 140,
    width = 446,
    height = 33)

entry2_img = PhotoImage(file = f"AddBeatPage/img_textBox2.png")
entry2_bg = canvas.create_image(
    519.0, 206.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 296, y = 189,
    width = 446,
    height = 33)

entry3_img = PhotoImage(file = f"AddBeatPage/img_textBox3.png")
entry3_bg = canvas.create_image(
    519.0, 255.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 296, y = 238,
    width = 446,
    height = 33)

entry4_img = PhotoImage(file = f"AddBeatPage/img_textBox4.png")
entry4_bg = canvas.create_image(
    519.0, 304.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 296, y = 287,
    width = 446,
    height = 33)

img2 = PhotoImage(file = f"AddBeatPage/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = 748, y = 287,
    width = 136,
    height = 35)

entry5_img = PhotoImage(file = f"AddBeatPage/img_textBox5.png")
entry5_bg = canvas.create_image(
    519.0, 353.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 296, y = 336,
    width = 446,
    height = 33)

entry6_img = PhotoImage(file = f"AddBeatPage/img_textBox6.png")
entry6_bg = canvas.create_image(
    519.0, 402.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry6.place(
    x = 296, y = 385,
    width = 446,
    height = 33)

entry7_img = PhotoImage(file = f"AddBeatPage/img_textBox7.png")
entry7_bg = canvas.create_image(
    519.0, 452.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry7.place(
    x = 296, y = 435,
    width = 446,
    height = 33)

entry8_img = PhotoImage(file = f"AddBeatPage/img_textBox8.png")
entry8_bg = canvas.create_image(
    215.0, 687.0,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry8.place(
    x = 148, y = 672,
    width = 134,
    height = 28)

entry9_img = PhotoImage(file = f"AddBeatPage/img_textBox9.png")
entry9_bg = canvas.create_image(
    519.0, 593.0,
    image = entry9_img)

entry9 = Text(
    bd = 0,
    bg = "#ffffff",
    wrap="word",  # wrap text at word boundaries
    highlightthickness = 0)

entry9.place(
    x = 296, y = 484,
    width = 446,
    height = 216)

img3 = PhotoImage(file = f"AddBeatPage/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b3.place(
    x = 748, y = 336,
    width = 136,
    height = 35)

img4 = PhotoImage(file = f"AddBeatPage/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b4.place(
    x = 748, y = 435,
    width = 136,
    height = 35)

window.resizable(False, False)
window.mainloop()
