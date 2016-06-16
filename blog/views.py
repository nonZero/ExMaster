import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import View
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

        if request.POST.get('like'):
            # ADD/REMOVE LIKE
            assert False, "LIKE"
        else:
            # ADD COMMENT
            form = forms.CommentForm(request.POST)
            if not form.is_valid():
                return JsonResponse({
                    'errors': json.loads(form.errors.as_json()),
                }, status=400)
            form.instance.post = parent
            form.instance.user = request.user
            form.save()
            if request.is_ajax():
                # return JsonResponse({'status': 'ok'})
                return render(request, "blog/_comment.html", {
                    'comment': form.instance,
                })
            messages.success(request, "Comments saved.")
            return redirect(parent)


class PostLikeView(LoggedInMixin, View):
    def post(self, request, *args, **kwargs):
        parent = get_object_or_404(models.Post, id=kwargs['pk'])
        # parent = models.Post.objects.get(id=kwargs['pk'])
        # ADD/REMOVE LIKE
        assert False, "LIKE"

# class MyView(View):
#     def get(self, request, *args, **kwargs):
#
#         return JsonResponse({'data': [
#             {'x':123, 'y': i} for i in range(100, 1000, 20)]})
