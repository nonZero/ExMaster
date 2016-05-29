from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListExpensesView.as_view(), name="list"),
    url(r'^add/$', views.CreateExpenseView.as_view(), name="create"),
]
