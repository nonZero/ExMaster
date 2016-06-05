import silly
from django.core.management.base import BaseCommand

from expenses import models


class Command(BaseCommand):
    help = 'Adds a silly expense'

    def handle(self, *args, **options):
        o = models.Expense.objects.create(
            account=models.Account.objects.order_by("?").first(),
            amount=silly.number() * 100,
            date=silly.datetime().date(),
            title=silly.sentence(),
        )
        print(o.id)
        print(o.title)
