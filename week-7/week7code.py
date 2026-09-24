# part- B
class Patient:
    def __init__(
        self,
        patient_id: str,
        name: str,
        Patient_details: str
    ) -> None:
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Patient name cannot be empty")

        if not Patient_details.strip():
            raise ValueError("patient details cannot be empty")

        self.patient_id: str = patient_id
        self.name: str = name
        self. patient_details: str = Patient_details



## Part - c 

class Practitioner:
    def __init__ (
        self,
        practitioner_id: str,
        name: str,
        specialty: str
    ) -> None:
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        self.practitioner_id: str = practitioner_id
        self.name: str = name
        self.specialty: str = specialty

# Part - D 
from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date_time: datetime
    ) -> None:
        if not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty")

        self.appointment_id: str = appointment_id
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date_time: datetime = date_time
        self.status: AppointmentStatus = AppointmentStatus.SCHEDULED

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")

        self.status = AppointmentStatus.CANCELLED
