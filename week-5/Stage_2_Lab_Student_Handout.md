Week – 5


## Part A – Client Brief: AI OFF


SmartCare Client Brief
SmartCare currently uses spreadsheets and paper records to manage its record of patients and the practitioners. 
The Client has been facing several problems and expect the system to get rid of the following problems below:
•	Duplication of the records or the information like patient bookings or the schedule of the practitioners 
•	Patient appointments are properly booked with constituency 
•	Hard to maintain or keep the track of the patient records 
•	There is no proper space to record or maintain the recent patient information like the recent appointments

Client wants a fast, easy, maintainable system for there 
•	Patients
•	Appointments
•	Practitioners
•	Schedule of practitioners 

Initial Problem Statement
The existing system makes it hard for the staff to keep the track of the record of the patients as well it also creates a lot of errors like not having a valid format or duplication of the data. The proposed SmartCare system should make the easy management of patient appointments bookings, Easy practitioner and appointment records while reducing duplicate bookings and inconsistent appointment information.


Evidence Of the Client Needs 
The following data below is directly supported by the client brief:
Patient management, practitioner management, appointment management, reducing duplicate bookings, improving access to patient information, consistent appointment status, appointment history, and maintainability.


## Part B – Stakeholders and Scope: AI OFF

Stakeholders
Stakeholder	Role / Interest	Evidence
Patients	The patient record and there appointments details should be stored in the system 	The requires storing patient details in brief 
Practitioners	Need access to their schedules and the information of the patient’s appointments	The system is designed to maintain the practitioner and the patient information relevantly.
Management	Wants an easy maintainable system that also resolves the clients’ problems 	Explicitly stated in the client brief.
Reception/Admin Staff	Efficient managing of the client’s record 	Staff have reported their problems in brief 
System Administrator	Maintaining the system 	the brief does not explicitly identify this role.

In Scope
•	Building up the Patients records 
•	keeping track of patient information
•	Managing practitioner records
•	Creating appointments
•	Viewing appointments
•	Preventing duplicate bookings
•	Updating appointment status
•	Viewing appointment history
•	Maintaining consistent appointment information

Out of Scope
The following are outside the current confirmed scope:
•	Health diagnosis 
•	Decision making about the hospital or clinic 
•	Online services to provide to patients 
•	External healthcare-system integration
•	Advanced analytics
•	Recommendation about the future projects or any sort of recommendation
Provisional / To Be Confirmed
These features have not been confirmed by the client:
•	Whom to be provided access to the data and at what stage of access to be provided 
•	Online or by email appointment booking 
•	Confirmation of booking to be send to practitioner 
•	Dedicated system administrator functionality



## Part C – Functional Requirements

Each requirement describes one observable system capability.
ID	Functional Requirement
FR-01	The system should allow the staff to book an appointment.
FR-02	The system should allow the staff to keep the track of the record 
FR-03	The system should allow the staff to make changes to the data of patients.
FR-04	The system should allow the staff to create the practitioner data about their schedules and allow them to make changes in the data 
FR-05	The system shall allow authorised staff to book an appointment for the patient at the specific time or date as per patient and practitioners availability 
FR-06	The system should allow the staff to cancel the appointments if there is any change in the practitioner’s schedule or availability or there are two patients booked at same time 
FR-07	The system should allow the staff to maintain and update the schedule of the practitioner
FR-08	The system should allow the staff to make changes or update the appointments specifications at every stage
FR-09	The system shall allow authorised staff to view the appointment history associated with a patient.
FR-10	The system shall store appointment details, including the patient, practitioner, date, time and status, so they can be retrieved after being saved.
 





## Part D – Non-Functional Requirements


ID	Category	Non-Functional Requirement
NFR             -01	Usability	The system should allow the staff members to keep the track of record of patients and can have access to the patient data just by searching their name rather than using any database tools 
NFR-02	Data Integrity	The system should prevent creating the duplicate data record of patient 
NFR-03	Reliability	The system should store the data or information of the patient or partitioners in the system for the future use 
NFR-04	Maintainability	The system should allow the staff to create the change in the data or modify the data rather than just redesigning the whole system
NFR-05	Testability	The system shall produce predictable results for patient searches, appointment creation and appointment-status 
NFR-06	Data Consistency	The system shall use consistent appointment-status values throughout the system.


