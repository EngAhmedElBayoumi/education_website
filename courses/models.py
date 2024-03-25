from django.db import models
#user
from django.contrib.auth.models import User
#import rich text field
from ckeditor.fields import RichTextField
# Create your models here.

#grade choices for the courses we have four grades 
grade_choices=(
    ('1st year','1st year'),
    ('2nd year','2nd year'),
    ('3rd year','3rd year'),
    ('4th year','4th year'),
)

#department choices for the courses we have five departments (computer , technology , art , music , economics)
department_choices=(
    ('Computer','Computer'),
    ('Technology','Technology'),
    ('Art','Art'),
    ('Music','Music'),
    ('Economics','Economics'),
)

class courses(models.Model):
    instructor=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='courses', blank=True)
    description=models.TextField()
    grade=models.CharField(max_length=100, choices=grade_choices)
    department=models.CharField(max_length=100, choices=department_choices)
    duration=models.CharField(max_length=100)
    skill_level=models.CharField(max_length=100)
    over_view=RichTextField()
    
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

    # delete file on update and change the file
    def save(self, *args, **kwargs):
        try:
            this = courses.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(courses, self).save(*args, **kwargs)
    
        
class Lectures(models.Model):
    course=models.ForeignKey(courses, on_delete=models.CASCADE, related_name='lectures')
    title=models.CharField(max_length=100)
    link=models.URLField()
    
    def __str__(self):
        return self.title
    
    