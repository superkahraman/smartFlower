from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from smartflower.settings import STATIC_URL
from smartpet.models import Pet, petBreed, petPhoto, petType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import html
from django.views import View

from colorama import Fore, Back, Style

# My little funcs.
# This function writes colored debug message to Terminal


def myprint(mymessage):
    print(Fore.CYAN + ">>> ", end="")
    print(mymessage)
    print(Style.RESET_ALL, end="")

# Create your views here.

#########################################################
# Home Page                                             #


class HomePageView(View):
    def get(self, request):
        return render(request, 'smartpet/index.html')


#########################################################
# petTypes                                              #

class petTypesView(View):
    def get(self, request):
        pettypes = petType.objects.all()
        icerik = {'pettype_view': pettypes}
        return render(request, 'smartpet/types.html', icerik)


#########################################################
# petBreeds                                             #

class petBreedsView(View):
    def get(self, request):
        petbreeds = petBreed.objects.all()
        icerik = {'petbreed_view': petbreeds}
        return render(request, 'smartpet/breeds.html', icerik)


#########################################################
# Pets    (Shows all Pets and Search Pets)         #

def allPets(request):  # It shows all Pets
    pets = Pet.objects.all()
    icerik = {'pet_view': pets}
    return render(request, 'smartpet/pets.html', icerik)


class PetsView(View):
    def get(self, request):  # Default method is "get"
        # Returns allPets function
        return allPets(request)

# Pet Search things.

    def post(self, request):  # If FORM posted to this view.
        myprint("Post geldi")
        # searchPetName is form's input name
        searched_name = request.POST.get('searchPetName')
        # html.escape is important!!
        # if we dont do escape, visitor send anything via form.
        searched_name = html.escape(searched_name)

        if not searched_name:
            myprint("Formu boş gönderdin kro")
            return allPets(request)
        if searched_name:
            myprint("We have FORM searchPetName data : " + searched_name)
            # "name" field contains searched_name
            pets = Pet.objects.filter(name__contains=str(searched_name))
            if pets:
                messagetext = "<strong>" + searched_name + "</strong> için sonuçlar"
                # This data for HTML alert-div
                messagedata = {'type': 'info', 'message_text': messagetext}
            if not pets:
                messagetext = "<strong>'" + searched_name + "'</strong> bulunamadı."
                # This data for HTML alert-div
                messagedata = {'type': 'danger', 'message_text': messagetext}
            # We send Pets data and message for search results.
            icerik = {'pet_view': pets, 'message': messagedata}
            return render(request, 'smartpet/pets.html', icerik)


#########################################################
# PetView v2
# Tries to get Pet object.
# If Pet object does not exist, "object.filter(condition).first()" returns "None"
#
# We have or dont have "Pet.id"
# id specified in urls like that smartpet.app/pet/id
# we can get it as "id" variable together with "request" data.

class PetView(View):
    def get(self, request, id):
        pet = Pet.objects.filter(id=id).first()
        if pet == None:
            myprint("No Pet!")
            icerik = {'error_text': "Pet not found."}
            return render(request, 'smartpet/error.html', icerik)
        myprint("Pet is " + str(pet))
        photos = petPhoto.objects.filter(pet=id)
        icerik = {'pet_view': pet, 'pet_photos': photos}
        # print(pet)
        myprint(photos)
        myprint(icerik)
        return render(request, 'smartpet/pet.html', icerik)


#########################################################
# Photos                                                #

class PhotosView(View):
    def get(self, request):
        photos = petPhoto.objects.all()
        icerik = {'petphoto_view': photos}
        return render(request, 'smartpet/photos.html', icerik)


#########################################################
# Error                                                 #

class ErrorView(View):
    def get(self, request):
        icerik = {'error_text': "Bilinmeyen hata"}
        return render(request, 'smartpet/error.html', icerik)


#########################################################
# MyPets                                                #

class MyPetsView(View):
    def get(self, request):
        # if the user logged in:
        if request.user.is_authenticated:
            myprint("User: " + request.user.username)
            petowner = User.objects.get(username=request.user.username)
            pets = Pet.objects.filter(owner=petowner.id)
            myprint("Pet Owner: " + petowner.username)
            myprint(pets)
            if not pets:
                messagetext = "You dont have any Pet(s).."
                # This data for HTML alert-div
                messagedata = {'type': 'danger', 'message_text': messagetext}
            icerik = {'mypets_view': pets, 'message': messagedata}
            return render(request, 'smartpet/my_pets.html', icerik)
        else:
            # if user not logged in, go to login page.
            myprint("Please Login")
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return HttpResponseRedirect(loginurl)


class ProtectedPage(LoginRequiredMixin, View):  # Protected Page
    def get(self, request):
        # User authenticated only page view, makes automatic.
        icerik = {'protected_message': "gizli sayfaya hoşgeldiniz."}
        return render(request, 'smartpet/protected.html', icerik)


class ProtectedPageAnother(View):  # Protected2 Page
    # @login_required(login_url='/login')
    def get(self, request):
        icerik = {'protected_message': "gizli sayfaya hoşgeldiniz."}
        return render(request, 'smartpet/protected.html', icerik)
