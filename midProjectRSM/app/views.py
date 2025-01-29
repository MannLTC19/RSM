from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def area_chart(request):
    return render(request, "area_chart.html")


def formlist(request):
    return render(request, "form_list.html")


def form(request):
    return render(request, "form1.html")

def form2(request):
    return render(request, "form2.html")

def form3(request):
    return render(request, "form3.html")

def form4(request):
    return render(request, "form4.html")