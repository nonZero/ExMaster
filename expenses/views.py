from django.db.models import Sum
from django.shortcuts import render
from django.views.generic.list import ListView
from django import forms

from . import models


class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']




def create_expense(request):
    if request.method == "POST":
        assert False, request.POST
    return render(request, "expenses/expense_form.html")