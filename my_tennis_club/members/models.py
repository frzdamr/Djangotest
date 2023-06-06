from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    birthdate = models.DateField(null= True)

def __srt__(self):

    return f"{self.firstname} {self.lastname}"

     

