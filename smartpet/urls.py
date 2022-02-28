from django.urls import path
# from django.views.static import serve #Debug=FALSE durumunda static dosyaların erişimi için...
from . import views

# static klasöründeki öğelere erişim için.. örnek : favicon.ico
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name="home_page"),
]
