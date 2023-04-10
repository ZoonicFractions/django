from django.db import models

# Create your models here.
# Model for users such as admins and teachers
class Usuario(models.Model):
    # Atributes
    mail = models.CharField(max_length=200, primary_key = True)
    role = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

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
