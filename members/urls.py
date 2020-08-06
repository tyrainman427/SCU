from django.urls import path
from django.urls import re_path
from .views import MemberList,profile, MemberDetailView,ActivateAccount,SignUpView,index,program,founders, MemberCreateView, MemberUpdateView, MemberDeleteView,privacy,about,contact, employee_portal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView



app_name = 'members'

urlpatterns = [
    path('', index, name='index'),
    path('members/profile/', profile, name='profile'),
    path('privacy/', privacy, name='privacy'),
    path('about/', about, name='about'),
    path('contact/', contact,name='contact'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('members/<int:id>/', MemberDetailView.as_view(), name='members_detail'),
    path('create/', MemberCreateView.as_view(), name='member-create'),
    path('members/<int:id>/update/', MemberUpdateView, name='member-update'),
    path('members/<pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    path('portal/', employee_portal, name='portal'),
    path('programs/', program, name='programs'),
    path('founders/', founders, name='founders'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(),{'next_page': '/'}, name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('accounts/password_reset/',PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]
