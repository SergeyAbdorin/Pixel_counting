from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("result/<int:image_id>/", views.result, name='result')
]
