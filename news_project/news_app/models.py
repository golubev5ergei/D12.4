from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    def __str__(self):
        return self.title