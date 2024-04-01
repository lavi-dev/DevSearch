from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.profiles,name='profiles'),
    path('user/<str:pk>/',views.userProfile,name='user-profile'),
]