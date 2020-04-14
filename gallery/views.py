from django.shortcuts import render

from .models import Image

def gallery(request):
    photos = Image.objects
    return render(request, "photos/gallery.html", {'photos':photos})
