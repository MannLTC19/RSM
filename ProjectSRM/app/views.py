from django.shortcuts import render, redirect
from .forms import  ProjectForm, AssetForm
from .virustotal_service import scan_url, get_url_report
from .models import VTResult
from .models import Project,Asset
from .forms import ProjectForm, AssetForm


# Create your views here.
def index(request):
    likelihood_counts = {str(i): Asset.objects.filter(likelihood=str(i)).count() for i in range(1, 6)}
    impact_counts = {str(i): Asset.objects.filter(impact=str(i)).count() for i in range(1, 6)}

    context = {
        "projects": Project.objects.all(),
        "assets": Asset.objects.all(),
        "likelihood_counts": likelihood_counts,
        "impact_counts": impact_counts
    }
    return render(request, "index.html", context)

def area_chart(request):
    return render(request, "area_chart.html")


def formlist(request):
    return render(request, "form_list.html")

def dashboard(request):
    try:
        latest_result = VTResult.objects.latest('created_at')
        
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
        
    except VTResult.DoesNotExist:
        # Return empty chart data if no results exist
        chart_data = {
            'labels': ['Malicious', 'Suspicious', 'Harmless', 'Undetected', 'Timeout'],
            'data': [0, 0, 0, 0, 0],
            'colors': ['#FF6384', '#FFCE56', '#36A2EB', '#4BC0C0', '#9966FF']
        }
        return render(request, 'index.html', {'chart_data': chart_data})

def form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            # Store project_id in session to link with asset
            request.session['project_id'] = project.id
            return redirect('app-form2')
    else:
        form = ProjectForm()
    return render(request, 'form1.html', {'form': form})

def form2(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            project_id = request.session.get('project_id')
            if project_id:
                asset = form.save(commit=False)
                asset.project_id = str(project_id)
                asset.save(using='assets')
                del request.session['project_id']
                return redirect('app-dashboard')
            else:
                return redirect('app-form1')
    else:
        form = AssetForm()
    return render(request, 'form2.html', {'form': form})

def help(request):
    return render(request, 'help.html')

def update_project(request):
    if request.method == "POST":
        project = get_object_or_404(Project, id=request.POST["project_id"])
        project.project_title = request.POST["title"]
        project.project_owner = request.POST["owner"]
        project.process_scope = request.POST["scope"]
        project.save()
        return JsonResponse({"success": True})

def delete_asset(request):
    if request.method == "POST":
        asset = get_object_or_404(Asset, id=request.POST["asset_id"])
        asset.delete()
        return JsonResponse({"success": True})

def virus_scan(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            scan_result = scan_url(url)
            if scan_result and 'data' in scan_result:
                stats = scan_result['data']['attributes']['stats']
                results = {
                    'malicious': stats.get('malicious', 0),
                    'suspicious': stats.get('suspicious', 0),
                    'harmless': stats.get('harmless', 0),
                    'undetected': stats.get('undetected', 0),
                    'timeout': stats.get('timeout', 0),
                }

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