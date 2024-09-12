from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common_app.models import BaseModel


class GenderChoices(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female",
    OTHERS = "OTHERS", "Others",


class Candidate(BaseModel):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=16, choices=GenderChoices.choices)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
