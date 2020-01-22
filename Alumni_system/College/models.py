from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class College_Alumni_data(models.Model):
    student_name = models.CharField(max_length = 50)
    student_roll_no = models.IntegerField(unique = True)
    student_batch = models.IntegerField(validators = [MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])

    objects = models.Manager()

    def __str__(self):
        return self.student_name
