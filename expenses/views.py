import datetime
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django import forms

from . import models


class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


class ExpenseForm(forms.ModelForm):
    accept_terms_of_service = forms.BooleanField()
    class Meta:
        model = models.Expense
        exclude = (
            'date',
        )


# def create_expense(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             form.instance.date = datetime.date.today()
#             o = form.save()
#             return redirect("/")
#     else:  # GET
#         form = ExpenseForm()
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })

# class CreateExpenseView(FormView):
#     form_class = ExpenseForm
#     template_name = "expenses/expense_form.html"
#
#     def form_valid(self, form):
#         form.instance.date = datetime.date.today()
#         o = form.save()
#         return redirect("/")
#

class CreateExpenseView(CreateView):
    model = models.Expense
    # form_class = ExpenseForm
    fields = (
        'amount',
        'title',
    )

    success_url = "/" # UGLY

    def form_valid(self, form):
        form.cleaned_data['accept_terms_of_service']
        form.instance.date = datetime.date.today()
        return super().form_valid(form)
