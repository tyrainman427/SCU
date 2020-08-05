from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from captcha.fields import CaptchaField

from .models import Address, Member, Contact


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=200, help_text='Required')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

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
    captcha = CaptchaField(label='Verification code',error_messages={'invalid': "Verification code error"})
    forcefield = forms.CharField(required=False, widget=forms.HiddenInput,label="Leave empty", validators=[should_be_empty])


    class Meta:
        model = Contact
        fields = "__all__"
