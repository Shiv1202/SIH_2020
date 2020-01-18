from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# Users Models for storing data in Database.
#class Alumni_Manager(models.Manager):


class Alumni_User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    college_name = models.CharField(max_length = 50)
    graduation_yr = models.IntegerField(validators = [MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])
    roll_no = models.IntegerField(unique = True)
    password = models.CharField(max_length = 60)
    is_verified = models.BooleanField(default = False)

    def __str__(self):
        return (self.name, self.college_name, self.graduation_yr, self.roll_no)


# College Model for sotring data in Database.
class Colleges(models.Model):
    college_name = models.CharField(max_length = 50)
    college_code = models.CharField(max_length = 5)

    def __str__(self):
        return (self.college_name, self.college_code)

