from django.db import models
from uuid import *
from django.utils import timezone

# Create your models here.
class Recovers(models.Model):
    username = models.CharField("username", unique=True, max_length=50, primary_key=True)
    token = models.CharField("token", unique=True, max_length=36)
    time_created = models.DateTimeField("time created", default=timezone.now)

    def generate_token(self, random = True):
        if random:
            self.token = str(uuid4())
        else:
            self.token = str(uuid5(NAMESPACE_DNS, self.username))

    def __str__(self) -> str:
        return f'{self.username} requested to recover password at time {self.time_created.hour}'
    
    def time_elapsed(self):
        return timezone.now() - self.time_created
    
