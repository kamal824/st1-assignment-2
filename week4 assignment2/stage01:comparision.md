Part -E

Human vs AI Comparison 



Question	Human version	AI version
Easy to understand?	The code has basic lists and the dictionaries taught in the unit 	The code made by AI is also simple but I need to test it before using it.
Runs successfully?	Yes, the code rum successfully 	Yes the code run successfully but needs to be made some changes.
Uses only required features?	The code stores the patient records and their appointment details using basic technology 	The code made by AI does not introduce to database or SQL.
Adds assumptions?	Assumptions are made in the details or the record of appointments like the time and name 	The AI may make assumptions about validation, data format or how appointments should be stored.
Handles errors?	It checks that the patient’s name is not empty, but it does not handle all possible invalid inputs.	The amount of error handling depends on what the AI generated. It must be tested rather than assumed to work.
Could I explain it?	Yes. I understand the list, dictionaries, function and appointment data.	I could explain the code after reviewing and testing it, but I would not use code that I did not understand.

Five Limitations of the Human Prototype
1.	Appointments record made in the system is not stored permanently 
2.	There are chances of the double booking at a single time by two different patients to the same practitioner the system does not prevent it 
3.	There is no proper format for the data entered by the patient to book the appointment 
4.	There can be empty fields while entering the data from the patients during booking of appointment 
5.	There is no login option available to the patient to check their booking time again.

Overall Comparison
The human-written version was useful because the code has represented every part of the code very properly which make the code simple and easy to understand. The code made by AI was also good as AI provides the different types of ways or alternatives to present the code but the code made by AI needs to be tested properly before using it, there is no guarantee in the code made by AI that it meets the requirements of the clients  so the code is needed to be make changes in it to fulfill the clients requirements. 




Part G – Improve One Thing


I chose to improve the format of the input for the patient’s name. The original function could accept an empty patient name, which would result in an incomplete appointment record so I made a change in the function to show the error if the patient’s name is empty .
below is the function I have added:
“If not patient_name:
    raise ValueError ("Patient name cannot be empty")”
I tested the improvement using an empty patient name. The program correctly and function raised an error if the name of the patient column is empty 
.
