from django.contrib import admin
from django.urls import path, include
from . import views, user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),
    path('404', views.PAGE_NOT_FOUND, name='404'),
    path('', views.HOME, name='home'),
    path('challenges', views.SINGLE_CHALLENGE, name='single_challenge'),
    path('product/filter-data', views.filter_data, name="filter-data"),
    path('challenge/<slug:slug>', views.CHALLENGE_DETAILS, name='challenge_details'),
    path('challenge/', views.CHALLENGE_START, name='start_challenge'),
    path('resources/', views.RESOURCES, name='resources'),
    path('submit', views.CHALLENGE_SUBMIT, name='submit'),
    path('my-challenge', views.MY_CHALLENGES, name='my-challenges'),
    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),

    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profiles', user_login.PROFILES, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
