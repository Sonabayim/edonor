from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from .choices import *

# from .forms import RegisterForm
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	blood_group  = models.IntegerField(choices=BLOOD_GROUP, blank=False, null=True)
	gender	= models.IntegerField(choices=GENDER_CHOICES,default=1, null=True)
	timestamp     	= models.DateTimeField(auto_now_add=True)
	updated       	= models.DateTimeField(auto_now=True)
	illness  = models.IntegerField(
		 choices=ILLNESS_CHOICES, blank=False, null=True)

	illness1  = models.IntegerField(choices=ILLNESS_CHOICES, blank=False, null=True)

	illness2  = models.IntegerField(
		 choices=ILLNESS_CHOICES, blank=False, null=True)

	# weight = models.IntegerField(blank=False, null=True)
	# height = models.IntegerField(blank=False, null=True)



	def __str__(self):
		return str(self.user.username)



def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
	if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)