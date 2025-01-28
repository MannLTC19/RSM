from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def area_chart(request):
    return render(request, "area_chart.html")


def datatables(request):
    return render(request, "datatables.html")


def form(request):
    return render(request, "form1.html")

def form2(request):
    return render(request, "form2.html")