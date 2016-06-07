from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='accounts')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Expense(models.Model):
    account = models.ForeignKey(Account, related_name='expenses', verbose_name=_("account"))
    date = models.DateField(_("date"), db_index=True)
    amount = models.DecimalField(_("amount"), max_digits=12, decimal_places=2)
    title = models.CharField(_("title"), max_length=200)
    description = models.TextField(_("description"), null=True, blank=True)
    # TODO: add security
    photo = models.ImageField(_("photo"), upload_to="expenses/", null=True, blank=True)

    def __str__(self):
        return "[#{}] ${}@{} ({})".format(
            self.pk or "?",
            self.amount,
            self.date,
            self.title,
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.pk,))
