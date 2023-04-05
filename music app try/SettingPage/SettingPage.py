from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import csv
import sqlite3
import os
#-------------------------------------------------------------------------#

def btn_clicked():
    backup_location = entry0.get()
    db_location = entry1.get()
    BeatDBLocation = entry2.get()

    if backup_location == "" or db_location == "" or BeatDBLocation == "":
        messagebox.showerror("Error", "Please fill out both fields.")
        return

    with open("settings.txt", "w") as f:
        f.write(backup_location + "\n" + db_location + "\n" + BeatDBLocation)

    messagebox.showinfo("Success", "Settings saved to file.")
    print("Settings saved to file.")
    window.destroy()

def btn1_clicked():
    print("Button Clicked2")
    window.destroy()

def btn2_clicked():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Folder selected:", folder_path)
        entry0.delete(0, END)  # clear any previous value in entry0
        entry0.insert(0, folder_path)  # insert the selected folder path
    else:
        print("No folder selected.")

def btn3_clicked():
    db_file = filedialog.askopenfilename(defaultextension=".db", filetypes=[('DB files', '*.db')])
    if db_file:
        entry1.delete(0, END)
        entry1.insert(0, db_file)
        print("DB file selected:", db_file)
        
        # Attempt to open and read the file
        try:
            with open(db_file, "r"):
                print("DB file opened successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        print("No DB file selected.")


def btn4_clicked():
    new_db_name = simpledialog.askstring("New Database Name", "Enter a name for your new database:")
    if new_db_name:
        program_dir = os.path.dirname(os.path.abspath(__file__))
        new_db_location = os.path.join(program_dir, new_db_name + ".db")
        print("New database file saved to:", new_db_location)
        
        

        # Create the database file and connect to it
        conn = sqlite3.connect(new_db_location)
        c = conn.cursor()
        
        # Create a table in the database
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, artist_name TEXT, feat_name TEXT, writer TEXT, wav TEXT, cover_image TEXT, song_name TEXT, song_status TEXT, extra_img TEXT, verison TEXT, extra_notes TEXT)''')
        
        # Insert data into the table
        c.execute("INSERT INTO users (artist_name, feat_name, writer, wav, cover_image, song_name, song_status, extra_img, verison, extra_notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ("Artist1", "Feat1", "Writer1", "Wav1", "Cover1", "Song1", "Status1", "ExtraImg1", "Version1", "Notes1"))
        

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        
        entry1.delete(0, 'end')
        entry1.insert(0, new_db_location)
    else:
        print("No new database file saved.")


def btn5_clicked():
    # Read the database file location from the settings file
    with open("settings.txt", "r") as f:
        backup_location = f.readline().strip()

    # Check if the backup location is valid
    if not backup_location:
        messagebox.showerror("Error", "Please provide a backup location in the settings file.")
        return

    db_location = entry1.get()

    if not db_location:
        messagebox.showerror("Error", "Please provide a database file location.")
        return

    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    for table_name in table_names:
        cursor.execute(f"SELECT * FROM {table_name[0]};")
        rows = cursor.fetchall()

        # Save the CSV file to the backup location specified in the settings file
        csv_file_path = os.path.join(backup_location, f"{table_name[0]}.csv")
        with open(csv_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Database converted to CSV.")
    print("Database converted to CSV.")


#-------------------------------------------------------------------------#

# Check if the settings.txt file exists
try:
    with open("settings.txt", "r") as f:
        # Read the first two lines of the file
        line0 = f.readline().strip()
        line1 = f.readline().strip()
        line2 = f.readline().strip()
except FileNotFoundError:
    # If the file doesn't exist, set the lines to empty strings
    line0 = ""
    line1 = ""

#-------------------------------------------------------------------------#

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

background_img = PhotoImage(file = f"SettingPage/background.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

canvas.create_text(
    148.0, 108.0,
    text = "Back-Up Location :",
    fill = "#ffffff",
    font = ("WorkSansRoman-Regular", int(15.0)))
#-------------------------------------------------------------------------#
img0 = PhotoImage(file = f"SettingPage/img0.png")
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
#-------------------------------------------------------------------------#
img1 = PhotoImage(file = f"SettingPage/img1.png")
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
#-------------------------------------------------------------------------#
entry0_img = PhotoImage(file = f"SettingPage/img_textBox0.png")
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
# Set the value of the Entry widget to the value of my_string
entry0.insert(0, line0)

#-------------------------------------------------------------------------#
img2 = PhotoImage(file = f"SettingPage/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = 748, y = 93,
    width = 136,
    height = 35)
#-------------------------------------------------------------------------#
canvas.create_text(
    148.0, 153.0,
    text = "Data-Base Location :",
    fill = "#ffffff",
    font = ("WorkSansRoman-Regular", int(15.0)))

canvas.create_text(
    148.0, 198.0,
    text = "Make a New Data-Base :",
    fill = "#ffffff",
    font = ("WorkSansRoman-Regular", int(15.0)))

canvas.create_text(
    148.0, 243.0,
    text = "Convert Data-Base to CSV :",
    fill = "#ffffff",
    font = ("WorkSansRoman-Regular", int(15.0)))
#-------------------------------------------------------------------------#
# create the label for the new textbox
label2 = Label(
    window,
    text="Second Database For Beats:",
    bg="#65079e",
    fg="white",
    font=("Arial", 14))
label2.place(x=100, y=300)

# create the new textbox
entry2 = Entry(
    window,
    bg="white",
    fg="black",
    font=("Arial", 12),
    width=50)
entry2.place(x=400, y=300)
entry2.insert(0, line2)
# create the "File" button for the new textbox
button2 = Button(
    window,
    text="File",
    bg="#65079e",
    fg="white",
    font=("Arial", 12),
    command=lambda: btn6_clicked(entry2))
button2.place(x=840, y=295)

def btn6_clicked(entry):
    file_path = filedialog.askopenfilename(defaultextension=".db", filetypes=[('DB files', '*.db')])
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)
        print("Database file selected:", file_path)
    else:
        print("No database file selected.")

entry1_img = PhotoImage(file = f"SettingPage/img_textBox1.png")
entry1_bg = canvas.create_image(
    519.0, 155.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 296, y = 138,
    width = 446,
    height = 33)
# Set the value of the Entry widget to the value of my_string
entry1.insert(0, line1)
#-------------------------------------------------------------------------#
img3 = PhotoImage(file = f"SettingPage/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b3.place(
    x = 748, y = 138,
    width = 136,
    height = 35)
#-------------------------------------------------------------------------#
img4 = PhotoImage(file = f"SettingPage/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b4.place(
    x = 296, y = 183,
    width = 136,
    height = 35)
#-------------------------------------------------------------------------#
img5 = PhotoImage(file = f"SettingPage/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn5_clicked,
    relief = "flat")

b5.place(
    x = 296, y = 225,
    width = 136,
    height = 35)


#-------------------------------------------------------------------------#
window.resizable(False, False)
window.mainloop()

