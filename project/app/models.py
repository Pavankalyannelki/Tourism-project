from django.db import models

from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError  # Make sure this line exists
# Create your models here.

class ROOM_TYPES(models.Model):
    type_rooms=models.CharField( max_length=50,primary_key=True)
    def _str_(self):
        return self.type_rooms

class HotelBooking(models.Model):
    checkin_date = models.DateField(verbose_name='Check-in Date')
    checkout_date = models.DateField(verbose_name='Check-out Date')
    num_guests = models.IntegerField(verbose_name='Number of Guests', default=1)
    Room_Type=models.ForeignKey(ROOM_TYPES,null=True,on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone Number', max_length=10)
    # slots = models.CharField(verbose_name='Slots', max_length=10)
    is_reserved = models.BooleanField(verbose_name='Is Reserved', default=False)

    
    def clean(self):
        # Check if checkout date is not less than check-in date
        if self.checkout_date < self.checkin_date:
            raise ValidationError("Check-out date cannot be earlier than check-in date")

        # Check if num_guests is within the range (1 to 5)
        if self.num_guests < 1 or self.num_guests > 5:
            raise ValidationError("Number of guests must be between 1 and 5")

class Contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.BigIntegerField(primary_key=True)
    message=models.CharField(max_length=50)