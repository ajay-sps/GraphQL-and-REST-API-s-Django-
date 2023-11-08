from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    department_id = models.ForeignKey('Department', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

