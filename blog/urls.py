from django.conf.urls import url

from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/like/$', views.PostLikeView.as_view(), name="like"),
]
