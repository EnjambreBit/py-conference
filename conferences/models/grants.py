from django.db import models


class Grant(models.Model):
    STATUS = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('approbed', 'Approbed'),
    )
    TYPES = (
        ('transport', 'Transport'),
        ('housing', 'Housing'),
        ('food', 'Food'),
        ('other', 'Other'),
    )
    profile = models.ForeignKey("Profile", related_name="grants", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='requested')
    type = models.CharField(max_length=20, choices=TYPES, default='other')
    reasons = models.TextField(default=None, blank=True, null=True)
    request_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    approbed_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    approbed_date = models.DateField(default=None, null=True, blank=True)
    approbed_by = models.ForeignKey("Profile", related_name="grants_approbed", on_delete=models.CASCADE, null=True, blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(default=None, null=True, blank=True)
    paid_by = models.ForeignKey("Profile", related_name="grants_paid", on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'grants'
        verbose_name = "Grant"
        verbose_name_plural = "grants"

    def __str__(self):
        return str(self.profile)
