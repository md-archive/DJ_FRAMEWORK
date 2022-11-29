from django.db import models

class username(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class items(models.Model):
    username = models.ForeignKey(username, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text