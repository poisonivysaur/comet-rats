from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import localtime, now
from datetime import datetime, date


class Residency(models.Model):
    user = models.ForeignKey('auth.User',null=True)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    duration_in_mins = models.IntegerField(default=90)
    
    def get_duration_in_mins(self):
        duration = datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)
        if int(abs(duration.total_seconds()//60)) == None:
            self.duration_in_mins = 90
            return self.duration_in_mins
        else:
            self.duration_in_mins = int(abs(duration.total_seconds()//60))
            return self.duration_in_mins
    def __str__(self):
        return str(self.date)


class Attendance(models.Model):
    user = models.ForeignKey('auth.User',null=True)
    residency = models.ForeignKey('rats.Residency', related_name='attendance', null=True)
    start_time = models.TimeField(default='08:00:00')
    end_time = models.TimeField(default='11:00:00')
    status = models.CharField(max_length=200, null=True)
    
    def start(self):
        self.start_time = timezone.now()

    def end(self):
        self.end_time = timezone.now()

    def get_total_duration(self):
        duration = datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)
        if int(abs(duration.total_seconds()//60)) == None:
            return 0
        else:
            return int(abs(duration.total_seconds()//60))
        
    def __str__(self):
        return str(self.residency.date)


class Team(models.Model):
    user = models.ForeignKey('auth.User', related_name='ownerk', null=True)
    members = models.ManyToManyField(User)
    team_name = models.CharField(max_length=100)
    max_capacity = models.IntegerField(default=5)
    project = models.ForeignKey('rats.Project', null = True)

    @classmethod
    def addMember(cls, user, new_team):
        team, created = cls.objects.get_or_create(
            user = user
        )
        team.members.add(new_team)

    def __str__(self):
        return str(self.team_name)


class Project(models.Model):
    user = models.ForeignKey('auth.User', related_name='owner', null=True)
    committee = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    desc = models.TextField(default="")
    due_date = models.DateField(blank=True, null=True)
   # team = models.ForeignKey('Team', blank=True, null=True)
    status = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.name)


