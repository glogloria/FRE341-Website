from django.urls import path
from apps.public import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("gallery/", views.gallery, name="gallery"),
    path("video/", views.video, name="video"),
]