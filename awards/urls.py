from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers, serializers, viewsets
# from django.contrib.auth.models import User

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^search/', views.search_projects, name='search_results'),
    url(r'^project/(\d+)', views.get_project, name='project_results'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)