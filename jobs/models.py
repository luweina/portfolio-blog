from django.db import models

class Job (models.Model):
    image = models.ImageField(upload_to ='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default='title')
    link = models.URLField(default='url')


class Contact (models.Model):
    name=models.EmailField()
    email = models.EmailField()
    messagetitle = models.TextField(max_length=100, default='message')
    subject = models.TextField()
    def __str__(self):
        return self.name

