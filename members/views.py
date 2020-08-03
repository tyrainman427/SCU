from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member, Address, Membership
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from .forms import MemberUpdateForm, ContactForm,NewsletterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth import update_session_auth_hash
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


def index(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            form.save()

            try:

                return render(request,'members/index.html',{'first_name':first_name})
            except BadHeaderError:
                return HttpResponse("Invalid headers")
        else:
            form = NewsletterForm()
            return HttpResponse("The header was invalid")

    context = {'form':form}
    return render(request,'members/index.html',context)


def about(request):
    return render(request, 'members/about.html')

def privacy(request):
    return render(request, 'members/privacy.html')

def program(request):
    return render(request, 'members/programs.html')

def founders(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            form.save()

            try:

                return render(request,'members/index.html',{'first_name':first_name})
            except BadHeaderError:
                return HttpResponse("Invalid headers")
        else:
            form = NewsletterForm()
            return HttpResponse("The header was invalid")

    context = {'form':form}
    return render(request, 'members/founders.html',context)

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Subject: {form.cleaned_data["subject"]}'
            message = f'Message: {form.cleaned_data["message"]}'
            from_email = "no-reply@silvercityuprising.org"
            to = ['support@silvercityuprising.org',]
            name = form.cleaned_data["name"]
            email = f'Email: {form.cleaned_data["email"]}'

            try:
                send_mail(subject, message, from_email, to,name,email)

                return render(request,'members/contact.html',{'name':name})
            except BadHeaderError:
                return HttpResponse("Invalid headers")
        else:
            form = ContactForm()
            return HttpResponse("The header was invalid")

    return render(request, 'members/contact.html',{'form':form})







def signup(request):
    return render(request, 'members/member_signup.html')

def employee_portal(request):
    return render(request,'employee/index.html')

class MemberList(ListView):
    model = Member
    model = Address
    queryset = Member.objects.all()
    address = Address.objects.all()
    template_name = 'members/member_list.html'


class MemberDetailView(DetailView):
    template_name = "members/member_detail.html"
    member = Member.objects.all()
    form_class = MemberUpdateForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Member, id=id_)

    def form_valid(self,form):
        return super().form_valid(form)


class MemberCreateView(CreateView):
    model = Member
    fields = ['first_name', 'last_name','phone_number','email_address',
    ]

@login_required
class MemberUpdateView(UpdateView):
    model = Member
    fields = ['first_name', 'last_name','email_address',
    ]

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/members/'
