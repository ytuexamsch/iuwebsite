from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.core.validators import  MinValueValidator
# Create your models here.

seniority_dict = (
("1","1"),
("2", "2"))

class Assistants(models.Model):
    authorized = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Authorized")
    assistant_code = models.CharField(max_length = 5,verbose_name = "Supervisor Code", blank= False)
    assistant_name = models.CharField(max_length = 150, verbose_name = "Supervisor Name",blank= False)
    seniority = models.CharField(max_length=1,verbose_name="Seniority",choices=seniority_dict)
    undesired_days = models.CharField(validators=[validate_comma_separated_integer_list],max_length=100,verbose_name="Unfavorable Days",blank=True, null=False)
    undesired_slots = models.CharField(validators=[validate_comma_separated_integer_list],max_length=100,verbose_name="Unfavorable Slots",blank=True, null=False)
    total_assignment = models.IntegerField(validators=[MinValueValidator(0)],verbose_name="Total Assignments", blank=False)
    def __str__(self):
        return str(self.assistant_name)
