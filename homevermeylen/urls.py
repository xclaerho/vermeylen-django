"""homevermeylen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views 
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    # other
    path('', include('home.urls'), name='home'),
    # photos
    path('gallery/', include('photos.urls'), name='photos'),
    path('photologue/',include('photologue.urls',namespace='photologue')),
    # activities
    path('activities/', include('activities.urls')),
    # augustjes
    path('augustjes/', include('augustjes.urls')),
    # input
    path('input/', include('input.urls')),
    # authentication
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # muilgraaf
    path('muilgraaf/', include('muilgraaf.urls')),
    # admin
    path('admin/', admin.site.urls),
    # users: account related
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # users: password reset urls
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
] 

admin.site.site_header = "Home Vermeylen sitebeheer"
admin.site.site_title = "Home Vermeylen"

# serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
