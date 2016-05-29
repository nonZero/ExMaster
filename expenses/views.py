import datetime

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from . import forms
from . import models


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "login.html"

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect('expenses:list')

        form.add_error(None, "Invalid user name or password")
        return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


class CreateExpenseView(CreateView):
    model = models.Expense
    # form_class = ExpenseForm
    fields = (
        'amount',
        'title',
    )

    success_url = reverse_lazy('expenses:list')

    def form_valid(self, form):
        form.instance.date = datetime.date.today()
        return super().form_valid(form)
