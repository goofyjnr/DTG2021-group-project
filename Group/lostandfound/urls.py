"""Group URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('lost<int:lost_id>/',views.detail, name='detail'),
    path('found<int:found_id>/',views.detail_2, name='detail_2'),
    path('search/', views.search, name = 'search'),
    path('lost_items/', views.lost_items, name='lost_items'),
    path('Found_items/', views.Found_items, name='Found_items')
]
