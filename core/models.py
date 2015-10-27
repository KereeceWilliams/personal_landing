from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70,blank=True, null=True, unique=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.title

class About(models.Model):
  title = models.CharField(max_length=300)