## Part E – User Stories and Acceptance Criteria
User Story 1 –Booking an Appointment
As a reception staff member, I want to book an appointment for a patient with a practitioner 
Acceptance Criteria
Scenario 1 – Appointment successfully created
•	Given the patient and practitioner exist
•	And the selected appointment time is available
•	When the staff member creates the appointment the appointment is saved with the patient, practitioner, date and time.
Scenario 2 – Duplicate booking
•	Given the practitioner already has an appointment at the selected date and time
•	When the staff member attempts to create another appointment Then the system prevents the duplicate appointment from being saved by giving the message or warning.
 


User Story 2 – Find Patient Information
As a reception staff member, I want to search for a patient record so that I can quickly access the patient’s information.
Acceptance Criteria
Scenario 1 – Patient found
•	The given patient record was there in the system 
•	When staff member searched for the patient, the record was found 
Scenario 2 – Patient not found
•	There was no patient record found in the system 
•	When the staff member searches for the patient record the system does not give any output for the required patient 


User Story 3 – Update Appointment Status
As a staff member I want to update the appointment details.
Acceptance Criteria
Scenario 1 – Valid status
•	The appointment exists in which the changes were need to make 
•	When the staff member try to make changes the system note the changes to be made and update the changes in the system .
Scenario 2 – Invalid status
•	Appointment exists in which the changes need to be made 
•	When the staff member tries to make changes the system shows invalid status and there were no changes updated in the system 

User Story 4 – View Appointment History
As a practitioner I want to check the patient’s history 
Acceptance Criteria
Scenario 1 – History exists
•	The patient has old past appointments in the system 
•	When the practitioner views the patient’s appointment history the system displays the recorded appointments and their statuses.
Scenario 2 – No history
•	The patient has no old appointment record 
•	When the practitioner views the appointment history then the system indicates that no appointment history is available.






## Part F – AI Requirements Review
The AI was instructed:
“Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.”



AI Review Findings
#	AI Suggestion	Type	Reason
1	Define what information is required when creating a patient record.	Question requiring validation	The brief says the system manages patients but does not specify the required patient fields.
2	Define the approved appointment-status values.	Question requiring validation	The brief identifies inconsistent appointment status but does not state which statuses should exist.
3	Clarify whether two appointments at the same time are prohibited for all practitioners or only in specific circumstances.	Question requiring validation	The brief reports duplicate bookings but does not define the exact duplicate-booking rule.
4	Clarify whether appointment times can overlap partially or only when they have exactly the same start time.	Question requiring validation	The brief does not specify appointment duration or overlap rules.
5	Define how patient records are uniquely identified to avoid duplicates.	Question requiring validation	The brief says duplicate bookings are a problem, but does not define the patient-identification method.
6	Define what “maintainable” means in measurable/testable terms.	Evidence-based observation + question	Maintainability is explicitly requested, but the client has not provided measurable criteria.
7	Define how quickly patient searches should return results.	Question requiring validation	Searchability is supported by the problem brief, but no performance target is provided.
8	Clarify who is authorised to create or modify records.	Question requiring validation	The requirements use “authorised staff”, but the client brief does not define user roles or permissions.
9	Avoid assuming that patients will have direct system access.	Evidence-based	The brief does not state that patients will use the system directly.
10	Avoid adding SMS reminders, mobile apps, billing or external integrations as requirements.	Evidence-based	These features are not stated in the client brief and therefore should not be invented.
11	FR-06 should clarify whether the duplicate-booking rule applies to the same practitioner only or all appointments.	Question requiring validation	The client identifies duplicate bookings as a problem but does not define the exact business rule.
12	NFRs should be measurable where possible.	Evidence-based	Testability requires criteria that can be verified, but the brief does not provide numerical targets.
 


