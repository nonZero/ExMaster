import datetime
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django import forms

from . import models


class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


# class ExpenseForm(forms.Form):
#     date = forms.DateField(widget=forms.widgets.Input(attrs={'type': 'date'}))
#     amount = forms.DecimalField(max_digits=12, decimal_places=2)
#     title = forms.CharField(max_length=300)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = (
            'date',
        )
        # fields = (
        #     'title',
        #     'amount',
        # )


# def create_expense(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             o = models.Expense(**form.cleaned_data)
#             o.full_clean()
#             o.save()
#             return redirect("/")
#     else:  # GET
#         form = ExpenseForm()
#     return render(request, "expenses/expense_form.html", {
#         'form': form,
#     })


def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.instance.date = datetime.date.today()
            o = form.save()
            return redirect("/")
    else:  # GET
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })
