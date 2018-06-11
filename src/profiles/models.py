from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from .choices import *

# from .forms import RegisterForm
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	# blood_group  = models.ChoiceField(label='Qan qrupunuz',choices=BLOOD_GROUP, required=True)
	gender	= models.IntegerField(choices=GENDER_CHOICES,default=1, null=True)



	def __str__(self):
		return str(self.user.username)



def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
	if created:
		try:
			Profile.objects.create(user=instance)
		except:
			pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)