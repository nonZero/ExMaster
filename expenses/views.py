from django.shortcuts import render

from . import models

def list_expenses(request):

    qs = models.Expense.objects.all()

    return render(request, 'expenses/expense_list.html', {
        'object_list': qs,
    })
