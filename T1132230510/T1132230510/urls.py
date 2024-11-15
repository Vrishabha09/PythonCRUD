"""
URL configuration for T1132230510 project.

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
from Vrishabha import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', views.admin_home, name='admin_home'),
    path('admin/add_movie/', views.add_movie, name='add_movie'),
    path('admin/update_movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('admin/delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('',views.index,name="index"),
    path('display/',views.display,name="display"),
    path('trailor/',views.trailor,name="trailor"),
    #path('upload/', views.upload_movie, name="upload_movie"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
