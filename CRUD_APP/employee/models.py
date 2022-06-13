from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.IntegerField(null=True)

    class Meta:
        db_table = 'EMPLOYEE'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

