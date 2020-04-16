from django.db import models

# Create your models here.

class User(models.Model):

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

class Series(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)

class Film(models.Model):

    def __str__(self):
        return self.name

    def standalone(self):
        return self.series is None

    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)
    ordinal = models.IntegerField(default=0)
    name = models.CharField(max_length=250)
    addition_date = models.DateTimeField('Date added')

    user = models.ForeignKey(User, related_name='films', on_delete=models.CASCADE)

