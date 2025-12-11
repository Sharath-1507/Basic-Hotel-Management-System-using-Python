from tabulate import tabulate
# Creating a list to Store the Rooms

rooms = [{"Type":"single","Total":10,"Price":1500},{"Type":"double","Total":15,"Price":2500},{"Type":"suite","Total":5,"Price":5000}]

# Function to Check Room Availabilty

def cra(type):
    cra_single = rooms[0]
    cra_double = rooms[1]
    cra_suite = rooms[2]
    if(type == "single"):
        
        if(cra_single["Total"]>0):
            # print("Rooms are Available")
            return cra_single["Total"]
        # else:
        #     print("Rooms not Available.")

    elif(type == "double"):
        
        if(cra_double["Total"]>0):
            # print("Rooms are Available")
            return cra_double["Total"]
        # else:
        #     print("Rooms not Available.")
        
    elif(type == "suite"):
        
        if(cra_suite["Total"]>0):
            # print("Rooms are Available")
            return cra_suite["Total"]
        # else:
        #     print("Rooms not Available.")
    elif(type == "all"):
        cra_tab_data = [["1","Single",cra_single["Total"]],["2","Double",cra_double["Total"]],["3","Suite",cra_suite["Total"]]]
        cra_tab_header = ["Sl.no","Room Type","Total Rooms"]
        print(tabulate(cra_tab_data, headers=cra_tab_header,tablefmt="grid"))

# Function to Make Reservations

def res():
    booking = []

    data = [["Single","1500",cra("single")],["Double","2500",cra("double")],["Suite","5000",cra("suite")]]
    header = ["Room Type","Price","Available Rooms"]
    print("Choose roon from the below option")
    print(tabulate(data, headers=header, tablefmt="grid"))
    print("")

    name = input("Enter your name:")
    room_typ = input("Enter the room you want:").lower()
    room_dys = int(input("Enter the Number of Days you want to Book:"))

    if(room_typ == "single"):
        res_single = rooms[0]
        if(res_single["Total"]>0):
            res_single["Total"] = res_single["Total"]-1

        

    elif(room_typ == "double"):
        res_double = rooms[1]
        if(res_double["Total"]>0):
            res_double["Total"] = res_double["Total"]-1
         
        
    elif(room_typ == "suite"):
        res_suite = rooms[2]
        if(res_suite["Total"]>0):
            res_suite["Total"] = res_suite["Total"]-1
        
    else:
        print("Enter a Valid Room Type")
        res()            

    booking.append({"Name":name,"Room":room_typ,"Days":room_dys})


# res()
# cra("suite")

# Creating a Menu 

def menu():
    print("Select an Action\n")

    menu_headers = ["Sl.No","Action"]
    menu_data = [["1","Check Room Availabilty"],["2","Make Reservations"],["3","Cancel Booking"]]

    print(tabulate(menu_data,headers=menu_headers,tablefmt="grid"))

    act = int(input("Enter the Sl.No of the action you wish to perform:"))

    if (act == 1):
        cra("all")

    elif (act == 2):
        res()


menu()