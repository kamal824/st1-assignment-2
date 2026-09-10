Part - C

Explain what the code does step by step.
Identify three limitations.
Suggest improvements.
Avoid rewriting the whole application.
Ask you two questions to test your understanding.

In the meantime, here are two introductory Python questions:

What is the difference between a variable and a function?
Why might a program need to check whether user input is valid before processing it?
I'll explain the code, point out limitations, suggest improvements, and then test your understanding with two questions.

1. What the code does

The program simulates a simple appointment booking system for a community clinic called SmartCare.

Part 1: Hard-coded appointments
Python
1
patient1_name = "Alice Smith"
2
practitioner1_name = "Dr. John Doe"
3
appointment1_time = "2024-07-20 10:00 AM"
Show more lines

This creates variables to store details for the first appointment.

Python
1
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
Show more lines

This uses an f-string to display the appointment information.

The same process is repeated for a second appointment:

Python
1
patient2_name = "Bob Johnson"
2
practitioner2_name = "Dr. Jane Roe"
3
appointment2_time = "2024-07-20 11:30 AM"
Show more lines
Part 2: Improved appointment system

An empty list is created:

Python
1
appointments = []
Show more lines

This list will store all appointments.

The book_appointment() function
Python
1
def book_appointment(patient_name, practitioner_name, appointment_time):
Show more lines

This function accepts three pieces of information:

Patient name
Practitioner name
Appointment time

It performs a simple validation:

Python
1
if not patient_name:
2
raise ValueError("Patient name cannot be empty")
Show more lines

If the patient name is missing, the function raises an error.

Next, a dictionary is created:

Python
1
appointment = {
2
"patient": patient_name,
3
"practitioner": practitioner_name,
4
"time": appointment_time
5
}
6
``
Show more lines

The dictionary stores appointment details as key-value pairs.

The appointment is then added to the list:

Python
1
appointments.append(appointment)
Show more lines
The display_appointments() function
Python
1
def display_appointments():
Show more lines

This function displays all stored appointments.

First it checks if the list is empty:

Python
1
if not appointments:
2
print("No appointments recorded.")
Show more lines

If there are no appointments, an informative message is displayed.

Otherwise, it loops through each appointment:

Python
1
for appointment in appointments:
Show more lines

and prints the details.

Program execution

The code books two appointments:

Python
1
book_appointment(...)
2
book_appointment(...)
Show more lines

Finally:

Python
1
display_appointments()
Show more lines

prints all stored appointments.

2. Three limitations
1. Limited input validation

Only the patient name is checked.

For example, these would still be accepted:

Python
1
book_appointment("Alice", "", "")
2
``
Show more lines

There is no validation for:

Practitioner name
Appointment time format
Invalid or misspelled values
2. No duplicate booking checks

The system allows multiple appointments at the same time.

Example:

Python
1
book_appointment("Alice", "Dr. John Doe", "2024-07-20 10:00 AM")
2
book_appointment("Bob", "Dr. John Doe", "2024-07-20 10:00 AM")
Show more lines

This creates a scheduling conflict.

3. Data is not saved permanently

Appointments exist only while the program runs.

When the program closes:

Python
1
appointments = []
Show more lines

is recreated and all stored bookings are lost.

3. Suggested improvements
Improvement 1: Validate all inputs

Check that:

Patient name is not empty
Practitioner name is not empty
Appointment time follows a valid date/time format

This reduces incorrect data entry.

Improvement 2: Prevent scheduling conflicts

Before adding an appointment, check whether the practitioner already has an appointment at that time.

This would make the booking system more realistic.

Improvement 3: Store data permanently

Save appointments to a file or database so that bookings remain available after the program is closed and reopened.

Improvement 4: Add appointment management features

Possible extensions include:

Search appointments
Cancel appointments
Update appointment times
Sort appointments by date and time
Improvement 5: Use date/time objects

Instead of storing dates as strings:

Python
1
"2024-07-20 10:00 AM"
Show more lines

use Python's datetime module. This makes it easier to:

Compare times
Sort appointments
Detect overlaps
4. Overall assessment

This is a good introductory example because it demonstrates several important Python concepts:

Variables
Lists
Dictionaries
Functions
Input validation
Loops
f-strings

The second version is much better than the first because it avoids repeating code and can store any number of appointments.

5. Questions to test your understanding
Question 1

Why is a list of dictionaries a better design for storing appointments than creating variables such as:

Python
1
patient1_name
2
patient2_name
3
patient3_name
Show more lines

for every new appointment?

Question 2

What is the purpose of this statement?

Python
1
appointments.append(appointment)
Show more lines

What would happen if this line were removed from the book_appointment() function?



Part - D
 

 def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    
    return appointment


# Example usage
appointment1 = book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)

print(appointment1)