## Part G – Verify the AI Review
The AI reviews were checked with the needs to the clients and after crosschecking the AI and the client’s needs the test was passed 
AI Suggestion	Decision	Evidence / Reason
Define Patient Information 	Accepted	As per client the system was expected to maintain the client records but there was no brief provided about what sort of data of patient record to be maintained.
Define appointment-status values.	Accepted	The brief explicitly identifies inconsistent appointment status as a problem.
Clarify duplicate-booking rules.	Accepted	There is problem identified for the duplicate bookings 
Clarify overlapping appointment rules.	Unverified	There is no data about the duration of the appointment the overlap between the appointments 
Define patient unique identifier.	Accepted	There is need of client confirmation for addressing the duplicate information 
Make “maintainable” measurable.	Accepted	Maintainability is explicitly requested, but no measurable definition is provided.
Define search response time.	Unverified	Difficulty finding information is confirmed, but no performance target is given.
Define authorised users.	Accepted	The requirements refer to authorised staff, but specific roles/permissions have not been confirmed.
Do not assume patient direct access.	Accepted	Patient system management is in scope, but direct patient access is not stated.
Do not add SMS/mobile/billing/integration features.	Accepted	These are not mentioned in the client’s brief .
Clarify scope of duplicate-booking prevention.	Accepted	The problem is confirmed, but the precise business rule requires validation.
Verification Principle
The AI Suggestions that identified ambiguity in existing requirements were useful, Suggestions that would require introducing new functionality were not automatically accepted.









## Part H – SmartCare Requirements Specification v0.2
1. Purpose
SmartCare is expected. to replace the old spreadsheets method to maintain the data and create a easy maintainable and fast system to run the smart care system 
2. Problems
The system should address the following problems identified by staff:
1.	Duplicate bookings
2.	Difficulty finding patient information
3.	Limited appointment history
4.	Improper format of the appointments data 
3. Stakeholders
•	Reception/Admin Staff
•	Practitioners
•	Patients
•	Management
•	System Administrator – provisional
4. Scope
In Scope
•	Building up the Patients records 
•	keeping track of patient information
•	Managing practitioner records
•	Creating appointments
•	Viewing appointments
•	Preventing duplicate bookings
•	Updating appointment status
•	Viewing appointment history
•	Maintaining consistent appointment information
Out of Scope
•	Health diagnosis 
•	Decision making about the hospital or clinic 
•	Online services to provide to patients 
•	External healthcare-system integration
•	Advanced analytics
•	Recommendation about the future projects or any sort of recommendation

Provisional
•	User accounts and permissions
•	Patient self-service
•	SMS/email reminders
•	Automated reports
•	External integrations
•	Dedicated administrator role

5. Functional Requirements
FR 01- The system should allow the staff to book an appointment.
FR 02 The system should allow the staff to keep the track of the record 
FR 03 The system should allow the staff to make changes to the data of patients.
FR 04 The system should allow the staff to create the practitioner data about their schedules and allow them to make changes in the data 
FR 05 The system shall allow authorised staff to book an appointment for the patient at the specific time or date as per patient and practitioners availability 
FR 06 The system should allow the staff to cancel the appointments if there is any change in the practitioner’s schedule or availability or there are two patients booked at same time 
FR 07 The system should allow the staff to maintain and update the schedule of the practitioner
FR 08 The system should allow the staff to make changes or update the appointments specifications at every stage
FR 09 The system shall allow authorised staff to view the appointment history associated with a patient.
FR 10 The system shall store appointment details, including the patient, practitioner, date, time and status, so they can be retrieved after being saved.

6. Non-Functional Requirements
ID	Category	Non-Functional Requirement
NFR             -01	Usability	The system should allow the staff members to keep the track of record of patients and can have access to the patient data just by searching their name rather than using any database tools 
NFR-02	Data Integrity	The system should prevent creating the duplicate data record of patient 
NFR-03	Reliability	The system should store the data or information of the patient or partitioners in the system for the future use 
NFR-04	Maintainability	The system should allow the staff to create the change in the data or modify the data rather than just redesigning the whole system
NFR-05	Testability	The system shall produce predictable results for patient searches, appointment creation and appointment-status 
NFR-06	Data Consistency	The system shall use consistent appointment-status values throughout the system.


7. User Stories
User Story 1 –Booking an Appointment
As a reception staff member, I want to search for a patient record so that I can quickly access the patient’s information.

