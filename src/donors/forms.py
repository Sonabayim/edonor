from django import forms
from .models import DonorList
from profiles.choices import *

class DonorCreateForm(forms.ModelForm):
	YEARS= [x for x in range(1940,2021)]

	first_name = forms.CharField(label='Adiniz', required=True)
	last_name  = forms.CharField(label='Soyadiniz', required=True)
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	gender    = forms.ChoiceField(label='Cins', choices=GENDER_CHOICES, required=True)
	blood_group  = forms.ChoiceField(label='Qan qrupunuz',choices=BLOOD_GROUP, required=True)
	birth_date  = forms.DateField(label='Dogum gununuz',
	 widget=forms.SelectDateWidget(years=YEARS))
	illness  = forms.ChoiceField(
		label='Sarılıq, deri xesteliyi, göz xesteliyi, qanla ve ürekle bağlı xestelikler keçirmisinizmi?',
		 choices=ILLNESS_CHOICES, required=True)

	illness1  = forms.ChoiceField(
		label='6 ay erzinde emeliyyat olunmusunuzmuk?( yungul emeliyyat)',
		 choices=ILLNESS_CHOICES, required=True)

	illness2  = forms.ChoiceField(
		label='Bedeninizde tato varmı? ( vardırsa eletdirdiyiniz vaxtdan minimum 1 il keçmelidir.)',
		 choices=ILLNESS_CHOICES, required=True)

	weight = forms.IntegerField(label='Çəkiniz' , required=True)
	height = forms.IntegerField(label='Boyunuz' , required=True)


	last_blood_date= forms.DateField(
		label='Daha evvel qan vermisinizse qan verme tarixini qeyd edin',
	 widget=forms.SelectDateWidget(years=YEARS))
	


	class Meta:
		model = DonorList
		fields = ('first_name',
		'last_name',
		'username', 
		'email', 
		'gender',
		'blood_group',
		'birth_date',
		'last_blood_date',
		'illness',
		'illness1',
		'illness2',
		'weight',
		'height',
		   )

		