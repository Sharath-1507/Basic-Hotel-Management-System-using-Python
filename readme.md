# Hotel Booking System (Python)

A simple menu-driven hotel booking system built using core Python concepts.  
This project focuses on logic, data structures, and control flow without using databases, files, or object-oriented programming.

---

## About the Project

This is a console-based Hotel Management System where a user can:

- Check room availability
- Make a reservation
- Cancel a booking
- View billing details
- Return to the main menu after every action

All data is stored in memory while the program is running.  
Once the program exits, all booking data is lost. This is intentional.

---

## Concepts Used

This project strictly uses Python fundamentals:

- Strings
- Lists
- Dictionaries
- Functions
- Conditional statements

No databases  
No file handling  
No classes or OOP  

---

## Room Types and Pricing

| Room Type | Price per Day (INR) | Initial Availability |
|----------|--------------------|----------------------|
| Single   | 1500               | 1                    |
| Double   | 2500               | 15                   |
| Suite    | 5000               | 5                    |

---

## Features

### Check Room Availability
Displays all room types and their current availability in a table format.

### Make Reservation
- User selects a room type and number of days.
- Booking is allowed only if rooms are available.
- Room count decreases after a successful booking.
- Bill is generated immediately.

### Cancel Booking
- Booking is verified using name, room type, and number of days.
- Room availability is restored after cancellation.
- A cancellation penalty is applied based on room type.

### Menu-Based Navigation
- After every action, the user is returned to the main menu.
- The program runs continuously until the user chooses to exit.

---

## Billing and Cancellation Policy

### Billing
- Base cost = Room Price × Number of Days
- 18 percent tax is added
- Final bill is displayed in table format

### Cancellation Penalty

| Room Type | Penalty per Day (INR) |
|----------|-----------------------|
| Single   | 100                   |
| Double   | 250                   |
| Suite    | 500                   |

---

## How to Run the Project

1. Clone the repository: git@github.com:Sharath-1507/Basic-Hotel-Management-System-using-Python.git

2. Navigate to the project folder:

3. Install dependency: pip install tabulate

4. Run the program:


---

## Important Notes

- All bookings are stored in a Python list during runtime.
- Closing the program resets all data.
- The system is designed for internal use by staff/admin.
- This project is meant for learning purposes.

---

## Future Improvements

- File-based data storage (CSV or JSON)
- User authentication
- Dynamic room management
- Object-oriented refactoring

---

## Author

Sharath Chandra

---

This project was created to practice Python fundamentals and understand real-world logic in a simple system. :)