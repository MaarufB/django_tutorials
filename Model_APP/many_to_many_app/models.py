from django.db import models

# Create your models here.

# Many-to-one Relationship
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.headline


# One-to-One Relationship

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return "%s the place name " % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant " % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "% the waiter at %s " % (self.name, self.restaurant)
