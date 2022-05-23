from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/<username>/', views.profile, name='profile'),
    path('accounts/<username>/createprofile/', views.create_profile, name='create_profile'),
    path('accounts/<username>/updateprofile/', views.update_profile, name='update_profile'),
    path('accounts/<int:user_pk>/follow/', views.follow, name='follow'),
]

