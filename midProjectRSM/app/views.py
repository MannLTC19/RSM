
from django.shortcuts import render, redirect
from .forms import RiskAssessmentForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def area_chart(request):
    return render(request, "area_chart.html")


def formlist(request):
    return render(request, "form_list.html")

def dashboard(request):
    return render(request, "index.html")

def form(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-dashboard')
    else:
        form = RiskAssessmentForm()
    return render(request, 'form1.html', {'form': form})

def form2(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-dashboard')
    else:
        form = RiskAssessmentForm()
    return render(request, 'form2.html', {'form': form})

def form3(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-dashboard')
    else:
        form = RiskAssessmentForm()
    return render(request, 'form3.html', {'form': form})

def form4(request):
    if request.method == 'POST':
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-dashboard')
    else:
        form = RiskAssessmentForm()
    return render(request, 'form4.html', {'form': form})