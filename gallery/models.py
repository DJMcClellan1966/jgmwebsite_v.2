from django.db import models



class Image(models.Model):
    photo = models.ImageField(upload_to='images/')
    pub_date = models.DateField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Album(models.Model):
    title = models.CharField(max_length=250)
    images= models.ManyToManyField(Image, blank=True, related_name='image_albums')
    highlight = models.OneToOneField(Image, null=True, blank=True,
                                    on_delete=models.CASCADE,)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
