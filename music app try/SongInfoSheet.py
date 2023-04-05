import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

# Ask the user for the database location
db_location = filedialog.askopenfilename(
    title="Select Database File",
    filetypes=(("SQLite databases", "*.db;*.sqlite"), ("All files", "*.*"))
)

# If the user cancels the file dialog, exit the program
if not db_location:
    messagebox.showinfo("Information", "No database file selected. Exiting.")
    exit()

# You can remove the code below that reads the database location from a text file
# with open("../music app try/settings.txt") as f:
#     db_location = f.readlines()[1].strip()

db_Name = db_location.split("/")[-1].split(".")[0]
print(db_Name)

# Connect to the database
conn = sqlite3.connect(db_location)
c = conn.cursor()


# Function to retrieve record from the database and display it in the main window
def display_record(record_id):
    c.execute('SELECT id, song_name, artist_name, feat_name, writer, wav, cover_image, song_status, verison, extra_notes, extra_img FROM users WHERE id=?', (record_id,))
    song = c.fetchone()

    if song:
        # Convert the cover image to a 250x250 thumbnail
        try:
            cover_img = Image.open(song[6])
            cover_img.thumbnail((250, 250))
            cover_photo = ImageTk.PhotoImage(cover_img)
        except:
            cover_photo = None
            print(f"Skipping song '{song[1]}' due to an error opening the cover image.")

        # Create a label to display the cover image
        cover_label = Label(songFrame, image=cover_photo)
        cover_label.image = cover_photo
        cover_label.pack(side=LEFT, padx=1, pady=1)

        # Create a label to display the song name
        song_name_label = Label(songFrame, text="Song Name: " + song[1])
        song_name_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the artist name
        artist_name_label = Label(songFrame, text="Artist Name: " + song[2])
        artist_name_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the feat_name
        feat_name_label = Label(songFrame, text="Feat. Name: " + song[3])
        feat_name_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the writer
        writer_label = Label(songFrame, text="Writer: " + song[4])
        writer_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the wav
        wav_label = Label(songFrame, text="WAV: " + song[5])
        wav_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the song status
        song_status_label = Label(songFrame, text="Song Status: " + song[7])
        song_status_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the version
        version_label = Label(songFrame, text="Version: " + song[8])
        version_label.pack(side=TOP, padx=1, pady=1)

        # Create a label to display the extra_notes
        extra_notes_label = Label(songFrame, text="Extra Notes: " + song[9])
        extra_notes_label.pack(side=TOP, padx=1, pady=1)

        
        

# Function to handle the "OK" button click in the popup dialog
def on_ok_button_click():
    record_id = id_entry.get()
    if record_id.isdigit():
        display_record(int(record_id))
        popup.destroy()
    else:
        messagebox.showerror("Error", "Please enter a valid record ID.")
# Create a new Tkinter window
window = Tk()




# Create a frame to hold the song information
songFrame = Frame(window, 
                  bg="purple",
                  bd=0,
                  highlightthickness=5,
                  highlightbackground="black"
                  )
songFrame.pack(fill=BOTH)




# Create a popup dialog to ask the user to enter a record ID
popup = Tk()
popup.title("Enter Record ID")
popup.geometry("350x150")

id_label = Label(popup, text="Record ID:")
id_label.pack()

id_entry = Entry(popup)
id_entry.pack()

ok_button = Button(popup, text="OK", command=on_ok_button_click)
ok_button.pack()

popup.mainloop()







# Start the Tkinter event loop
window.mainloop()

# Close the database connection
conn.close()
