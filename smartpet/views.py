from django.http import HttpResponse
from django.shortcuts import render
from smartflower.settings import STATIC_URL
from smartpet.models import Pet, petBreed, petPhoto, petType

from django.views import View
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'smartpet/index.html')


class petTypesView(View):
    def get(self, request):
        pettypes = petType.objects.all()
        icerik = {'pettype_view': pettypes}
        return render(request, 'smartpet/types.html', icerik)


class petBreedsView(View):
    def get(self, request):
        petbreeds = petBreed.objects.all()
        icerik = {'petbreed_view': petbreeds}
        return render(request, 'smartpet/breeds.html', icerik)


class PetsView(View):
    def get(self, request):
        pets = Pet.objects.all()
        icerik = {'pet_view': pets}
        return render(request, 'smartpet/pets.html', icerik)

# We have or dont have "Pet.id"
# id specified in urls like that smartpet.app/pet/id
# we can get it as "id" variable together with "request" data.


####################################################################
# PetView v2 - Tries to get Pet object.
# If Pet object does not exist, "object.filter(condition).first()" returns "None"
#

class PetView(View):
    def get(self, request, id):
        pet = Pet.objects.filter(id=id).first()
        if pet == None:
            print("No Pet!")
            icerik = {'error_text': "Pet not found."}
            return render(request, 'smartpet/error.html', icerik)
        print("Pet is " + str(pet))
        photos = petPhoto.objects.filter(pet=id)
        icerik = {'pet_view': pet, 'pet_photos': photos}
        # print(pet)
        print(photos)
        print(icerik)
        return render(request, 'smartpet/pet.html', icerik)


class PhotosView(View):
    def get(self, request):
        photos = petPhoto.objects.all()
        icerik = {'petphoto_view': photos}
        return render(request, 'smartpet/photos.html', icerik)


class ErrorView(View):
    def get(self, request):
        icerik = {'error_text': "Bilinmeyen hata"}
        return render(request, 'smartpet/error.html', icerik)
