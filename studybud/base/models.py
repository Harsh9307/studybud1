from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)  #a topic can have multiple room but a room can have a single topic only ---> one to many relationship
    name=models.CharField(max_length=200)
    description=models.TextField(null=True ,blank=True)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):      #each message has to get stored in dataabase
    user=models.ForeignKey(User,on_delete=models.CASCADE)    #one to many relationships
    room=models.ForeignKey(Room,on_delete=models.CASCADE)     #many to one realtionship with room model.
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:50]