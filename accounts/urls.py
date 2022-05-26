from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/<str:username>/', views.profile, name='profile'),
    path('accounts/<str:username>/updateprofile/', views.update_profile, name='update_profile'),
    path('accounts/userdelete/', views.userdelete, name='userdelete'),
]

