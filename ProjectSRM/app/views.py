from django.shortcuts import render, redirect
from .forms import RiskAssessmentForm

# Create your views here.
def index(request):
    return render(request, "index.html")

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
    return render(request, 'form.html', {'form': form})
