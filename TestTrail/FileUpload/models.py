from django.db import models

# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=500,null=True)
    filepath = models.FileField(upload_to = 'files/',null=True,verbose_name='')

    def __str__(self):
        return self.name + ': ' + str(self.filepath)

class Skills(models.Model):
    pass