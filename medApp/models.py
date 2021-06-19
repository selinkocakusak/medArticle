from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def __str__(self):
    # Built-in attribute of django user
    return self.user.username


class content(models.Model):
    no = models.AutoField(primary_key=True)
    doc_id = models.CharField(max_length=20)
    title = models.TextField(default='')
    authors = models.TextField(default='')
    abstract = models.TextField(default='')
    keywords = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.doc_id)


class tagitem(models.Model):
    id = models.AutoField(primary_key=True)
    docId = models.CharField(blank=True, max_length=20)
    tag = models.CharField(max_length=30)
    link = models.URLField(max_length=250)

    def __str__(self):
        return str(self.docId)
