from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str.format(self.name)


class Kitten(models.Model):
    """

    """
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(460)])
    color = models.CharField(max_length=200)
    description = models.TextField()
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str.format(self.name, self.breed, self.age, self.color, self.description, self.user)


class Grade(models.Model):
    grade_value = models.IntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(5)])
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
