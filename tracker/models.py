from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField, TimeField
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.urls import reverse
from django.core.validators import *
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Physician(models.Model):
    CAN_REG = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    cell_no = PhoneNumberField(null=True, blank=True)
    doc_type = models.CharField(max_length=100, null=True)
    can_reg = models.CharField(max_length=100, null=True, blank=True, choices=CAN_REG)

    def __str__(self):
        return self.doc_type + " " + self.last_name



class Patient(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    suffix = models.CharField(max_length=2, null=True, blank=True)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX)
    birthdate = models.DateField(null=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    attending_doctor = models.ForeignKey(Physician, related_name="docpatient", on_delete=models.CASCADE, null=True)

    #Vaccine Certificate Date
    cert_date = models.DateField(null=True, blank=True)

    # Contact Deets
    cell_no = PhoneNumberField(null=True, blank=True, validators=[MaxLengthValidator(13)])
    landline = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    # Address
    house_no = models.CharField(max_length=100, null=True, blank=True)
    barangay = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    
    # Mother
    mfname = models.CharField(max_length=100, null=True, blank=True)
    mlname = models.CharField(max_length=100, null=True, blank=True)
    mcontact = PhoneNumberField(null=True, blank=True)
    memail = models.EmailField(max_length=254, null=True, blank=True)
    # Father
    ffname = models.CharField(max_length=100, null=True, blank=True)
    flname = models.CharField(max_length=100, null=True, blank=True)
    fcontact = PhoneNumberField(null=True, blank=True)
    femail = models.EmailField(max_length=254, null=True, blank=True)

    c1full_name = models.CharField(max_length=100, null=True, blank=True)
    relation1 = models.CharField(max_length=100, null=True, blank=True)
    c1contact = PhoneNumberField(null=True, blank=True)

    c2full_name = models.CharField(max_length=100, null=True, blank=True)
    relation2 = models.CharField(max_length=100, null=True, blank=True)
    c2contact = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class PatientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    relationship = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} of {}'.format(self.relationship, self.patient)


class Appointment(models.Model):
    STATUS = (
        ('Blank','Blank'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Rescheduled', 'Rescheduled'),
        ('Requested', 'Requested'),
    )
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    doctor = models.ForeignKey(Physician, on_delete=models.CASCADE)
    visit = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.patient)

class Vaccine(models.Model):
    LOCATION = (
        ('R thigh', 'R thigh'), ('L thigh', 'L thigh'), ('R arm ', 'R arm'),
        ('L arm', 'L arm'), ('R buttocks', 'R buttocks'), ('L buttocks', 'L buttocks'),
    )
    age = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    dose = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True, choices=LOCATION)
    remarks = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)
        
class PatientVaccine(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} for {}".format(self.vaccine, self.patient)