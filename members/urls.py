from django.urls import path
from django.urls import re_path
from .views import MemberList, MemberDetailView, index,program,founders, MemberCreateView, MemberUpdateView, MemberDeleteView, signup,about,contact, employee_portal
from django.contrib.auth.decorators import login_required


app_name = 'members'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('about/', about, name='about'),
    path('contact/', contact,name='contact'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('<int:id>/', MemberDetailView.as_view(), name='members_detail'),
    path('create/', MemberCreateView.as_view(), name='member-create'),
    path('<int:id>/update/', MemberUpdateView, name='member-update'),
    path('members/<pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    path('portal/', employee_portal, name='portal'),
    path('programs/', program, name='programs'),
    path('founders/', founders, name='founders')
    
]
