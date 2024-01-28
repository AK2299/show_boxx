from .models import Contact

from django import forms
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={'name','email','gender'}
        id={'arun','aru@gmail.com','male'}

