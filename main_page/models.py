from django.db import models

# Create your models here.
class Technologies(models.Model):
    name = models.CharField(max_length=20, null=True)
    

    class Meta:
        verbose_name_plural = "Technologies"


    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField(unique=True)
    project_image = models.ImageField()
    technologies = models.ManyToManyField(Technologies)


    class Meta:
        verbose_name_plural = "Projects"

    
    def __str__(self):
        return self.name


class RecievedMessages(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name