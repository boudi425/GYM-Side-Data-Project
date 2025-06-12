CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY  AUTOINCREMENT,
    Name TEXT,
    Password TEXT,
    Email TEXT,
    Body_Weight INTEGER,
    Body_Height INTEGER,
    Activity TEXT,
    Age INTEGER
);


CREATE TABLE IF NOT EXISTS Program_Users (
    User_PROGRAM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Gender TEXT,
    Diet_Goal TEXT,
    Target_Weight INTEGER,
    Training_Days TEXT,
    Not_Active_Days TEXT,
    Intensity_Level TEXT,
    Experience TEXT
);

CREATE TABLE IF NOT EXISTS Program_Data (
    Progam_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    BMR INTEGER,
    Calories TEXT,
    TDEE INTEGER,
    Program_Choice TEXT
);

