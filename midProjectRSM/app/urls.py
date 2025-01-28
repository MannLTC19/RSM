from django.urls import path
from . import views

urlpatterns = [
    path("area-chart", views.area_chart, name="app-area-chart"),
    path("datatables", views.datatables, name="app-datatables"),
    path("form", views.form, name="app-form1"),
    path("form2", views.form2, name="app-form2"),
    path("form3", views.form3, name="app-form3"),
    path("form4", views.form4, name="app-form4"),
    path("", views.index, name="app-index")
]