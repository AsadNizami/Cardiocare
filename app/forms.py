from django import forms
from .models import Test
from django.utils.translation import gettext_lazy as _


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        labels = {
            'cp': _('Chest Pain (0-3)'),
            'trestbps': _('Resting Blood Pressure in mm Hg'),
            'chol': _('Serum Cholestoral'),
            'restecg': _('Resting Electrocardiographic Result (0-2)'),
            'thalach': _('Maximum Heart Rate Achieved'),
            'exang': _('Exercise Induced Angina'),
            'oldpeak': _('ST depression induced by exercise relative to rest'),
            'slope': _('The slope of the peak exercise ST segment'),
            'ca': _('Number of major vessels (0-3) colored by flouroscopy'),
            'thal': _('Thalassemia (Blood Disorder)')
        }
