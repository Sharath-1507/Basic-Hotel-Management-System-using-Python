from tabulate import tabulate

# Creating a list to Store the Rooms

rooms = [{"Type":"single","Total":10,"Price":1500},{"Type":"double","Total":15,"Price":2500},{"Type":"suite","Total":3,"Price":5000}]
booking = []

# Function to Check Room Availabilty. cra--> Check Room Availabilty

def cra(cra_type):
    cra_single = rooms[0]
    cra_double = rooms[1]
    cra_suite = rooms[2]
    if(cra_type == "single"):
        
        if(cra_single["Total"]>0):

            return cra_single["Total"]


    elif(cra_type == "double"):
        
        if(cra_double["Total"]>0):
            return cra_double["Total"]

        
    elif(cra_type == "suite"):
        
        if(cra_suite["Total"]>0):
            # print("Rooms are Available")
            return cra_suite["Total"]
        # else:
        #     print("Rooms not Available.")
    elif(cra_type == "all"):
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
            booking.append({"Name":name,"Room":room_typ,"Days":room_dys})
            bill(name,room_typ,room_dys)
        else:
            print("All rooms occupied")

        
    elif(room_typ == "double"):
        res_double = rooms[1]
        if(res_double["Total"]>0):
            res_double["Total"] = res_double["Total"]-1
            booking.append({"Name":name,"Room":room_typ,"Days":room_dys})
            bill(name,room_typ,room_dys)
        else:
            print("All rooms occupied")
         
        
    elif(room_typ == "suite"):
        res_suite = rooms[2]
        if(res_suite["Total"]>0):
            res_suite["Total"] = res_suite["Total"]-1
            booking.append({"Name":name,"Room":room_typ,"Days":room_dys})
            bill(name,room_typ,room_dys)
        else:
            print("All rooms occupied")
        
    else:
        print("Enter a Valid Room Type")
        res()            
    

    menu()

# Function to Cancel Booking
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
            if(canc_rtype == "single"):
                canc_single = rooms[0]
                canc_single["Total"] = canc_single["Total"]+1
            elif(canc_rtype == "double"):
                canc_double = rooms[1]
                canc_double["Total"] = canc_double["Total"]+1
            elif(canc_rtype == "suite"):
                canc_suite = rooms[2]
                canc_suite["Total"] = canc_suite["Total"]+1
            menu()
            exit()

    print("No Reservation found. Check the credentials again")
    menu()

# Function to Calculate the Penalty for Cancelling
def canc_pen(pen_type,pen_days):
    if(pen_type == "single"):
        return(pen_days * 100)
    elif(pen_type == "double"):
        return(pen_days * 250)
    elif(pen_type == "suite"):
        return(pen_days * 500)
    

# Function for Billing
def bill(bill_name,bill_room,bill_days):
    if(bill_room == "single"):
        cost =  bill_days * 1500
    elif(bill_room == "double"):
        cost =  bill_days * 2500
    elif(bill_room == "suite"):
        cost = bill_days * 5000
       
    # Creating Table for Billing
    bill_data = [[bill_room,bill_days,cost],["Tax (18%)", "", cost*0.18],[ "Total Amount","" ,cost + (cost*0.18)]]
    bill_header = ["Room Type/Charges","Days","Amount (INR)"]
    print(tabulate(bill_data, headers=bill_header, tablefmt="grid"))

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
        print("Thank you for using the Hotel Management System")
        exit()
    else:
        print("Enter a Valid Action")
        menu()

menu()
