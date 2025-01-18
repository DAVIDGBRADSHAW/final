from django import forms
from .models import Post, Category,Comment


#choices = Category.objects.all().values_list('name', 'name')

choice= [('photo1', 'photo1'), ('photo2', 'photo2'), ('photo3', 'photo3'), ('photo4', 'photo4'), ('photo5', 'photo5'),('photo6', 'photo6'), ('photo7', 'photo7')]

choice_list= [('photo1', 'photo1'), ('photo2', 'photo2'), ('photo3', 'photo3'), ('photo4', 'photo4'), ('photo5', 'photo5'),('photo6', 'photo6'), ('photo7', 'photo7')]
#choice_list= [('pick one', 'Please pick a day of the week'),('Monday', 'monday'), ('Tuesday', 'tuesday'), ('Wednesday', 'wednesday'), ('Thursday', 'thursday'), ('Friday', 'friday'),('Saturday', 'saturday'), ('Sunday', 'sunday')]


#for item in choices:
#	choice_list.append(item)
#Day [('pick one', 'Please pick a day of the week'),('Monday', 'monday'), ('Tuesday', 'tuesday'), ('Wednesday', 'wednesday'), ('Thursday', 'thursday'), ('Friday', 'friday'),('Saturday', 'saturday'), ('Sunday', 'sunday')] # hard coding

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category','body','snippet', 'header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put in ur subject title'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Put in small tag to describe what this relates to'}),
			#'author': forms.Select(choices=choices,attrs={ 'value':'', id:'---', 'type': 'hidden'}),
			#'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
			#'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
			#'day': forms.Select(choices=days,attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in here,  max 1000 charters'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
		}


		
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category','body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put in ur subject title'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put in small tag to describe what this relates to'}),
			#'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
			
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in here,  max 1000 charters'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}