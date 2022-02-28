from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'smartpet/index.html')


def pettype(request):
    # return render(request, 'smartpet/types.html')
    odalar = Room.objects.all()

    icerik = {'rooms_list_in_view': odalar}
    # rooms_list_in_view home.html template'e gönderiliyor.
    return render(request, 'base/home.html', icerik)


def petbreed(request):
    return render(request, 'smartpet/breeds.html')


def pet(request):
    return render(request, 'smartpet/pets.html')


def photo(request):
    return render(request, 'smartpet/photos.html')
