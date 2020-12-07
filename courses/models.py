from django.db import models
from django.core.validators import  MinValueValidator
# Create your models here.
# Char and text types are never saved as null by Django, so null=True is unnecessary.
# db_index diye bir parametremiz var, bunu kullanabiliriz, bir bakalım. 

class Courses(models.Model):
    sixty_more_dict = (
                    ('1', 'More than or equal to 66'),
                    ("0",'Less than 66'))
    lab_or_not_dict = (
                    ("1","Lab Course"),
                    ("0", "Standard Course"))
    authorized = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Authorized")
    course_code = models.CharField(max_length=5, verbose_name = "Exam Code", blank= False)
    course_name = models.CharField(max_length=150, verbose_name = "Exam Name",blank= False)
    course_capacity = models.IntegerField(validators=[MinValueValidator(0)],verbose_name="Exam Capacity", default=0, blank=0)
    sixty_more = models.CharField(max_length=20, verbose_name="Is Class Capacity Over 66?",choices=sixty_more_dict)
    slot_number = models.IntegerField(validators=[MinValueValidator(0)],verbose_name="Slot Number", default=1)
    lab_or_not = models.CharField(max_length=20, verbose_name="Lab or Not", choices=lab_or_not_dict)
    department = models.CharField(max_length=30,verbose_name="Department", blank=False, null=False)
    desired_day = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Pre-Defined Days", blank=True, null=True)
    desired_slot = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Pre-Defined Slots", blank=True, null=True)



    def __str__(self):
        return str(self.course_name)


class SameTimeCourses(models.Model):
    hard_or_soft_dict = (
                    ('1', 'Hard Constraint'),
                    ("0",'Soft Constraint'))
    authorized = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Authorized")
    course1_code = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name="First Exam", related_name = "course_1_code")
    course2_code = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name="Second Exam", related_name = "course_2_code")
    cost = models.IntegerField(validators=[MinValueValidator(0)],verbose_name="Exam Capacity", default=0, blank=False)

