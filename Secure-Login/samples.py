import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """
)

username1, password1 = (
    "mike213",
    hashlib.sha256("mikepassword".encode("utf-8")).hexdigest(),
)
username2, password2 = (
    "john",
    hashlib.sha256("micatisgreat777".encode("utf-8")).hexdigest(),
)username3, password3 = (
    "striker999",
    hashlib.sha256("ILikeStriking".encode("utf-8")).hexdigest(),
)username4, password4 = (
    "philipef",
    hashlib.sha256("philipefpassword".encode("utf-8")).hexdigest(),
)
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
# print(password1) --> c3d1521637ed895bcac0a4fed2cf9bfc9a162335138553c393899141d0bc9bc6
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
