from django.urls import path
# from django.views.static import serve #Debug=FALSE durumunda static dosyaların erişimi için...
from . import views

# static klasöründeki öğelere erişim için.. örnek : favicon.ico
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="home_page"),
    path('types/', views.pettypes, name="urlTypes"),
    path('breeds/', views.petbreeds, name="urlBreeds"),
    path('pets/', views.pets, name="urlPets"),
    path('pet/<str:id>', views.pets, name="urlPet"),
    path('photos/', views.photos, name="urlPhotos"),
    path('photo/<str:id>', views.photos, name="urlPhoto"),

    # Static Files Definition
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")),),
]
