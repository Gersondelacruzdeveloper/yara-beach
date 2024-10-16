"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('api/', include('api.urls')),
    path('excursions/', include('excursions.urls')),
    path('admin/', admin.site.urls),
    path('rentals/', include('rentals.urls')),
    path('administrator/', include('administrator.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('blog/', include('blog.urls')),
    # accounts for Users
    path('accounts/', include('allauth.urls')),
    #ckeditor_uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
# if the page does not exist will through 
handler404 = 'home.views.page_not_found'
handler500 = 'home.views.server_error'
# media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

