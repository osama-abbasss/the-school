from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TeacherFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    the_file = models.FileField(
        upload_to='teacher files/', verbose_name=' upload file')
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
