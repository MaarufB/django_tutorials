from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    images_file = models.ImageField(null=True, blank=True, default='default.jpeg')


    class Meta:
        db_table = 'MEMBERS' 

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def imageURL(self):
        try:
            img = self.images_file
        except:
            img = ''

        return img