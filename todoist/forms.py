from django import forms 

class Register(forms.Form):
	username = forms.CharField(label='用户名：',max_length=50)
	password = forms.CharField(label='密码：',max_length=100,min_length=10)

class Login(forms.Form):
	l_username = forms.CharField(label='用户名：',max_length=50)
	l_password = forms.CharField(label='密码：',max_length=100,min_length=10)