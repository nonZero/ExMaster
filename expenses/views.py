from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from . import models

class ListExpensesView(ListView):
    model = models.Expense

    def total(self):
        return self.get_queryset().aggregate(sum=Sum('amount'))['sum']


# def list_expenses(request):
#     qs = models.Expense.objects.all()
#
#     # total = sum(x.amount for x in qs)
#     total = qs.aggregate(sum=Sum('amount'))['sum']
#
#     return render(request, 'expenses/expense_list.html', {
#         'object_list': qs,
#         'total': total,
#     })

# class ListExpensesView(View):
#     def get(self, request):
#         qs = models.Expense.objects.all()
#
#         # total = sum(x.amount for x in qs)
#         total = qs.aggregate(sum=Sum('amount'))['sum']
#
#         return render(request, 'expenses/expense_list.html', {
#             'object_list': qs,
#             'total': total,
#         })

# class ListExpensesView(TemplateView):
#     template_name = 'expenses/expense_list.html'
#
#     def get_context_data(self, **kwargs):
#         d = super().get_context_data(**kwargs)
#
#         qs = models.Expense.objects.all()
#
#         # total = sum(x.amount for x in qs)
#         total = qs.aggregate(sum=Sum('amount'))['sum']
#
#         d.update({
#             'object_list': qs,
#             'total': total,
#         })
#
#         return d



    # def get_context_data(self, **kwargs):
    #     d = super().get_context_data(**kwargs)
    #
    #     total = self.get_queryset().aggregate(sum=Sum('amount'))['sum']
    #
    #     d.update({
    #         'total': total,
    #     })
    #
    #     return d

    # def get_context_data(self, **kwargs):
    #     d = super().get_context_data(**kwargs)
    #
    #     total = self.get_queryset().aggregate(sum=Sum('amount'))['sum']
    #
    #     d.update({
    #         'total': total,
    #     })
    #
    #     return d
    #


