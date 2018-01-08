"""HistoryTimeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from timeline.views import TimelineView, CountryView

router = routers.DefaultRouter()
router.register(r'timeline', TimelineView)
router.register(r'country', CountryView)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path(r'', include(router.urls)),
    path('schema/', schema_view),
    path(r'docs/', include_docs_urls('历史轴')),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
