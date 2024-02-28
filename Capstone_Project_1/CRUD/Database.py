from . import Operation
from . import View

DB_PATH = "D:/Bootcamp/Tugas/Capstone_Project_1/data.txt"

TEMPLATE = {
    "ISBN": "xxxxxxxxxxxxx",
    "Title": 100*" ",
    "Writter": 50*" ",
    "Year": "yyyy",
    "Publisher": 50*" ",
    "Availibility": 3*" "

}

def init_console():
    try:
        with open(DB_PATH,"r") as file:
            print("Database is available !")

    except:
        print("Database is not available !")
        print("\nPlease make a new database:")
        View.create_first_console()