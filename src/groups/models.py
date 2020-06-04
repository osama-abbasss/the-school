from django.db import models
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Group(models.Model):
    auther = models.ForeignKey(
        User, related_name='group_auther', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User, related_name='group_students', through='GroupMember')
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != self.name:
            self.slug = self.auther.username+slugify(self.name)

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('auther', 'name')


class GroupMember(models.Model):
    user = models.ForeignKey(
        User, related_name='user_groups', on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, related_name='memberships', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'group')
