from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^first/$', views.first,name='first'),
    # url(r'^weather/([a-z]+)/(\d{4})/$',views.weather,name ='weather'),
    url(r'^index/$',views.BookTestView.as_view())
    # url(r'^$',views.SelectView.as_view()),
]


