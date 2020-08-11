from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Address, Profile
from django.urls import reverse,reverse_lazy
from django.conf import settings
from .forms import ContactForm, SignUpForm, ProfileUpdateForm,AddressUpdateForm, UserUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth import update_session_auth_hash
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.utils.encoding import force_bytes
from django.utils.decorators import method_decorator


# def signup(request):
#     form = SignupForm()
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             ######################### mail system ####################################
#             htmly = get_template('members/email.html')
#             d = { 'username': username }
#             subject = 'Welcome to SCU'
#             html_content = htmly.render(d)
#             from_email = "no-reply@silvercityuprising.org"
#             to = email
#             form.save()
#
#             try:
#                 send_mail(subject, html_content, from_email, [to],username)
#                 return render(request,'members/signup.html',{'username':username})
#             except BadHeaderError:
#                 return HttpResponse("Invalid headers")
#         else:
#             form = SignupForm()
#             return HttpResponse("The header was invalid")
#
#     return render(request, 'members/signup.html', {'form': form})
#
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


def login(request):
    user = authenticate(username=username, password=password)
    if user is not None:
    # Password verified for user
        if user.is_active:
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')
    return render(request, 'accounts/login.html')

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'members/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            human = True

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your SCU Account'
            message = render_to_string('members/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('/accounts/login')
        else:
            message = "You have enter an incorrect captcha. Please try again."
            messages.error(request,message)

        return render(request, self.template_name, {'form': form})

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            print("made user")
            user.is_active = True
            user.profile.email_confirmed = True
            print("email confirmed")
            user.save()
            login(request, user)
            messages.success(request, ('Your account has been confirmed.'))
            return redirect('/accounts/login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('/')

def index(request):
    return render(request,'members/index.html',{})


def about(request):
    return render(request, 'members/about.html')

def privacy(request):
    return render(request, 'members/privacy.html')

def volunteer(request):
    return render(request, 'members/volunteer.html')

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        address_form = AddressUpdateForm(request.POST,instance=request.user.address)

        if user_form.is_valid() and profile_form.is_valid() and address_form.is_valid():
            user_form.save()
            profile_form.save()
            address_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('members:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        address_form = AddressUpdateForm()

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'address_form':address_form
    }

    return render(request, 'members/profile.html', context)

def program(request):
    return render(request, 'members/programs.html')

def founders(request):
    return render(request, 'members/founders.html')

def contact(request):
    form = ContactForm(data=request.POST or None)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True
            subject = f'Subject: {form.cleaned_data["subject"]}'
            message = f'Message: {form.cleaned_data["message"]}'
            sender = "no-reply@silvercityuprising.org"
            name = f'Name: {form.cleaned_data["name"]}'
            email = f'Email: {form.cleaned_data["email"]}'

            msg_mail = str(name) + " " + str(email) + " " + str(message)


            try:
                send_mail(subject, msg_mail, sender, ['support@silvercityuprising.org',],fail_silently=False)

                return render(request,'members/contact.html',{'name':name})
            except BadHeaderError:
                return HttpResponse("Invalid headers")

        else:
            # form = ContactForm()
            message = "You have enter an incorrect captcha. Please try again."
            messages.error(request,message)

    return render(request, 'members/contact.html',{'form':form})






#
# def signup(request):
#     return render(request, 'members/member_signup.html')
@login_required
def employee_portal(request):
    return render(request,'employee/index.html')


# class MemberList(ListView):
#     model = Member
#     model = Address
#     queryset = Member.objects.all()
#     address = Address.objects.all()
#     template_name = 'members/member_list.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)


# class MemberDetailView(DetailView):
#     template_name = "members/member_detail.html"
#     member = Member.objects.all()
#     # form_class = MemberUpdateForm
#
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Member, id=id_)
#
#     def form_valid(self,form):
#         return super().form_valid(form)
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#
# class MemberCreateView(CreateView):
#     model = Member
#     fields = ['first_name', 'last_name','phone_number','email_address',
#      "date_of_birth"
#     ]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# class MemberDeleteView(DeleteView):
#     model = Member
#     success_url = '/members/'
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
