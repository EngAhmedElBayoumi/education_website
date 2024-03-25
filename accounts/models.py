from django.db import models
#import user model
from django.contrib.auth.models import User
#import rich text field
from ckeditor.fields import RichTextField
# Create your models here.

class Skills(models.Model):
    skill=models.CharField(max_length=100)
    def __str__(self):
        return self.skill


class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profiles', blank=True)
    bio=RichTextField()
    points=models.IntegerField(default=0)
    skills=models.ManyToManyField(Skills, blank=True)
    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            super().delete(*args, **kwargs)
            storage.delete(path)
        else:
            super().delete(*args, **kwargs)
            
    def save(self, *args, **kwargs):
        if self.pk:
            old_profile = profile.objects.get(pk=self.pk)
            if self.image and old_profile.image and self.image != old_profile.image:
                storage, path = old_profile.image.storage, old_profile.image.path
                storage.delete(path)
        super().save(*args, **kwargs)
        


