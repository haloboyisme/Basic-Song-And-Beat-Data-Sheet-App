from tkinter import *
import subprocess
from tkinter import *
from tkinter import messagebox
import pandas as pd
import sqlite3


#--------------------------------------------------------------------------------------#
# Define function that will execute on button click
def btn_clicked(): # Run AddSongPage.py script located in AddPage folder
    subprocess.call(["python", "AddBeatPage/AddBeatPage.py"])

    print("Button Clicked")


# Define function that will execute on button click 
def btn1_clicked():
    # Run AddSongPage.py script located in AddPage folder
    subprocess.call(["python", "AddPage/AddSongPage.py"])

# Define function that will execute on button click
def btn2_clicked():
    print("Close")
    window.destroy()


def btn3_clicked():
    # Run AddSongPage.py script located in AddPage folder
    subprocess.call(["python", "SettingPage/SettingPage.py"])

def btn4_clicked():
    subprocess.call(["python", "SongInfoSheet.py"])



def btn7_clicked():

    # Connect to the database and retrieve the latest data
    conn = sqlite3.connect(db_filename)
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()

    # Update the DataTable widget with the latest data
    empty_df = pd.DataFrame()
    table.updateModel(TableModel(empty_df))
    table.updateModel(TableModel(df))
    table.redraw()
    

def btn5_clicked():
    print("Button5 Clicked")

# Save the changes to the database
    conn = sqlite3.connect(db_filename)
    df = table.model.df
    df.to_sql("users", conn, if_exists="replace", index=False)
    conn.close()
    

def btn6_clicked():
    # Get the selected item from the DataTable widget
    selected_item = table.getSelectedRow()

    if selected_item is None:
        # If no item is selected, show an error message
        messagebox.showerror("Error", "No item selected")
    else:
        # Convert selected_item to a tuple or list if it's an integer
        if isinstance(selected_item, int):
            selected_item = (selected_item,)

        # If an item is selected, prompt the user to confirm the removal
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to remove this item?")

        if confirm:
            # If confirmed, remove the item from the database
            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE rowid = ?", (selected_item[0]+1,))
            conn.commit()
            conn.close()

            # Remove the item from the DataTable widget
            table.model.df.drop(selected_item[0], inplace=True)
            table.model.df.reset_index(drop=True, inplace=True)  # reset the index
            table.redraw()
            
            # Save the changes to the database
            conn = sqlite3.connect(db_filename)
            df = table.model.df
            df.to_sql("users", conn, if_exists="replace", index=False)
            conn.close()


 

#--------------------------------------------------------------------------------------#
# Create a Tkinter window object
window = Tk()

window.geometry("1080x720") # Set the size of the window
window.configure(bg = "#65079e")# Set the background color of the window

