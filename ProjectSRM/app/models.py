from django.db import models

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_owner = models.CharField(max_length=200)
    process_scope = models.TextField()
    asset_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Projects'
        app_label = 'app'

class Asset(models.Model):
    project_id = models.CharField(max_length=200)  # Changed from ForeignKey to CharField
    asset_name = models.CharField(max_length=200)
    asset_owner = models.CharField(max_length=200)
    primary_threats = models.TextField()
    asset_description = models.TextField()
    likelihood = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Assets'
        app_label = 'app'

class VTResult(models.Model):
    scanned_url = models.URLField(max_length=2000)
    malicious = models.IntegerField(default=0)
    suspicious = models.IntegerField(default=0)
    harmless = models.IntegerField(default=0)
    undetected = models.IntegerField(default=0)
    timeout = models.IntegerField(default=0)
    scan_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'VT_Result'
