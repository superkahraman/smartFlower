from django.db import migrations, models
from django.contrib.auth.models import User


# # # # # # # # # # # # # # # # # # # # # # # # # #
# smartPET models.
# # # # # # # # # # # # # # # # # # # # # # # # # #

class Pet(models.Model):
    name = models.CharField(max_length=256)
    type = models.ForeignKey('petTypes', on_delete=models.SET_NULL null=True)
    breed = models.ForeignKey('petBreed', on_delete=models.SET_NULL null=True)
    color = models.CharField(max_length=256)
    birthday = models.DateField(null=True)
    isBarren = models.BooleanField(null=True)
    owner = models.ForeignKey('User', on_delete=models.SET_NULL null=True)

    # When Pet object updated?
    updated = models.DateTimeField(auto_now=True)
    # When Pet object created?
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class petType(models.Model):  # "Cat, Dog, Fish" etc..
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class petBreed(models.Model):  # "Scottish Fold, Jack Russel, Shark" etc.
    name = models.CharField(max_length=256)
    # each Breed object must be have "Cat, Dog, Fish" etc.. (Type information)
    pettype = models.ForeignKey(
        'petTypes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class petPhotos:
    url = models.CharField(max_length=512, null=False)
    pet = models.ForeignKey('Pet', on_delete=models.SET_NULL null=True)

    def __str__(self):
        return self.url
