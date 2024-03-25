from django.db import models
import os
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books', blank=True)
    pages = models.IntegerField()
    file = models.FileField(upload_to='books', blank=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Delete the associated image and file when a Book instance is deleted
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

    def save(self, *args, **kwargs):
        # Delete old image and file if they are being updated
        if self.pk:
            old_book = Book.objects.get(pk=self.pk)
            if self.image and old_book.image and self.image != old_book.image:
                storage, path = old_book.image.storage, old_book.image.path
                storage.delete(path)
            if self.file and old_book.file and self.file != old_book.file:
                storage, path = old_book.file.storage, old_book.file.path
                storage.delete(path)
        
        super().save(*args, **kwargs)
        
    
    
    
    

    
