from django.db.models import Sum
from django.shortcuts import render

from . import models


def list_expenses(request):
    qs = models.Expense.objects.all()

    # total = sum(x.amount for x in qs)
    total = qs.aggregate(sum=Sum('amount'))['sum']

    return render(request, 'expenses/expense_list.html', {
        'object_list': qs,
        'total': total,
    })
