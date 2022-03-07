from email.mime import application
from django.urls import path, include
# from django.views.static import serve #Debug=FALSE durumunda static dosyaların erişimi için...
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls


# static klasöründeki öğelere erişim için.. örnek : favicon.ico
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
app_name = 'smartpet'
urlpatterns = [
    path('', views.HomeView.as_view(), name="urlHome"),
    path('types', views.petTypesView.as_view(), name="urlTypes"),
    path('breeds', views.petBreedsView.as_view(), name="urlBreeds"),
    path('pets/', views.PetsView.as_view(), name="urlPets"),
    path('pet/<int:id>', views.PetView.as_view(), name="urlPet"),
    path('pet/', views.ErrorView.as_view(), name="urlError"),
    path('photos', views.PhotosView.as_view(), name="urlPhotos"),
    path('photo/<str:id>', views.PhotosView.as_view(), name="urlPhoto"),

    # login required pages

    path('mypets', views.MyPetsView.as_view(), name="urlMyPets"),
    path('protected', views.ProtectedPage.as_view(), name="urlProtected"),
    path('protected2', views.ProtectedPageAnother.as_view(),
         name="urlProtectedAnother"),

    # Static Files Definition
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")),),
]
