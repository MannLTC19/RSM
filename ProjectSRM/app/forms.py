from django import forms
from .models import Project, Asset

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_owner', 'process_scope', 'asset_description']
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            'project_owner': forms.TextInput(attrs={'class': 'form-control'}),
            'process_scope': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class AssetForm(forms.ModelForm):
    LIKELIHOOD_CHOICES = [
        ('1', 'Very Low'),
        ('2', 'Low'),
        ('3', 'Medium'),
        ('4', 'High'),
        ('5', 'Very High'),
    ]

    IMPACT_CHOICES = [
        ('1', 'Very Low'),
        ('2', 'Low'),
        ('3', 'Medium'),
        ('4', 'High'),
        ('5', 'Very High'),
    ]

    likelihood = forms.ChoiceField(choices=LIKELIHOOD_CHOICES, widget=forms.RadioSelect)
    impact = forms.ChoiceField(choices=IMPACT_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Asset
        fields = ['asset_name', 'asset_owner', 'primary_threats', 'asset_description', 'likelihood', 'impact']
        widgets = {
            'asset_name': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_owner': forms.TextInput(attrs={'class': 'form-control'}),
            'primary_threats': forms.Textarea(attrs={'class': 'form-control'}),
            'asset_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

# Legacy form - can be removed if not needed
class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = Project  # Changed from RiskAssessment to Project
        fields = ['project_title', 'project_owner', 'process_scope', 'asset_description']
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            'project_owner': forms.TextInput(attrs={'class': 'form-control'}),
            'process_scope': forms.TextInput(attrs={'class': 'form-control'}),
            'asset_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }