from django.conf.urls import url, include
from django.contrib import admin

import expenses.views

urlpatterns = [
    url(r'', include('expenses.urls')),
    url(r'^login/$', expenses.views.LoginView.as_view(), name='login'),
    url(r'^logout/$', expenses.views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
]
