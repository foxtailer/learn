from os import name
from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/edit', views.ProfileEditView.as_view(), name='profile_edit'),
    path('accounts/password/edit', views.PasswordEditView.as_view(), name='password_edit'),
    path('accounts/register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/activate/<str:sign>/', views.user_activate, name='activate'),
    path('<str:page>/', views.other_page, name='other_page'),
    path('', views.index, name='index')
]
