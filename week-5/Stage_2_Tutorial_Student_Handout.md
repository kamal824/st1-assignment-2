## Activity 1 – Stakeholder Map
Stakeholder	Stakeholder Need	Potential Conflict
SmartCare staff	Booking and managing of the appointments easily .	May want more features, while management wants a small and maintainable system.
Practitioners	Access accurate appointment and relevant patient information.	Some of times the practitioner needs some more deep information of the patient 
Management	The easy maintain software system that helps working of Smart Care and maintain the current records 	May prioritise simplicity and cost over additional features.
Patients	Accurate appointments and reliable appointment history.	Patient-facing features may increase system complexity and may not be in the initial scope.
 

## Activity 2 – Functional or Non-Functional?
The correct answers are highlighted below:
Requirement	Answer	Reason
The system shall allow staff to cancel an appointment.	 Functional Non-functional	Describes a specific capability the system must provide.
The system should remain responsive for the course-scale dataset.	 Functional Non-functional	Describes system performance.
The system shall retain cancelled appointments.	 Functional Non-functional	Describes what the system must do with appointment records.
Core business logic should be independently testable.	 Functional Non-functional	Describes testability/maintainability rather than a user-facing function.
The system shall search for a patient by ID.	Functional Non-functional	Describes a specific search capability.
 

## Activity 3 – Repair Ambiguous Requirements
1. The system should be easy to use.
Problem: “Easy to use” is subjective and cannot be measured or tested clearly.
Clarification question: What tasks should staff be able to complete easily, and what measurable usability target should the system meet?
2. Patient search should be fast.
Problem: “Fast” is vague and does not specify an acceptable response time.
Clarification question: How quickly should a patient search return results under normal operating conditions?
3. The system should securely manage data.
Problem: “Securely” is too broad and does not identify specific security controls.
Clarification question: What security requirements are needed, such as user authentication, access permissions, encryption or audit logging?
4. Appointments should normally be easy to cancel.
Problem: “Normally” and “easy” are ambiguous, and the requirement does not explain who can cancel appointments or what happens after cancellation.
Clarification question: Who should be allowed to cancel an appointment, and what should happen to the appointment record after it is cancelled?


## Activity 4 – AI Requirements Audit
AI Suggestion	Classification	Evidence / Reason
Patients receive SMS reminders.	Unsupported	The client brief does not mention SMS reminders.
Facial recognition login.	Unsupported	No facial recognition or login method is specified in the brief.
Receptionists create appointments.	Assumption requiring validation	Staff are mentioned, but the brief does not specifically state that receptionists create appointments.
Online payment.	Out of scope	The brief focuses on patients, practitioners and appointments; payments are not part of the stated problem or scope.
Practitioners view schedules.	Assumption requiring validation	Practitioners are a stakeholder, but the brief does not explicitly state that they need to view schedules.
AI recommends treatments.	Unsupported	There is no requirement for treatment recommendations or clinical decision support.
Cancelled appointments remain in history.	Assumption requiring validation	The brief identifies limited appointment history, but does not explicitly state how cancelled appointments should be handled.
 
## Exit Question
Why is “AI suggested it” not sufficient evidence for a requirement?
AI is not capable of designing the software as per the client needs, AI solutions needs to be tested before implementing, Moreover the AI develops the system that has many more advance and unwanted features as well which were not in the clients’ requirements brief . AI can help identify possibilities, ambiguities and missing requirements, but it must not invent stakeholder needs. 