User Story 2 – Find Patient Information
As a reception staff member, I want to create an appointment for a patient with a practitioner so that the appointment is recorded accurately.

User Story 3 – Update Appointment Stats 
As a reception staff member, I want to update an appointment’s status so that staff can see its current state consistently.


User Story 4 – View Appointment History
As a practitioner, I want to view a patient’s appointment history so that I can see previous appointments.

8. Acceptance Criteria
US-01 – Patient Search
Given a patient record exists
When staff search for the patient
Then the matching patient record is displayed.
Given no matching patient exists
When staff perform a search
Then the system indicates that no matching record was found.
US-02 – Appointment Creation
Given a patient and practitioner exist and the appointment time is available
When staff create an appointment
Then the appointment is saved.
Given the practitioner already has an appointment at the selected time
When staff attempt to create another appointment
Then the system prevents the duplicate appointment from being saved.
US-03 – Appointment Status
Given an appointment exists
When staff select an approved appointment status
Then the status is saved.
Given an invalid status is entered
When staff attempt to save it
Then the system rejects the invalid status.
US-04 – Appointment History
Given a patient has recorded appointments
When the practitioner views the history
Then the recorded appointments and statuses are displayed.
Given a patient has no recorded appointments
When the practitioner views the history
Then the system indicates that no appointment history is available.
US-05 – Patient Information
Given an existing patient record is available
When staff update valid patient information and save it
Then the updated information is stored.
Given required information is missing or invalid
When staff attempt to save the record
Then the system prevents the invalid information from being saved.

9. Assumptions and Open Questions
Assumptions
These are working assumptions made:
•	Staff will be given the access to the system 
•	Appointments will require a format like proper date and time to get stored in the system 
•	Each patient is identified with the unique name, and all patients have different details 
•	Practitioner should have the fixed schedule according to which the appointments are been held.
•	The system has enough database storage to save all the records of the patients 

Open Questions
1.	What information is needed to be stored in the record of the patient 
2.	What information is needed to be stored in the record of the practitioner.
3.	What things are referred to be included as the duplicate bookings 
4.	How should patients be uniquely identified?
5.	Which staff members should have the access to the data to make changes or modify the data of the patient and the practitioners 
6.	What aspects are expected from the client to be concluded the system as maintainable 
7.	Are patients required to give access online to Smart Care online for booking their appointments 

10. Selected AI Review Evidence
The AI findings and the review evidence is provided below:

Evidence 1 – Appointment Status
The client explicitly reports “inconsistent appointment status.” Therefore, the AI suggestion to clarify the approved appointment statuses is supported by the brief.
Decision: Accepted.
Evidence 2 – Duplicate Bookings
The client explicitly reports “duplicate bookings.” Therefore, the AI suggestion to clarify exactly when a booking should be considered a duplicate is supported.
Decision: Accepted.
Evidence 3 – Patient Fields
The brief says SmartCare will manage patients but does not identify the required patient information.
Decision: Accepted as an open question, not as a new requirement.
Evidence 4 – SMS Reminders
The client brief does not mention SMS or email reminders.
Decision: Rejected as a requirement / not added to scope.
Evidence 5 – Patient Mobile Application
The brief does not say that patients will directly access SmartCare through a mobile application.
Decision: Rejected as a requirement / placed outside confirmed scope.


## 
Reflection – AI Requirements Review
AI   highlighted that requirements such as creating a patient record and updating an appointment status could not completely testable because the client had not specified the values which are to be included In the patient and the practitioner field. AI needs to be got classified which appointments are included as the duplicate bookings and which are unique to be get stored 
However, AI has too many suggestions for this system which were not included by the client’s brief, Examples include assumptions about reminding the patients about their appointment, patient mobile applications and specific performance targets. These suggestions are not considered because we do not have any evidence of them in the client’s brief 
The requirements needs an evidence to become the part of the system because a system is designed as per the clients requirements and the brief we cannot go out of them and add the requirements to the system without any evidence of them in the clients’ brief. If requirements are based on assumptions, developers may build unnecessary features. Evidence also makes requirements easier to justify, verify and test, helping prevent scope creep and misunderstandings between stakeholders and developers. I  added open questions about the status values and duplicate-booking rules rather than inventing answers.


