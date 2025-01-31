from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="app-dashboard"),
    path("form-list", views.formlist, name="app-form-list"),
    path("form", views.form, name="app-form"),
    path("", views.index, name="app-index")
]