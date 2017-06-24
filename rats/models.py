from django.db import models
from django.utils import timezone
from datetime import datetime, date


class Residency(models.Model):
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    duration_in_mins = models.IntegerField(default=90)
    def get_duration_in_mins(self):
        duration = datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)
        if int(abs(duration.total_seconds()//60)) == None:
            self.duration_in_mins = 90
            return self.duration_in_mins
        else:
            self.duration_in_mins = int(abs(duration.total_seconds()//60))
            return self.duration_in_mins
        

class Project(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
   # team = models.ForeignKey('Team', blank=True, null=True)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)
    


class Team(models.Model):
    name = models.CharField(max_length=100)
    max_capacity = models.IntegerField(default=5)
    '''
    members = []
    roles = []
    projects = []'''
'''
    def assignProj(self):
        asfda

    def addMember(self):
        asdfasd

    def removeMember(self):

    
    def assignRoles(self):


class User
'''