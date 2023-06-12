"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.urls.conf import include  # <-- Make sure you have both of these imports.

from django.contrib.auth.views import LoginView, LogoutView

from .views import Home  # Added for Assignment 09

urlpatterns = [
    path("blogging/", include("blogging.urls")),  # <-- Added this
    path("polling/", include("polling.urls")),  # <-- Added this
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  # Added for Assignment 09
# NOTE - Following line seems to no longer be necessary
# was causing an error about access to 127.0.0.1
#   path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("", Home.as_view(), name="home"),
]
# 21da26e61303a9d25de5 Client ID for GIT
# 6413111d074ea033e5e17d465ad22c679beca76e Client Secret