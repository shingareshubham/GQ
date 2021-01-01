from django.db import models


class photo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return self.name
