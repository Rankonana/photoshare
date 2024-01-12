from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Photo(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.folder) + str(self.image)
