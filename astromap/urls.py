from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("ping/", views.ping, name="ping"),
    path("map/", views.map_view, name="map_view")
]
