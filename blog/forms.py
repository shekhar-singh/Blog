from django import forms
from blog.models import Register,UserEditPro

class SignupForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model=Register
		fields=['username','email','password']

class LoginForm(forms.Form):
	email=forms.CharField(max_length=25)
	password=forms.CharField(widget=forms.PasswordInput())

class UserForm(forms.ModelForm):

	class Meta:
		model=UserEditPro
		fields=['name','bio','contect']