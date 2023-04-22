from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    tools = models.CharField(max_length=200)
    description = models.TextField(null=True)
    project_image = models.ImageField(upload_to='images/', default="")
    project_link = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name