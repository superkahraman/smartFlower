from django.urls import path
# from django.views.static import serve #Debug=FALSE durumunda static dosyaların erişimi için...
from . import views

# static klasöründeki öğelere erişim için.. örnek : favicon.ico
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('types', views.petTypesView.as_view(), name="urlTypes"),
    path('breeds', views.petBreedsView.as_view(), name="urlBreeds"),
    path('pets', views.PetsView.as_view(), name="urlPets"),
    path('pet/<int:id>', views.PetView.as_view(), name="urlPet"),
    path('pet/', views.ErrorView.as_view(), name="urlError"),
    path('photos', views.PhotosView.as_view(), name="urlPhotos"),
    path('photo/<str:id>', views.PhotosView.as_view(), name="urlPhoto"),

    # Static Files Definition
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")),),
]
