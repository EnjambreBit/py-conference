from statistics import mode
from django.db import models


class Grant(models.Model):
    STATUS = (
        ("requested", "Requested"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("approbed", "Approbed"),
    )
    TYPES = (
        ("transport", "Transport"),
        ("housing", "Housing"),
        ("food", "Food"),
        ("other", "Other"),
    )
    CURRENCIES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ("ARS", "Pesos Argentinos"),
        ("BRL", "Real"),
    )
    profile = models.ForeignKey(
        "Profile", related_name="grants", on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        "Event",
        related_name="grants",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    status = models.CharField(max_length=20, choices=STATUS, default="requested")
    type = models.CharField(max_length=20, choices=TYPES, default="other")
    reasons = models.TextField(default=None, blank=True, null=True)
    request_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default="ARS", choices=CURRENCIES)
    usd_exchanged_rate = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    approbed_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    approbed_date = models.DateField(default=None, null=True, blank=True)
    approbed_by = models.ForeignKey(
        "Profile",
        related_name="grants_approbed",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    paid_date = models.DateField(default=None, null=True, blank=True)
    paid_by = models.ForeignKey(
        "Profile",
        related_name="grants_paid",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "grants"
        verbose_name = "Grant"
        verbose_name_plural = "grants"

    def __str__(self):
        return f"{self.profile} - {self.request_amount} {self.currency}"

    def request_amount_str(self):
        return f"{self.request_amount} {self.currency}"

    def approbed_amount_str(self):
        if self.approbed_amount:
            return f"{self.approbed_amount} {self.currency}"
        return f"0.0 {self.currency}"
    
    def paid(self):
        if self.paid_date:
            return True
        return False
    paid.boolean = True