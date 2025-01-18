from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instragram_url')

		widgets ={
				'bio': forms.Textarea(attrs={'class': 'form-control'}),
				#'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
				'website_url': forms.TextInput(attrs={'class': 'form-control'}),
				'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
				'instragram_url': forms.TextInput(attrs={'class': 'form-control'}),
			}


class SignUpForm(UserCreationForm):
	email = forms.EmailField() #(attrs={'class': 'form-control'})
	first_name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, min_length=1, widget=forms.TextInput(attrs={'class':'form-control'}))
	address_one = forms.CharField(max_length=100, min_length=1)
	address_two = forms.CharField(max_length=100, min_length=1)
	address_three = forms.CharField(max_length=100)
	county_name = forms.Select()
	country_api = forms.Select()

	class Meta:
		model = User
		fields =('username' , 'first_name', 'last_name', 'password1', 'password2') #, 'address_one ','address_two',
	#'address_three', 'county_name', 'country_api')

#	def __init__(self, *args, **kwargs):
#		super(SignUpForm, self).__init__(*args, **kwargs)

#		self.fields['username']. widget.attrs['class'] = 'form-control'
#		self.fields['password1']. widget.attrs['class'] = 'form-control'
#		self.fields['password2']. widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
	email = forms.EmailField()
	first_name = forms.CharField(min_length=1, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(min_length=1, max_length=100)
	address_one = forms.CharField(min_length=1, max_length=100)
	address_two = forms.CharField(min_length=1, max_length=100)
	address_three = forms.CharField(min_length=1, max_length=100)
	address_four = forms.CharField(min_length=1, max_length=100)
	address_five = forms.CharField(min_length=1, max_length=100)
	terms_conditions = forms.CharField(widget=forms.CheckboxInput(attrs={' class': 'form-check'}))
	#DoB = forms.CharField(min_length=8, max_length=8, widget=forms.DateField(attrs={'class':'form-control'}))
	#Date_time_joined = forms.CharField(widget=forms.DateTimeField(attrs={'class':'form-control'}))

	class Meta:
			model = User
			fields =('username', 'first_name', 'last_name', 'email', 'address_one', 'address_two', 'address_three', 'address_four','address_five', 'terms_conditions')

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password1 =forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	class Meta:
		model = User
		fields = ('old_password','new_password1', 'new_password2')