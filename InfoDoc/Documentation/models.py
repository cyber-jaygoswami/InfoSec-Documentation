from django.db import models
import uuid
# Create your models here.


# tool description model

class Description(models.Model):
    id =  models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    tool_name = models.CharField(max_length=128)
    tool_description = models.TextField()

    def __str__(self):
        return self.tool_name

class Command(models.Model):
    id =  models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    command_name = models.CharField(max_length=200)
    command = models.CharField(max_length=500)
    tool = models.ForeignKey(Description,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.command_name