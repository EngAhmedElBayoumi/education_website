from django.db import models
#import rich text field
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)   
    image=models.ImageField(upload_to='blogs', blank=True)
    short_description=models.TextField()
    topic=RichTextField()
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            super().delete(*args, **kwargs)
            storage.delete(path)
        if self.file:
            storage, path = self.file.storage, self.file.path
            super().delete(*args, **kwargs)
            storage.delete(path)
        else:
            super().delete(*args, **kwargs)

    