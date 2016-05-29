from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListExpensesView.as_view()),
    url(r'^add/$', views.create_expense),
]
