from django.db import models
#import rich text field
from ckeditor.fields import RichTextField
# Create your models here.

class events(models.Model):
    title=models.CharField(max_length=100)
    description=RichTextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='event_images/')
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            super().delete(*args, **kwargs)
            storage.delete(path)
        else:
            super().delete(*args, **kwargs)
            
    def save(self, *args, **kwargs):
        if self.pk:
            old_event = events.objects.get(pk=self.pk)
            if self.image and old_event.image and self.image != old_event.image:
                storage, path = old_event.image.storage, old_event.image.path
                storage.delete(path)
        super().save(*args, **kwargs)
        
    