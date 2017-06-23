from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateDue = models.DateTimeField()
    team = models.ForeignKey('Team')
    status = models.CharField(max_length=20)


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = []
    roles = []
    projects = []
'''
    def assignProj(self):
        asfda

    def addMember(self):
        asdfasd

    def removeMember(self):

    
    def assignRoles(self):


class User
'''