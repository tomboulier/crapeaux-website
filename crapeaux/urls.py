from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accueil', views.index, name='accueil'),
    path('a-propos', views.apropos, name="a-propos"),
    path('en-construction', views.en_construction, name="en-construction"),
    path('calendrier', views.en_construction, name="en-construction"),
    path('blog', views.en_construction, name="en-construction"),
    path('contact', views.en_construction, name="en-construction"),
    path('en-construction', views.en_construction, name="en-construction"),
]

handler404 = "crapeaux.views.page_not_found_view"
