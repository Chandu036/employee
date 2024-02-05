from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import *
from django.core.mail import send_mail
from django.conf import settings


# def createProfile(sender, instance, created, **kwargs):
#     print("profile signal trigred")
#     if created:
#         user = instance
#         profile = EmployeeProfile.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#             name=user.first_name,
            
            
#         )
#         subject = 'welcome to employee management system'
#         message = 'we are glad you to hear'
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             [profile.email],
#             fail_silently=False,
#         )
# def deleteUser(sender, instance, **kwargs):
#     user = instance.profile
#     user.delete()
    
# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=EmployeeProfile)
