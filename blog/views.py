from django.views.generic import DetailView
from django.views.generic.list import ListView

from . import models


class PostListView(ListView):
    model = models.Post


class PostDetailView(DetailView):
    model = models.Post
