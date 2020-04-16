from django.db import models



class Image(models.Model):
    photo = models.ImageField(upload_to='images/')
    pub_date = models.DateField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def __img__(self):
        return self.image

class Album(models.Model):
    title = models.CharField(max_length=250)
    images= models.ManyToManyField(Image, blank=True)
    

    def __str__(self):
        return self.title
