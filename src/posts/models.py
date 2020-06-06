from django.db import models
from groups.models import Group
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    content = models.TextField(verbose_name='post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
