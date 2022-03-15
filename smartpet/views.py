#from email import message
from django.http import HttpResponseRedirect  # ,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse  # , include
from django.utils.http import urlencode
from smartflower.settings import STATIC_URL
from smartpet.models import Pet, petBreed, petPhoto, petType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
import html
from django.views import View
from smartpet.config import *

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
    xx("[PetsView](allPets) starting...")
    pets = Pet.objects.all()
    xx(pets)
    icerik = {'pet_view': pets}
    xx("[PetsView](allPets) ending...")
    return render(request, 'smartpet/pets.html', icerik)


def searchPets(request, searched_name):
    xx("[PetsView](searchPets) starting..")

    # "name" field contains searched_name
    pets = Pet.objects.filter(name__contains=str(searched_name))
    if pets:
        xx("[PetsView](searchPets) found something for '"+searched_name+"'")
        xx(pets)
        xx("[PetsView](searchPets) creating 'info' message...")
        messages.info(request, "Results...")
        messages.error(request, "Erol..")
        messagetext = "<strong>" + searched_name + "</strong> için sonuçlar"
        # This data for HTML alert-div
        messagedata = {'type': 'info', 'message_text': messagetext}
    if not pets:
        xx("[PetsView](searchPets) NOT found for '"+searched_name+"'")
        xx("[PetsView](searchPets) creating 'danger' message...")

        messagetext = "<strong>'" + searched_name + "'</strong> bulunamadı."
        # This data for HTML alert-div
        messagedata = {'type': 'danger', 'message_text': messagetext}
        # We send Pets data and message for search results.
    icerik = {'pet_view': pets, 'message': messagedata}
    xx("[PetsView](searchPets) returning...")
    return render(request, 'smartpet/pets.html', icerik)


class PetsView(View):
    def get(self, request):  # Default method is "get"
        # Returns allPets function
        xx("[PetsView](GET) starting...")
        searched_name = request.session.get('searched_pet', False)
        xx("[PetsView](GET) searched_name=session['searched_pet']")
        xx("[PetsView](GET) searched_name=='" + str(searched_name)+"'")

        if searched_name:
            xx("[PetsView](GET)<searched_name> condition starting...")
            xx("[PetsView](GET) deleting session['searched_pet']")
            del(request.session['searched_pet'])
            xx(
                "[PetsView](GET)<searched_name> searchPets('"+searched_name + "')")
            return searchPets(request, searched_name)
        else:
            searched_name = None
            xx("[PetsView](GET) session['searched_pet'] not found ")
            xx("[PetsView](GET) return allPets(request)")
            return allPets(request)

    def post(self, request):  # If FORM posted to this view.
        xx("[PetsView](POST) received.")
        # searchPetName is form's input name
        searched_name = request.POST.get('searchPetName')
        # html.escape is important!!
        # if we dont do escape, visitor send anything via form.
        searched_name = html.escape(searched_name)
        xx("[PetsView](POST) searched_name=='" + searched_name + "'")

        # Redirect searched_name to Session's "searched_pet"
        # We gonna process search result as GET (not POST)

        if not searched_name:
            xx("[PetsView](POST) searched_name is 'None'")
            xx("[PetsView](POST) is redirecting to (GET).")
            return redirect(request.path)
        if searched_name:
            request.session['searched_pet'] = searched_name
            xx("[PetsView](POST) session['searched_pet']='" + searched_name+"'")
            xx("[PetsView](POST) is redirecting to (GET).")
            return redirect(request.path)  # Redirect to itself for GET


#########################################################
# PetView v2
# Tries to get Pet object.
# If Pet object does not exist, "object.filter(condition).first()" returns "None"
#
# We have or dont have "Pet.id"
# id specified in urls like that smartpet.app/pet/id
# we can get it as "id" variable together with "request" data.


class SinglePetView(View):
    def get(self, request, id):
        try:
            pet = Pet.objects.filter(id=id).first()
            if pet == None:
                xx("No Pet!")
                icerik = {'error_text': "Pet not found."}
                return render(request, 'smartpet/error.html', icerik)
            xx("Pet is " + str(pet))
            photos = petPhoto.objects.filter(pet=id)
            icerik = {'pet_view': pet, 'pet_photos': photos}
            # print(pet)
            xx(photos)
            xx(icerik)
            return render(request, 'smartpet/pet.html', icerik)
        except:
            icerik = {'error_text': "hatalı sollama"}
            return render(request, 'smartpet/error.html', icerik)


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
            xx("User: " + request.user.username)
            petowner = User.objects.get(username=request.user.username)
            pets = Pet.objects.filter(owner=petowner.id)
            xx("Pet Owner: " + petowner.username)
            xx(pets)
            messagedata = None
            if not pets:
                messagetext = "You dont have any Pet(s).."
                # This data for HTML alert-div
                messagedata = {'type': 'danger', 'message_text': messagetext}
            icerik = {'mypets_view': pets, 'message': messagedata}
            return render(request, 'smartpet/my_pets.html', icerik)
        else:
            # if user not logged in, go to login page.
            xx("Please Login")
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
