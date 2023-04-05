from django import forms
from .models import usersignup,mynotes,feedback

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
    
class updateform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields=['firstname','lastname','username','password','city','state','mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'