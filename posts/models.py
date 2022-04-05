from django.db import models

from account.models import MyUser


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title