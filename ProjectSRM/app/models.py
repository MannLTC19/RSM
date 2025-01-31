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
    residual_risk = models.CharField(max_length=50)
    existing_controls = models.TextField()
    additional_controls = models.TextField()
    review_frequency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)