from django.db import models
from django.contrib.auth.models import User

class CreateToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tdlist", null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class items(models.Model):
    username = models.ForeignKey(CreateToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    