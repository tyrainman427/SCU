from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Address, Member, Contact

class MemberUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ['first_name','last_name']
  
def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')      

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    forcefield = forms.CharField(required=False, widget=forms.HiddenInput,label="Leave empty", validators=[should_be_empty])
  
    
    class Meta:
        model = Contact
        fields = "__all__"
       