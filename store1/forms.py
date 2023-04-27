from django import forms
from store1 import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class CreatPostFrom (forms.ModelForm):
    # class Meta:
        # model = models.Post
        # fields = ['tittle','description']

 class Dummy(forms.form):
    eamil = forms.Emailfield()
    first_name = .CharField(max_lenght=20)
    last_name = .CharField(max_lenght=20)
    description = forms.CharField()
    class meta:    
# class DummyForm(UserCreationForm):
    # email = forms.EmailField()
    # class Meta:
        # model = User
        # fields = ['email']


