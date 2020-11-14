from django.db import models


CHOICES = (('Family', 'Family'), ('Friends', 'Friend'), ('Work', 'Work'), ('General', 'General'))

class Contact(models.Model):
    firstName = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60, null=True)
    lastName = models.CharField(max_length=60, null=True)
    contact1 = models.CharField(max_length=60)
    contact2 = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60, null=True)
    address = models.TextField(null=True)
    group = models.CharField(max_length=60, null=True, choices= CHOICES, default='General')
    favourite = models.BooleanField(default=False)

    def __str__(self):
        name = self.firstName + " " + self.lastName
        return name
