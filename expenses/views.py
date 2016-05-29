from django.db.models import Sum
from django.views.generic.list import ListView

from . import models

class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']
