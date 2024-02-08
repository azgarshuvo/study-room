from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# This user model is for the custom user model
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True) # it will override the default email field
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email' # saying django that the username filed will be email field now
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # host->room [one to many] |SET_NULL means when a topic is deleted, don't delete the room. just make it null
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # topic->room [one to many]
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    participants =  models.ManyToManyField(User, related_name='participants', blank= True) # user(participants)->room [many to many]
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created'] # ordering the list | updated(Ascending), -updated(Descending)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user->message [one to many]. the CASCADE keywords says that if a user is deleted then all messages of that user will be deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # room -> message [one to many]
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] # ordering the list | updated(Ascending), -updated(Descending)
    
    def __str__(self):
        return self.body[0:50] #the value supposed to be returned by default
    