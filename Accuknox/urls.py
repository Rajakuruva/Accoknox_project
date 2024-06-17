"""
URL configuration for Accuknox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from friends.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Signup/', Signup, name='Signup'),
    path('user_login/',user_login,name='user_login'),
    path('Display_profile/',Display_profile,name='Display_profile'),
    path('Show_users/', Show_users, name='Show_users'),
    path('Friend_Request/',Friend_Request,name='Friend_Request'),
    path('Messages/', Messages, name='Messages'),
    path('accept/<int:friend_request_id>/', handle_accept, name='accept'),
    path('reject/<int:friend_request_id>/', handle_reject, name='reject'),
    path('Frineds_list/',Frineds_list,name='Frineds_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
