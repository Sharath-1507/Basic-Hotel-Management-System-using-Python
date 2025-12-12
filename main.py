from tabulate import tabulate
# Creating a list to Store the Rooms

rooms = [{"Type":"single","Total":10,"Price":1500},{"Type":"double","Total":15,"Price":2500},{"Type":"suite","Total":5,"Price":5000}]
booking = []
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
    
    menu()

# Function to Make Reservations

def res():
    

    data = [["Single","1500",cra("single")],["Double","2500",cra("double")],["Suite","5000",cra("suite")]]
    header = ["Room Type","Price","Available Rooms"]
    print("Choose roon from the below option")
    print(tabulate(data, headers=header, tablefmt="grid"))
    print("")

    name = input("Enter your name:").lower()
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
    menu()
    


# res()
# cra("suite")
def canc():
    print(booking)
    canc_name = input("Enter your name:").lower()
    canc_rtype = input("Enter your room type:").lower()
    canc_days = int(input("Enter the Number of days you booked the room:"))

    for i in range(0,len(booking)):
        canc_dic = booking[i]
        if(canc_dic["Name"] == canc_name and canc_dic["Room"]==canc_rtype and canc_dic["Days"] == canc_days):
            print("Booking Succefully Canceled")
            booking.pop(i)
            print(booking)
            print("The Penalty for Cancelling the Reservation is:",canc_pen(canc_rtype,canc_days))
            exit()
        
    print("No Reservation found. Check the credentials agaain")
    menu()

# Function to Calculate the Penalty for Cancelling
def canc_pen(pen_type,pen_days):
    if(pen_type == "single"):
        return(pen_days * 100)
    elif(pen_type == "double"):
        return(pen_days * 250)
    elif(pen_type == "suite"):
        return(pen_days * 500)
    
    

# Creating a Menu 

def menu():
    print("Select an Action\n")

    menu_headers = ["Sl.No","Action"]
    menu_data = [["1","Check Room Availabilty"],["2","Make Reservations"],["3","Cancel Booking"],["4","Exit"]]

    print(tabulate(menu_data,headers=menu_headers,tablefmt="grid"))

    act = int(input("Enter the Sl.No of the action you wish to perform:"))

    if (act == 1):
        cra("all")

    elif (act == 2):
        res()
    elif (act == 3):
        canc()
    elif(act == 4):
        exit

menu()