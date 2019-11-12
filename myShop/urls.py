from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('store/<slug>', store, name="store"),
    path('item_details/<slug>', item_details, name="item_details"),
    path('contact', contact, name="contact"),
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('users/', users, name="users"),
    path('logout/', logout_user, name="logout"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='pages/password_reset.html'),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='pages/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done',
         auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html'),
         name='password_reset_complete'),
    path('search_results', search_results, name='search_results'),
]
