from django.db import models


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "[#{}] ${}@{} ({})".format(
            self.pk or "?",
            self.amount,
            self.date,
            self.title,
        )


