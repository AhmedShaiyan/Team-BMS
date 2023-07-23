from django.db import models

# Create your models here.

class Document(models.Model):
    #user = models.ForeignKey()
    name = models.CharField(max_length=500,null=True)
    filepath = models.FileField(upload_to = 'files/',null=True,verbose_name='')

    def __str__(self):
        return self.name + ': ' + str(self.filepath)

class Skills(models.Model):
    #name = models.CharField(max_length=500,null=True)
    user = models.CharField(max_length=500,null=False)
    name = models.ForeignKey(Document, default=1, null=True,on_delete=models.SET_NULL)
    skill_list = models.CharField(max_length=800,null=True)

    def __str__(self):
        return self.skill_list

class JobRec(models.Model):
    user = models.CharField(max_length=500,null=False)
    user_skills = models.ForeignKey(Skills,default=1,null=False,on_delete=models.CASCADE)
    job_recs = models.CharField(max_length=1000,null=True)
    