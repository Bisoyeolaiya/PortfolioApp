from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='img', default='img/client.png', blank=True, null=True)

    def __str__(self):
        return self.title