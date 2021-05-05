from django.db import models
from django.utils import timezone
# Create your models here.


class Message(models.Model):
    #TODO add serial number
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=False)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    phoneNumber = models.CharField(max_length=20, null=False, default='-')

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' - ' + self.date.__str__()


class Warranty(models.Model):
    startDate = models.DateField(default=timezone.now)
    endDate = models.DateField(null=False)
    length = models.IntegerField(null=False)
    warrantyNumber = models.CharField(max_length=50, primary_key=True)
    product = models.CharField(max_length=100, null=False)
    serialNumber = models.CharField(max_length=50)
