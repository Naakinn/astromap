from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("ping/", views.ping, name="ping"),
    path("group0/", views.group0_view, name="group0_view"),
    path("group1/", views.group1_view, name="group1_view"),
    path("group2/", views.group2_view, name="group2_view"),
    path("group3/", views.group3_view, name="group3_view"),
    path("group4/", views.group4_view, name="group4_view"),
    path("group5/", views.group5_view, name="group5_view")
]
