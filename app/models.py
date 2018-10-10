from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rate(models.Model):
    rater = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey('app.Project',on_delete=models.CASCADE,related_name='rates')
    design = models.PositiveIntegerField(default=0)
    usability = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.rater.username


class Project(models.Model):
    title = models.CharField(max_length = 60)
    homepage = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    link = models.CharField(max_length = 60)
    rating = models.ForeignKey(Rate, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title
#
# class Profile(models.Model):
#     name = models.ForeignKey(User,on_delete=models.CASCADE )
#     profile_pic = models.ImageField(upload_to = 'images/')
#     bio = models. TextField()
#     projects = models.ForeignKey(Project, on_delete=models.CASCADE)
#     contact = models.TextField()
#
#     def __str__(self):
#         return self.name.username
