"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as uploader_views
from django.views.decorators.cache import never_cache
from rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    path('', include('myside.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('ckeditor/upload/', login_required(uploader_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(uploader_views.browse)), name='ckeditor_browse'),
    path('mycvs/', include('mycvs.urls')),

    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
    path('api/auth/registration/', RegisterView.as_view(), name='account_signup'),
    re_path('api/auth/account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path('api/auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
        
  #  path('api/auth/login', )
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
