from django.db import models

# Create your models here.
class Uploadimage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateField(auto_now_add=True)

class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    uemail = models.EmailField()
    ucontact = models.CharField(max_length=15)

    class Meta:
        db_table = "user"
