from django import forms
from django.forms.widgets import DateInput
from .models import *
from django.contrib.auth.models import User
from django.utils.timezone import utc


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username',)
    
    password = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class ResidencyForm(forms.ModelForm):
    class Meta:
        model = Residency
        fields = ('date','start_time','end_time',)
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'start_time' : forms.TimeInput(attrs={'type':'time'}),
            'end_time' : forms.TimeInput(attrs={'type':'time'})
        }
     
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('residency','status',)

class ProjForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('name','desc','due_date','status',)
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'})
        }
        #due_date = forms.DateField(widget=forms.DateInput(format='%Y%m%D'))#, input_formats=['%Y%m%D']))
    
    #due_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

