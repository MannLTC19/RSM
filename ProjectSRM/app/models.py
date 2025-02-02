from django.db import models

class RiskAssessment(models.Model):
    project_title = models.CharField(max_length=200)
    project_owner = models.CharField(max_length=200)
    process_scope = models.TextField()
    primary_threats = models.TextField()
    critical_assets = models.TextField()
    vulnerabilities = models.TextField()
    asset_description = models.TextField()
    likelihood = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)
    existing_controls = models.TextField()
    additional_controls = models.TextField()
    review_frequency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class VTResult(models.Model):
    scanned_url = models.URLField(max_length=2000)
    malicious = models.IntegerField(default=0)
    suspicious = models.IntegerField(default=0)
    harmless = models.IntegerField(default=0)
    undetected = models.IntegerField(default=0)
    timeout = models.IntegerField(default=0)
    scan_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'VT_Result'
