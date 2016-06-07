from django.conf.urls import url

from . import views

app_name = "expenses"
urlpatterns = [
    url(r'^$', views.ListExpensesView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.ExpenseDetailView.as_view(), name="detail"),
    url(r'^add-account/$', views.CreateAccountView.as_view(),
        name="create_account"),
    url(r'^add-expense/$', views.CreateExpenseView.as_view(), name="create"),
]
