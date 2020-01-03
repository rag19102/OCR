from django.db import models

class Upload:
    img = models.ImageField(upload_to='media')
# Create your models here.
