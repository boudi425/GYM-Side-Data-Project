CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY  AUTOINCREMENT,
    Name TEXT,
    Password TEXT,
    Passkey TEXT,
    Body_Weight INTEGER,
    Body_Height INTEGER,
    Activity TEXT,
    Age INTEGER,
    Active TEXT
);