from django import forms
from .models import RiskAssessment

class RiskAssessmentForm(forms.ModelForm):
    LIKELIHOOD_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    IMPACT_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    likelihood = forms.ChoiceField(
        choices=LIKELIHOOD_CHOICES,
        widget=forms.RadioSelect,
        label="Likelihood"
    )
    
    impact = forms.ChoiceField(
        choices=IMPACT_CHOICES,
        widget=forms.RadioSelect,
        label="Impact"
    )

    class Meta:
        model = RiskAssessment
        fields = '__all__'  # Include all fields or specify which ones you want