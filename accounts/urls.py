from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/createprofile/', views.create_profile, name='create_profile'),
    path('<username>/updateprofile/', views.update_profile, name='update_profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

