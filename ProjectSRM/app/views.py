from django.shortcuts import render, redirect
from .forms import RiskAssessmentForm
from .virustotal_service import scan_url, get_url_report
from .models import VTResult

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

def help(request):
    return render(request, 'help.html')

def virus_scan(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            scan_result = scan_url(url)
            if scan_result and 'data' in scan_result:
                # Format the results for better display
                stats = scan_result['data']['attributes']['stats']
                results = {
                    'malicious': stats.get('malicious', 0),
                    'suspicious': stats.get('suspicious', 0),
                    'harmless': stats.get('harmless', 0),
                    'undetected': stats.get('undetected', 0),
                    'timeout': stats.get('timeout', 0),
                }
                
                # Save results to MongoDB
                vt_result = VTResult(
                    scanned_url=url,
                    malicious=results['malicious'],
                    suspicious=results['suspicious'],
                    harmless=results['harmless'],
                    undetected=results['undetected'],
                    timeout=results['timeout']
                )
                vt_result.save()
                
                return render(request, 'virus_scan_result.html', {
                    'report': results,
                    'url': url
                })
            return render(request, 'virus_scan.html', {
                'error': 'Failed to scan URL. Please try again.'
            })
        except Exception as e:
            return render(request, 'virus_scan.html', {
                'error': f'Error scanning URL: {str(e)}'
            })
    return render(request, 'virus_scan.html')

def dashboard(request):
    # Ambil data terbaru dari MongoDB
    latest_result = VTResult.objects.latest('created_at')
    
    # Siapkan data untuk Donut Chart
    chart_data = {
        'labels': ['Malicious', 'Suspicious', 'Harmless', 'Undetected', 'Timeout'],
        'data': [
            latest_result.malicious,
            latest_result.suspicious,
            latest_result.harmless,
            latest_result.undetected,
            latest_result.timeout
        ],
        'colors': ['#FF6384', '#FFCE56', '#36A2EB', '#4BC0C0', '#9966FF']
    }
    
    return render(request, 'index.html', {'chart_data': chart_data})
