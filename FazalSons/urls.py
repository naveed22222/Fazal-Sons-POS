"""
URL configuration for FazalSons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from AppAccount.views import *

urlpatterns = [
                  # path('', LoginAPIView.as_view(), name='LoginView'),
                  path('admin/', admin.site.urls),
                  path('pos/products', include('AppProduct.urls')),
                  path('pos/customer', include('AppCustomer.urls')),
                  path('pos/stock', include('AppStock.urls')),
                  path('pos/login', include('AppAccount.urls')),
                  path('pos/transaction', include('AppPOS.urls')),
                  path('pos/report', include('AppReport.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')), ### For Django Debug Toolbar
    ] + urlpatterns


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
