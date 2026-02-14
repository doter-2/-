from django.db import models

# Create your models here.
class Articles(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  body = models.TextField()

def __str__(self):
  return self.title


class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    img = models.ImageField(upload_to='media/', blank=True, null=True, default='media/default.png')
    class Meta:
       ordering = ['date']

def __str__(self):
  return self.title


