CREATE TABLE
IF NOT EXISTS Users
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Password TEXT,
    Email TEXT,
    Body_Weight INTEGER,
    Body_Height INTEGER,
    Activity TEXT,
    Age INTEGER,
    Full_Logged TEXT
);

CREATE TABLE
IF NOT EXISTS Program_Users
(
    User_PROGRAM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    User_id INTEGER,
    Gender TEXT,
    Diet_Goal TEXT,
    Target_Weight INTEGER,
    Training_Days TEXT,
    Not_Active_Days TEXT,
    Intensity_Level TEXT,
    Experience TEXT,
    FOREIGN KEY
(User_id) REFERENCES Users
(ID)
);

CREATE TABLE
IF NOT EXISTS Program_Data
(
    Program_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    User_id INTEGER,
    BMR INTEGER,
    Calories TEXT,
    TDEE INTEGER,
    Program_Choice TEXT,
    FOREIGN KEY
(User_id) REFERENCES Users
(ID)
);

CREATE TABLE
IF NOT EXISTS userPlan
(
    Plan_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Calories_Plan TEXT,
    Exercise_Plan TEXT,
    FOREIGN KEY
(User_ID) REFERENCES Users
(ID)
);

CREATE TABLE
IF NOT EXISTS Meals
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    User_id INTEGER,
    Date DATETIME,
    Section TEXT,
    Meal TEXT,
    Proteins INTEGER,
    Carbs INTEGER,
    Fats INTEGER,
    Kcal INTEGER,
(User_id) REFERENCES Users
(ID)
)