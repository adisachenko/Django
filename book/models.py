from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone as tz
import datetime

def validate_date_not_in_future(value):
    if value > datetime.date.today():
        raise ValidationError('date is in the future')
        return value
def validate_date_after(value):
    date= datetime.date(2018, 1, 1)
    if value < date:
        raise ValidationError('Publication should be after 01.01.2018')
        return value

# Create your models here.
class Author(models.Model):
      name = models.CharField(max_length=200, null=True)

      def __str__(self):
          return self.name
      



class Book(models.Model):
      title = models.CharField(max_length=200, null=True)
      publication = models.DateField(validators=[ validate_date_not_in_future, validate_date_after])
      author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
      body = models.TextField(null=True)
      
     

      def __str__(self):
          return self.title