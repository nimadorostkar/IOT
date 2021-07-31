from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile, User_uuid
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from . import models


#------------------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone','address','user_photo']


#------------------------------------------------------------------------------
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']



#------------------------------------------------------------------------------
class User_uuidForm(forms.ModelForm):
	class Meta:
		model = User_uuid
		fields = ['UUID']
