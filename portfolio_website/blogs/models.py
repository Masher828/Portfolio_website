from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255   )
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image= models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
