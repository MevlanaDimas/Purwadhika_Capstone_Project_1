from . import Database
import os

def input_data(ISBN,title,writter,year,publisher,availibility):
    data = Database.TEMPLATE.copy()

    data["ISBN"] = ISBN + Database.TEMPLATE["ISBN"][len(ISBN):]
    data["Title"] = title + Database.TEMPLATE["Title"][len(title):]
    data["Writter"] = writter + Database.TEMPLATE["Writter"][len(writter):]
    data["Year"] = year
    data["Publisher"] = publisher + Database.TEMPLATE["Publisher"][len(publisher):]
    data["Availibility"] = availibility + Database.TEMPLATE["Availibility"][len(availibility):]

    txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'

    try:
        with open(Database.DB_PATH,mode="w",encoding="utf-8") as file:
            file.write(txt_data)
            print("\nSuccesfully to save data")
    except:
        print("\nFailed to save data !!!")


def read_data(**kwargs):
    try:
        with open(Database.DB_PATH,'r') as file:
            content = file.readlines()
            total_books = len(content)

            if "index" in kwargs:
                books_index = kwargs["index"]-1
                if books_index < 0 or books_index > total_books:
                    return False
                else:
                    return content[books_index]
            else:
                return content
    except:
        print("Can't read database error !!!")
        return False
    

def add_data(ISBN,title,writter,year,publisher,availibility):
    data = Database.TEMPLATE.copy()

    data["ISBN"] = ISBN + Database.TEMPLATE["ISBN"][len(ISBN):]
    data["Title"] = title + Database.TEMPLATE["Title"][len(title):]
    data["Writter"] = writter + Database.TEMPLATE["Writter"][len(writter):]
    data["Year"] = year
    data["Publisher"] = publisher + Database.TEMPLATE["Publisher"][len(publisher):]
    data["Availibility"] = availibility + Database.TEMPLATE["Availibility"][len(availibility):]

    txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'

    try:
        with open(Database.DB_PATH,mode='a',encoding="utf-8") as file:
            file.write(txt_data)
            print("\nSuccesfully to save data")
    except:
        print("\nFailed to save data !!!")


def update(index,ISBN,title,writter,year,publisher,availibility):
    data = Database.TEMPLATE.copy()

    data["ISBN"] = ISBN + Database.TEMPLATE["ISBN"][len(ISBN):]
    data["Title"] = title + Database.TEMPLATE["Title"][len(title):]
    data["Writter"] = writter + Database.TEMPLATE["Writter"][len(writter):]
    data["Year"] = year
    data["Publisher"] = publisher + Database.TEMPLATE["Publisher"][len(publisher):]
    data["Availibility"] = availibility + Database.TEMPLATE["Availibility"][len(availibility):]



    if index == 0:
        txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'
        length_txt_data = len(txt_data)
        try:
            with(open(Database.DB_PATH,mode='r+',encoding="utf-8")) as file:
                file.seek(length_txt_data*(index))
                file.write(txt_data)
                print("\n\nSuccessfully to save data\n")
                
        except:
            print("\nFailed to save data !!!")
    
    if index == 1:
        txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}'
        length_txt_data = len(txt_data)
        try:
            with(open(Database.DB_PATH,mode='r+',encoding="utf-8")) as file:
                file.seek(length_txt_data*(index))
                file.write("\n"+txt_data)
                print("\n\nSuccessfully to save data\n")
                
        except:
            print("\nFailed to save data !!!")
    
    elif index == 2:
        txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'
        length_txt_data = len(txt_data)
        try:
            with(open(Database.DB_PATH,mode='r+',encoding="utf-8")) as file:
                file.seek(length_txt_data*(index))
                file.write("\n"+txt_data)
                print("\n\nSuccessfully to save data\n")
                
        except:
            print("\nFailed to save data !!!")

    elif index == 3:
        txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'
        length_txt_data = len(txt_data)
        try:
            with(open(Database.DB_PATH,mode='r+',encoding="utf-8")) as file:
                file.seek(length_txt_data*(index)+1)
                file.write("\n"+txt_data)
                print("\n\nSuccessfully to save data\n")
                
        except:
            print("\nFailed to save data !!!")
    
    elif index == 4:
        txt_data = f'{data["ISBN"]};{data["Title"]};{data["Writter"]};{data["Year"]};{data["Publisher"]};{data["Availibility"]}\n'
        length_txt_data = len(txt_data)
        try:
            with(open(Database.DB_PATH,mode='r+',encoding="utf-8")) as file:
                file.seek(length_txt_data*(index)+2)
                file.write("\n"+txt_data)
                print("\n\nSuccessfully to save data\n")
                
        except:
            print("\nFailed to save data !!!")



def delete(index):   
    try:
        data_file = read_data()
        
        with open(Database.DB_PATH,'w') as file:
            for ind,data in enumerate(data_file):
                if ind != index:
                    file.write(data)
                    print("\n\nSuccessfully to delete data\n")
                    break

    except:
        print("\n\nFailed to delete data\n")
        