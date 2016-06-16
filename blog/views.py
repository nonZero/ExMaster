from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView

from blog import forms
from expenses.views import LoggedInMixin
from . import models


class PostListView(ListView):
    model = models.Post


class PostDetailView(LoggedInMixin, DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        d['form'] = forms.CommentForm()
        return d

    def post(self, request, *args, **kwargs):
        parent = self.get_object()
        form = forms.CommentForm(request.POST)
        form.instance.post = parent
        form.instance.user = request.user
        form.save()
        messages.success(request, "Comments saved.")
        return redirect(parent)
