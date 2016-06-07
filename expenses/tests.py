import datetime
import decimal

import random
from django.contrib.auth.models import User
from django.test import TestCase

from . import models


class ExpensesTestCase(TestCase):
    def test_expenses(self):
        users = [User.objects.create_user(
            "user #{}".format(i + 1)) for i in range(5)]

        n = 12
        for i in range(n):
            o = models.Expense(
                user=random.choice(users),
                date=datetime.date(2016, 1, i + 1),
                title="Expense #{}".format(i + 1),
                amount=(i + 1) * decimal.Decimal("10.10"),
            )
            o.full_clean()
            o.save()

        self.assertEquals(models.Expense.objects.count(), n)
