CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY  AUTOINCREMENT,
    Name TEXT,
    Password TEXT,
    Email TEXT,
    Body_Weight INTEGER,
    Body_Height INTEGER,
    Activity TEXT,
    Age INTEGER,
);

CREATE TABLE IF NOT EXISTS Program_Users (
    PROGRAM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Gender TEXT,
    Diet_Goal TEXT,
    Target_Weight INTEGER,
    Training_Days TEXT,
    Active_Days TEXT,
    Intensity_Level TEXT,
    Experience TEXT,
    FOREIGN KEY (ID) REFERENCES Users(ID)
);

