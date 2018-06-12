from django.db import models
from profiles.choices import *

# Create your models here.



class DonorList(models.Model):
	first_name = models.CharField(max_length=120, null=True,blank=True )
	last_name = models.CharField(max_length=120, null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	blood_group  = models.IntegerField(choices=BLOOD_GROUP, blank=False, null=True)
	gender	= models.IntegerField(choices=GENDER_CHOICES,default=1, null=True)
	timestamp     	= models.DateTimeField(auto_now_add=True)
	updated       	= models.DateTimeField(auto_now=True)
	illness  = models.IntegerField(
		 choices=ILLNESS_CHOICES, blank=False, null=True)

	illness1  = models.IntegerField(choices=ILLNESS_CHOICES, blank=False, null=True)

	illness2  = models.IntegerField(
		 choices=ILLNESS_CHOICES, blank=False, null=True)

	birth_date  = models.DateField(auto_now_add=False, auto_now=False, null=True)

	def __str__(self):
		return self.first_name