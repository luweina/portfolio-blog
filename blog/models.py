from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    caption = models.CharField(max_length=255, default="caption")
    content = models.TextField()
    discription = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

