from django.db import models

# Create your models here.

class Form(models.Model):
    id=models.AutoField(primary_key=True)
    location = models.CharField(max_length=256)
    indes = models.CharField(max_length=256)
    dtinc = models.DateTimeField()
    incloc = models.CharField(max_length=256)
    insev=models.CharField(max_length=256)
    suscau=models.CharField(max_length=256)
    imactk=models.CharField(max_length=256)
    repby=models.CharField(max_length=256)

    class Meta:
        db_table = "Form"

