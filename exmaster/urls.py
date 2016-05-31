from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import expenses.views

urlpatterns = [
    url(r'', include('expenses.urls')),
    url(r'^login/$', expenses.views.LoginView.as_view(), name='login'),
    url(r'^logout/$', expenses.views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
