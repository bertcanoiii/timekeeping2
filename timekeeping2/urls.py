"""timekeeping2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Since we are using a customer user class/model, we need to use a custom-registration-form
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/"),
         name="django_registration_register"),

    # Login through the browser
    path('accounts/', include('django.contrib.auth.urls')),

    # Other urls used by the django_registration package
    path('accounts/', include('django_registration.backends.one_step.urls')),

    # Endpoint for current user login
    path('api/', include('users.api.urls')),

    # allows login via browsable API
    path('api-auth/', include('rest_framework.urls')),

    # allows login via REST
    path('api/rest-auth/', include('rest_auth.urls')),

    # allows registration via REST
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r'^.*$', IndexTemplateView.as_view(), name='entry-point'),

]