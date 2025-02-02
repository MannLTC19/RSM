from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="app-dashboard"),
    path("area-chart", views.area_chart, name="app-area-chart"),
    path("form-list", views.formlist, name="app-form-list"),
    path("form", views.form, name="app-form1"),
    path("form2", views.form2, name="app-form2"),
    path("help", views.help, name="app-help"),
    path("virus-scan", views.virus_scan, name="app-virus-scan"),
    path("", views.index, name="app-index")
]