from django.db import models

class Parent(models.Model):
    #Here's hoping nobody has a name longer than 30 char
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return "Parent with name " + self.first_name