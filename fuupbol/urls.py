"""neurorehabilitation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from userprofiles.views import (UserViewSet,)
from games_information.views import (FieldViewSet, TeamViewSet, MatchViewSet)


from .views import home, home_files


# Router provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'fields', FieldViewSet)
#router.register(r'trainingcompetitioncenter', TrainingCompetitionCenterViewSet)
router.register(r'matchs', MatchViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),

    #  which is a regular expression that takes the desired urls and passes as an argument
    # the filename, i.e. robots.txt or humans.txt.
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),

    # Wire up our API using automatic URL routing.
    url(r'^api/', include(router.urls)),


    # If you're intending to use the browsable API you'll probably also want to add REST framework's
    # login and logout views.
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
