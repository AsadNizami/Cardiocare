from django import forms

class InviteForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        fields = ['email']
