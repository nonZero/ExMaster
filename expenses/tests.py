import datetime
import decimal

from django.test import TestCase

from . import models


class ExpensesTestCase(TestCase):
    def test_expenses(self):
        n = 12
        for i in range(n):
            o = models.Expense(
                date=datetime.date(2016, 1, i + 1),
                title="Expense #{}".format(i + 1),
                amount=(i + 1) * decimal.Decimal("10.10"),
            )
            o.full_clean()
            o.save()

        self.assertEquals(models.Expense.objects.count(), n)
