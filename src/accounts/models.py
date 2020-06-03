from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

import random
import string


def create_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=80))


User = settings.AUTH_USER_MODEL
PRO_TYPE = settings.PROFILE_TYPE
CITIES = settings.EGY_CITIES


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')

    account_type = models.CharField(
        max_length=10, choices=PRO_TYPE, verbose_name='you are a *can\'t change later*  ')

    city = models.CharField(max_length=30, choices=CITIES)
    address = models.CharField(max_length=60)
    Mobail = models.CharField(max_length=12)
    subject = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField()
    school_name = models.CharField(max_length=160)
    year = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username


'''
class TeacherFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    the_file = models.FileField(upload_to='teacher files/')
    file_name = models.CharField(max_length=60)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''


class EmailConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = create_code()

        super().save(*args, **kwargs)

    def active_user_email(self):
        subject = 'School code'
        message = f'http://127.0.0.1:8000/account/activate/{self.code}/'
        from_mail = settings.DEFAULT_FROM_EMAIL
        self.send_code_email(subject, message, from_mail)

    def send_code_email(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [
                  'eng.oabbass@gmail.com'], fail_silently=True, ** kwargs)


def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=user)
        create_email_conf = EmailConfirm.objects.create(user=user)

        if create_email_conf:
            create_email_conf.active_user_email()


post_save.connect(create_profile, sender=User)
