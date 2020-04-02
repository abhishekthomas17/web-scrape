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
from django.urls import path,include
from webscrape import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('sports/',views.sports,name='sports'),
    path('sports/cricket/mens/',views.cricket,name='cricket'),
    path('sports/cricket/mens/news',views.cricket_news,name='cricket_news'),
    path('sports/cricket/mens/odi/',views.mens_odi,name='mensodi'),
    path('sports/cricket/mens/test/',views.mens_test,name='menstest'),
    path('sports/cricket/mens/t20/',views.mens_t20,name='menst20'),
    path('sports/cricket/mens/player-ranking-odi/',views.player_ranking_odi,name='player_ranking_odi'),
    path('sports/cricket/mens/player-ranking-test/',views.player_ranking_test,name='player_ranking_test'),
    path('sports/cricket/mens/player-ranking-t20/',views.player_ranking_t20,name='player_ranking_t20'),
    path('sports/cricket/mens/player-ranking-odi/batting/',views.player_ranking_odi_batting,name='player_ranking_odi_batting'),
    path('sports/cricket/mens/player-ranking-odi/bowling/',views.player_ranking_odi_bowling,name='player_ranking_odi_bowling'),
    path('sports/cricket/mens/player-ranking-odi/all-rounder/',views.player_ranking_odi_all_rounder,name='player_ranking_odi_all_rounder'),
    path('sports/cricket/mens/player-ranking-test/batting/',views.player_ranking_test_batting,name='player_ranking_test_batting'),
    path('sports/cricket/mens/player-ranking-test/bowling/',views.player_ranking_test_bowling,name='player_ranking_test_bowling'),
    path('sports/cricket/mens/player-ranking-test/all-rounder/',views.player_ranking_test_all_rounder,name='player_ranking_test_all_rounder'),
    path('sports/cricket/mens/player-ranking-t20/batting/',views.player_ranking_t20_batting,name='player_ranking_t20_batting'),
    path('sports/cricket/mens/player-ranking-t20/bowling/',views.player_ranking_t20_bowling,name='player_ranking_t20_bowling'),
    path('sports/cricket/mens/player-ranking-t20/all-rounder/',views.player_ranking_t20_all_rounder,name='player_ranking_t20_all_rounder'),

    path('sports/', include('tennis.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL1, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL3, document_root=settings.MEDIA_ROOT)
