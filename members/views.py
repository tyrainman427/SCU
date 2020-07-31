from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member, Address, Membership
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from .forms import MemberUpdateForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth import update_session_auth_hash
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


def index(request):
    # post = Post.objects.filter(status=1).order_by('-created_on')
    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(post, 2)
    # try:
    #     post = paginator.page(page)
    # except PageNotAnInteger:
    #     post = paginator.page(1)
    # except EmptyPage:
    #     post = paginator.page(paginator.num_pages)

    context = {}
    return render(request,'members/index.html',context)


def about(request):
    return render(request, 'members/about.html')

def program(request):
    return render(request, 'members/programs.html')

def founders(request):
    return render(request, 'members/founders.html')

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
