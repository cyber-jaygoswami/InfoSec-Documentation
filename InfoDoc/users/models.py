from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=256,null=True,blank=True)
    user_feedback =  models.TextField()


    def __str__(self):
        return self.name