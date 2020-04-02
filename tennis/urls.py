"""scrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tennis/',views.tennis,name='tennis'),
    path('tennis/mens',views.tennis_mens_rankings,name='tennis-mens-rankings'),

    path('tennis/mens_doubles',views.tennis_mens_doubles,name='tennis-mens-doubles'),
    path('tennis/womens_doubles',views.tennis_womens_doubles,name='tennis-womens-doubles'),
    path('tennis/womens',views.tennis_womens_rankings,name='tennis-womens-rankings'),
    path('tennis/news',views.tennis_news,name='tennis-news'),


]
urlpatterns += static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT)
