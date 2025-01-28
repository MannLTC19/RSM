from django.urls import path
from . import views

urlpatterns = [
    path("area-chart", views.area_chart, name="app-area-chart"),
    path("datatables", views.datatables, name="app-datatables"),
    path("form", views.form1, name="app-form1"),
    path("form2", views.form1, name="app-form2"),
    path("form3", views.form1, name="app-form3"),
    path("", views.index, name="app-index")
]