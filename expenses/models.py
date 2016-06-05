from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Budget(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name="budgets_owned")

    # users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
    #                                related_name="budgets")

    # users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
    #                                related_name="budgets", through='BudgetUser')


class BudgetUser(models.Model):
    budget = models.ForeignKey(Budget)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    added_at = models.DateTimeField(auto_now_add=True)
    can_edit = models.BooleanField()

    class Meta:
        unique_together = (
            ('budget', 'user'),
        )


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='accounts',
                             verbose_name=_("user"))
    title = models.CharField(_("title"), max_length=200)

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return self.title


class Expense(models.Model):
    account = models.ForeignKey(Account, related_name='expenses')
    date = models.DateField(db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # TODO: add security
    photo = models.ImageField(upload_to="expenses/", null=True, blank=True)

    def __str__(self):
        return "[#{}] ${}@{} ({})".format(
            self.pk or "?",
            self.amount,
            self.date,
            self.title,
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.pk,))
