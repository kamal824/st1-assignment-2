# At very first class is defined 
## there are three main clases 
## 1.Patient,2.Practitioner,3.Appointment 

class Patient:
## defining of the components of the patient class in the system below:
    def __init__(self, patient_id, name, Patient_details):
        self.patient_id = patient_id   # Patient id to identify the patient easily  
        self.name = name    ##  Name of the patient 
        self.Patient_details = Patient_details   # Defing the contact details of patient  


## Below is the class of practitioner defined
class Practitioner:
    def __init__(self, practitioner_id, name,):
        self.practitioner_id = practitioner_id
        self.name = name
        self.schedule = [] ## schedule of practitoner definition



## appointment Class definition 
class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = "Scheduled"