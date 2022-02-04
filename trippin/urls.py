"""trippin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from trippin import settings

from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
   )
from query import views as views
from query import views_authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # send username, password to get “refresh” and the “access” tokens as a response
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('login', views.login_view),

    path('login/', views.login_view),
    path('register', views_authentication.register, name="register"),
    path('', include('query.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

