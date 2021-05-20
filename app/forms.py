from django import forms
from .models import Test
from django.utils.translation import gettext_lazy as _


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        labels = {
            'cp': _('Chest Pain'),
            'trestbps': _('Resting Blood Pressure in mm Hg (50-200)'),
            'chol': _('Serum Cholesterol (150-400)'),
            'restecg': _('Resting Electrocardiographic Result'),
            'thalach': _('Maximum Heart Rate Achieved (50-200)'),
            'exang': _('Exercise Induced Angina'),
            'oldpeak': _('ST depression induced by exercise relative to rest (0-10)'),
            'slope': _('The slope of the peak exercise ST segment (0-5)'),
            'ca': _('Number of major vessels colored by flouroscopy'),
            'thal': _('Thalassemia (Blood Disorder)')
        }
