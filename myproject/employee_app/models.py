from django.db import models

class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.empname
