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
# PetView v1 - Tries to get Pet object.
# If Pet object does not exist, it cauces "error"
#


class PetView1(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        photo = petPhoto.objects.get(pet=id)
        icerik = {'pet_view': pet, 'pet_photo': photo}
        return render(request, 'smartpet/pet.html', icerik)
####################################################################
# PetView v2 - Tries to get Pet object.
# If Pet object does not exist, "object.filter(condition).first()" returns "None"
#


class PetView2(View):
    def get(self, request, id):
        pet = Pet.objects.filter(id=id).first()
        if pet == None:
            print("No Pet!")
            icerik = {'error_text': "Pet not found."}
            return render(request, 'smartpet/error.html', icerik)
        else:
            # We need to know if there is no petPhoto what will show
            # We are preparing nophoto information here.
            nophoto = STATIC_URL + 'assets/images/ghost.png'
            #
            print("Pet is " + str(pet))
            photo = petPhoto.objects.filter(pet=id).first()
            icerik = {'pet_view': pet, 'pet_photo': photo, 'no_photo': nophoto}
            # print(pet)
            # print(photo)
            return render(request, 'smartpet/pet.html', icerik)
####################################################################
# PetView v3 - Tries to get Pet object.
# If Pet object does not exist, and .get method causes to error
# We can do something via try-catch
#


class PetView3(View):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        photo = petPhoto.objects.get(pet=id)
        icerik = {'pet_view': pet, 'pet_photo': photo}
        print(pet)
        print(photo)
        return render(request, 'smartpet/pet.html', icerik)
####################################################################


class PhotosView(View):
    def get(self, request):
        photos = petPhoto.objects.all()
        icerik = {'petphoto_view': photos}
        return render(request, 'smartpet/photos.html', icerik)
