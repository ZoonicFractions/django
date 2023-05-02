from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=1)

# Model for student's logs.
class Registro(models.Model):
    # Atributes
    classroom = models.CharField(max_length=1)
    role_number = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    date = models.DateTimeField('date published')
    grade = models.FloatField()
    time = models.FloatField()

    # Methods
    def get_data(self):
        return (self.difficulty, self.level)

    # Primary Key
    class Meta:
        unique_together = (('classroom', 'role_number', 'difficulty', 'level', 'date'),)
