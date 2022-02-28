from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'smartpet/index.html')

 
def pettype(request):
    return render(request, 'smartpet/types.html')


def petbreed(request):
    return render(request, 'smartpet/breeds.html')


def pet(request):
    return render(request, 'smartpet/pets.html')


def photo(request):
    return render(request, 'smartpet/photos.html')