from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    #code =
    #issues =
    #pull requests
    #actions
    #projects
    #wiki = models.TextField(max_length=10000)
    #category(public or private)
    stars = models.IntegerField(max_length=5)
    watching = models.IntegerField(max_length=5)
    forks = models.IntegerField(max_length=5)
    


    def __str__(self):
        return self.title
