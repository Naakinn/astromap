from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('favicon.ico',RedirectView.as_view(url='/static/img/favicon.ico')),
    
    path("", views.index_view, name="index_view"),
    path("ping/", views.ping, name="ping"),
    path("map/", views.map_view, name="map_view"),
    path("quiz/", views.quiz_view, name="quiz_view")
]
