import datetime

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

    success_url = "/"  # UGLY

    def form_valid(self, form):
        form.cleaned_data['accept_terms_of_service']
        form.instance.date = datetime.date.today()
        return super().form_valid(form)
