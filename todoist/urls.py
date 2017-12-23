from django.conf.urls import url 
from . import views
from django.http import Http404

app_name ='todoist'
urlpatterns = [
	url(r'^$', views.index, name='base'),
	]