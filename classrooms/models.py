from django.db import models
from django.core.validators import  MinValueValidator
# Create your models here.
lab_or_not_dict = (
("1", "Lab Classroom"),
("0",  "Standard Classroom"))
class Classrooms(models.Model):
    authorized = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Authorized")
    classroom_code = models.CharField(max_length = 3, verbose_name = "Classroom Code", blank = False)
    classroom_name = models.CharField(max_length = 25, verbose_name = "Classroom Name",blank = False)
    classroom_capacity = models.IntegerField(validators=[MinValueValidator(0)],verbose_name = "Classroom Capacity", default=0, blank=False)
    lab_or_not = models.CharField(max_length=20, verbose_name="Lab or Not", choices = lab_or_not_dict)


    def __str__(self):
        return str(self.classroom_name)