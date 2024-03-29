from django.db import models


# Create your models here.

class Book(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    ISBN = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(max_length=4)


class Accounts(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    accType = models.CharField(max_length=100)
