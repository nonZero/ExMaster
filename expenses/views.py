import datetime

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Sum
from django.shortcuts import redirect
from django.utils.encoding import escape_uri_path
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from . import forms
from . import models


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('expenses:list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None and user.is_active:
            login(self.request, user)
            if self.request.GET.get('from'):
                return redirect(
                    self.request.GET['from'])  # SECURITY: check path
            return redirect('expenses:list')

        form.add_error(None, "Invalid user name or password")
        return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class LoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            url = reverse("login") + "?from=" + escape_uri_path(request.path)
            return redirect(url)
        return super().dispatch(request, *args, **kwargs)


class ListExpensesView(LoggedInMixin, ListView):
    page_title = "Home"
    model = models.Expense

    def get_queryset(self):
        return super().get_queryset().filter(account__user=self.request.user)

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


class ExpenseDetailView(LoggedInMixin, DetailView):
    page_title = "Detail"
    model = models.Expense

    def get_queryset(self):
        return super().get_queryset().filter(account__user=self.request.user)


class CreateAccountView(LoggedInMixin, CreateView):
    page_title = "Add New Account"
    model = models.Expense
    form_class = forms.AccountForm

    success_url = reverse_lazy('expenses:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateExpenseView(LoggedInMixin, CreateView):
    page_title = "Add New Expense"
    model = models.Expense
    fields = (
        'account',
        'date',
        'amount',
        'title',
        'description',
        'photo',
    )

    # success_url = reverse_lazy('expenses:list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.fields['account'].queryset = models.Account.objects.filter(
        #     user=self.request.user)
        form.fields['account'].queryset = form.fields[
            'account'].queryset.filter(
            user=self.request.user)
        return form

    def get_initial(self):
        d = super().get_initial()
        d['date'] = datetime.date.today()
        return d

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
