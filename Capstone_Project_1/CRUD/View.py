from . import Operation


def create_first_console():
    print("\n\n"+"="*60)
    
    print("Please input data of the book\n")

    while(True):
        try:
            ISBN = input("ISBN\t\t: ")
            if len(ISBN) == 13:
                break
            else:
                print("ISBN length must be 13 numerical !!!")
                print("Please input the right ISBN")
        except:
            print("ISBN must be numerical")
    
    title = input("Title\t\t: ")
    
    writter = input("Writter\t\t: ")
    
    while(True):
        try:
            year = input("Year\t\t: ")
            if len(year) == 4:
                break
            else:
                print("Year length must be 4 (yyyy) !!!")
                print("Please input the right book year")
        except:
            print("Year must be numerical (yyyy)")
    
    publisher = input("Publisher\t: ")
    
    availibility = "Ada"

    Operation.input_data(ISBN,title,writter,year,publisher,availibility)


def read_all_console():
        data_file = Operation.read_data()

        ind = "No"
        IS = "ISBN"
        tit = "Title"
        writt = "Writter"
        yr = "Year"
        pub = "Publisher"
        avail = "Availibility"

        print("\n\n"+"="*197)
        print(f"{ind:4} | {IS:13} | {tit:50} | {writt:37} | {yr:4} | {pub:30} | {avail:3}")
        print("-"*197)
        
        for index,data in enumerate(data_file):
            data_break = data.split(";")
            
            ISBN = data_break[0]
            title = data_break[1]
            writter = data_break[2]
            year = data_break[3]
            publisher = data_break[4]
            availibility = data_break[5]
            print(f"{index+1:4} | {ISBN:13} | {title:.50} | {writter:.37} | {year:4} | {publisher:.30} | {availibility:3}",end="")

        print("="*197+"\n")


def read_ISBN_console():
        data_file = Operation.read_data()

        ind = "No"
        IS = "ISBN"
        tit = "Title"
        writt = "Writter"
        yr = "Year"
        pub = "Publisher"
        avail = "Availibility"

        print("\n"+"="*60)
        
        search_ISBN = input("\nPelase input the book ISBN: ")

        for index,data in enumerate(data_file):
            data_break = data.split(";")
                    
            ISBN = data_break[0]
            title = data_break[1]
            writter = data_break[2]
            year = data_break[3]
            publisher = data_break[4]
            availibility = data_break[5]
            
            if len(search_ISBN) == 13 and search_ISBN == ISBN:
                print("\n\n"+"="*197)
                print(f"{ind:4} | {IS:13} | {tit:50} | {writt:37} | {yr:4} | {pub:30} | {avail:3}")
                print("-"*197)

                print(f"{index+1:4} | {ISBN:13} | {title:.50} | {writter:.37} | {year:4} | {publisher:.30} | {availibility:.3}",end="")
                print('\n')
                print("="*197+"\n\n\n")
                break
            elif search_ISBN != ISBN:
                print("\nPlease insert the right ISBN !!!")
                continue
        
        
            
def add_console():
    
    print("Please input data of the book\n")

    while(True):
        try:
            ISBN = input("ISBN\t\t: ")
            if len(ISBN) == 13:
                break
            else:
                print("ISBN length must be 13 numerical !!!")
                print("Please input the right ISBN")
        except:
            print("ISBN must be numerical")
    
    title = input("Title\t\t: ")
    
    writter = input("Writter\t\t: ")
    
    while(True):
        try:
            year = input("Year\t\t: ")
            if len(year) == 4:
                break
            else:
                print("Year length must be 4 (yyyy) !!!")
                print("Please input the right book year")
        except:
            print("Year must be numerical (yyyy)")
    
    publisher = input("Publisher\t: ")
    
    availibility = "Ada"

    Operation.add_data(ISBN,title,writter,year,publisher,availibility)
    print("\n\n")
    read_all_console()


def edit_console():
    read_all_console()


    data_file = Operation.read_data()


    search_ISBN = input("\nPelase input the book ISBN you want to edit: ")    
                            
    for index,data in enumerate(data_file):
        data_break = data.split(";")
                                        
        ISBN = data_break[0]
        title = data_break[1]
        writter = data_break[2]
        year = data_break[3]
        publisher = data_break[4]
        availibility = data_break[5][:-1]

        if len(search_ISBN) == 13 and search_ISBN == ISBN:
            while(True):
                print(f'''Please select the data of the book you want to edit:
1. ISBN\t\t: {ISBN:13}
2. Title\t: {title:.50}
3. Writter\t: {writter:.37}
4. Year\t\t: {year:4}
5. Publisher\t: {publisher:.30}
6. Availibility\t: {availibility:.8}
''')
                edit_option = input("Please select [1-6]: ")

                match edit_option:
                    case "1": 
                        while(True):
                            try:
                                ISBN = input("ISBN\t\t: ")
                                if len(ISBN) == 13:
                                    break
                                else:
                                    print("The length of ISBN book must be 13 numerical !!!")
                            except:
                                print("Please input ISBN with length 13 and numerical !!!")
                    case "2": title = input("Title\t: ")
                    case "3": writter = input("Writter\t: ")
                    case "4": 
                        while(True):
                            try:
                                year = input("Year\t: ")
                                if len(year) == 4:
                                    break
                                else:
                                    ("Year length must be 4 (yyyy) !!!")
                                    print("Please input the right book year")
                            except:
                                print("Year must be numerical (yyyy)")
                    case "5": publisher = input("Publisher\t: ")
                    case "6": 
                        while(True):
                            try:
                                availibility = input("Availibility\t: ")
                                if availibility == 'Ada':
                                    break
                                elif availibility == 'Tdk':
                                    break
                                else:
                                    print("Can only select [Ada/Tdk] !!!")
                            except:
                                print("Pelase select [Ada/Tdk] !!!")
                    case _: print("Please select only [1-6] !!!")
                
                is_done = input("Is the new data is correct [y/n]: ")
        
                match is_done:
                    case 'y':
                        break
                    case'n':
                        continue
            break
               
        
    Operation.update(index,ISBN,title,writter,year,publisher,availibility)
        
    read_all_console()


def delete_console():
    read_all_console()
    
    ind = "No"
    IS = "ISBN"
    tit = "Title"
    writt = "Writter"
    yr = "Year"
    pub = "Publisher"
    avail = "Availibility"

    data_file = Operation.read_data()


    search_ISBN = input("\nPelase input the book ISBN you want to delete: ")    
                            
    for index,data in enumerate(data_file):
        data_break = data.split(";")
                                        
        ISBN = data_break[0]
        title = data_break[1]
        writter = data_break[2]
        year = data_break[3]
        publisher = data_break[4]
        availibility = data_break[5][:-1]

        if len(search_ISBN) == 13 and search_ISBN == ISBN:
            print("\n\n"+"="*197)
            print(f"{ind:4} | {IS:13} | {tit:50} | {writt:37} | {yr:4} | {pub:30} | {avail:3}")
            print("-"*197)

            print(f"{index+1:4} | {ISBN:13} | {title:.50} | {writter:.37} | {year:4} | {publisher:.30} | {availibility:.3}",end="")
            print('\n')
            print("="*197+"\n\n\n")

            while(True):

                delete_option = input("Are you sure to delete this [y/n]: ")

                match delete_option:
                    case 'y': 
                        Operation.delete(index)
                        break
                    case 'n': break
            break
            
    print("\nData has been successed deleted")