# Create a canvas on the window
canvas = Canvas(
    window,
    bg = "#65079e",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# Set the background image of the canvas

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

#--------------------------------------------------------------------------------------#

# Create a frame on the window to hold the song information
songFrame = Frame(
    window,
    highlightthickness=5,
    highlightbackground="black",
    height=645,
    width=445,
    bd=0,
    background="purple",
    relief="flat"
)
songFrame.place(x=0, y=75)

# Create a refresh button at the top left of the window
refresh_button = Button(
    window,
    text="Refresh",
    command=btn7_clicked,
    highlightthickness=0,
    relief="flat",
    bg="#65079e",
    fg="white",
    activebackground="#65079e",
    activeforeground="white",
    font=("Arial", 12, "bold")
)
refresh_button.place(x=10, y=10)

# Create a canvas inside the songFrame
canvas = Canvas(
    songFrame,
    bg="purple",
    bd=0,
    highlightthickness=0,
    width=445,
    height=645 - 10  # subtract scrollbar width
)
canvas.place(x=0, y=0)

# Add a scrollbar to the right side of the canvas
vscrollbar = Scrollbar(
    songFrame,
    orient=VERTICAL,
    command=canvas.yview
)
vscrollbar.place(x=445 - 10, y=0, height=645)

hscrollbar = Scrollbar(
    songFrame,
    orient=HORIZONTAL,
    command=canvas.xview
)
hscrollbar.place(x=0, y=645 - 10, width=445)

# Configure the canvas to use the scrollbars
canvas.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the song information
songInfoFrame = Frame(
    canvas,
    bg="purple",
    bd=0,
    highlightthickness=0
)
canvas.create_window((0, 0), window=songInfoFrame, anchor="nw", tags="songInfoFrame")

# Add your song information widgets to the songInfoFrame

# read database filename from settings file
try:
    with open('settings.txt') as f:
        settings = f.readlines()
    db_filename = settings[1].strip()
except FileNotFoundError as e:
    print(f"Error: {e}")
    db_filename = None

# connect to database and retrieve data
if db_filename:
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        result = cursor.fetchone()
        if not result:
            # table doesn't exist in the database, display error message
            messagebox.showerror("Error", "The database does not contain the required table 'users'")
            df = None
        else:
            # table exists, retrieve data
            df = pd.read_sql_query("SELECT * FROM users", conn)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        df = None
else:
    df = None

# create DataTable widget
if df is not None:
    from pandastable import Table, TableModel
    table = Table(songInfoFrame, dataframe=df, showtoolbar=False, showstatusbar=True)
    table.show()
    table.config(height=750)

# Update the canvas scroll region when the song information changes
songInfoFrame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


#--------------------------------------------------------------------------------------------------#

# Create a frame on the window to hold the beat information

beatFrame = Frame(
    window,
    highlightthickness = 5,  # set thickness to 1 to enable transparency
    highlightbackground = "black", #black line around the frame
    height = 645,
    width = 445,
    bd = 0,
    background="purple",
   
    relief = "flat")

beatFrame.place(x = 445, y = 75)

# Create a canvas inside the songFrame
canvas = Canvas(
    beatFrame,
    bg="purple",
    bd=0,
    highlightthickness=0,
    width=445,
    height=645 - 10  # subtract scrollbar width
)
canvas.place(x=0, y=0)

# Add a scrollbar to the right side of the canvas
scrollbar = Scrollbar(
    beatFrame,
    orient=VERTICAL,
    command=canvas.yview
)
scrollbar.place(x=445 - 10, y=0, height=645)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the song information
beatInfoFrame = Frame(
    canvas,
    bg="purple",
    bd=0,
    highlightthickness=0
)
canvas.create_window((0, 0), window=beatInfoFrame, anchor="nw", tags="songInfoFrame")

# Add your song information widgets to the songInfoFrame
# read database filename from settings file
try:
    with open('settings.txt') as f:
        settings = f.readlines()
    db_filename = settings[2].strip()
except FileNotFoundError as e:
    print(f"Error: {e}")
    db_filename = None

# connect to database and retrieve data
if db_filename:
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        result = cursor.fetchone()
        if not result:
            # table doesn't exist in the database, display error message
            messagebox.showerror("Error", "The database does not contain the required table 'users'")
            df = None
        else:
            # table exists, retrieve data
            df = pd.read_sql_query("SELECT * FROM users", conn)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        df = None
else:
    df = None

# create DataTable widget
if df is not None:
    from pandastable import Table, TableModel
    table = Table(beatInfoFrame, dataframe=df, showtoolbar=False, showstatusbar=True)
    table.show()
    table.config(height=750)

# Update the canvas scroll region when the song information changes
beatInfoFrame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))



#--------------------------------------------------------------------------------------#

# Create buttons for different actions with images

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b0.place(
    x = 890, y = 202,
    width = 190,
    height = 74)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 890, y = 276,
    width = 190,
    height = 74)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b2.place(
    x = 890, y = 350,
    width = 190,
    height = 74)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn5_clicked,
    relief = "flat")

b3.place(
    x = 890, y = 424,
    width = 190,
    height = 74)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn6_clicked,
    relief = "flat")

b4.place(
    x = 890, y = 498,
    width = 190,
    height = 74)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b5.place(
    x = 890, y = 572,
    width = 190,
    height = 74)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b6.place(
    x = 890, y = 646,
    width = 190,
    height = 74)


#--------------------------------------------------------------------------------------#

window.resizable(False, False) #set window to resizable

window.mainloop() #close the loop
