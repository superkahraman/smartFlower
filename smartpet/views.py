from django.shortcuts import render

from smartpet.models import Pet, petBreed, petPhoto, petType

# Create your views here.


def home(request):
    return render(request, 'smartpet/index.html')


def pettypes(request):
    # return render(request, 'smartpet/types.html')
    pettypes = petType.objects.all()
    icerik = {'pettype_view': pettypes}
    return render(request, 'smartpet/types.html', icerik)


def petbreeds(request):
    # return render(request, 'smartpet/breeds.html')
    petbreeds = petBreed.objects.all()
    icerik = {'petbreed_view': petbreeds}
    return render(request, 'smartpet/breeds.html', icerik)


def pets(request):
    # return render(request, 'smartpet/pets.html')
    pets = Pet.objects.all()
    icerik = {'pet_view': pets}
    return render(request, 'smartpet/pets.html', icerik)


def photos(request):
    # return render(request, 'smartpet/photos.html')
    photos = petPhoto.objects.all()
    icerik = {'petphoto_view': photos}
    return render(request, 'smartpet/photos.html', icerik)
