import datetime

from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . import models


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
