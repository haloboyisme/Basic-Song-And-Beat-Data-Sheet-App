import random
import string
import sqlite3

with open("../music app try/settings.txt") as f:
    db_location = f.readlines()[1].strip()
    db_Name = db_location.split("/")[-1].split(".")[0]

# Open a connection to the database
conn = sqlite3.connect(db_location)
cursor = conn.cursor()

# Repeat the process 25 times
for i in range(25):
    # Generate random values for each column
    id_val = i + 1
    artist_name_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    feat_name_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    writer_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    wav_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    cover_image_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    song_name_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    song_status_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    extra_img_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    version_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    extra_notes_val = ''.join(random.choices(string.ascii_uppercase, k=10))
    
    # Insert the values into the database
    cursor.execute(f"INSERT INTO users VALUES ({id_val}, '{artist_name_val}', '{feat_name_val}', '{writer_val}', '{wav_val}', '{cover_image_val}', '{song_name_val}', '{song_status_val}', '{extra_img_val}', '{version_val}', '{extra_notes_val}')")
    
    print("it show be in")
    # Commit the changes to the database
    conn.commit()

# Close the database connection
conn.close()
