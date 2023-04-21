from django.db import models

# Create your models here.
class Dm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'dm1_dm'
