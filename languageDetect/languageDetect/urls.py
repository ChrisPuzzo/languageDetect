
from languageDetectApp.views import GetAllLanguageAPIView #, HomepageView
from django.contrib import admin
from django.urls import path, include
from languageDetectApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.HomepageView.as_view(), name='app' ),
    path('', views.getInput),
    path('api/', GetAllLanguageAPIView.as_view(), name='app' ),
]
