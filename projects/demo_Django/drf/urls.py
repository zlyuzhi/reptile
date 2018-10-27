from django.conf.urls import url
from . import views

# eg:url(r'^book/$',views.BookView.as_view()),
urlpatterns = [
    url(r'^books/$',views.BooksView.as_view()),
    # url(r'^book/(?P<pk>\d+)/$',views.BookView.as_view())
    url(r'^book/(?P<pk>\d+)/$',views.BookView.as_view()),
    url(r'^heros/$',views.HerosAPIView.as_view()),
    url(r'^hero/(?P<pk>\d+)/$',views.HeroAPIView.as_view())

]
