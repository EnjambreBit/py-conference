from django.db import models


class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, default=None, blank=True, null=True)
    address_line_2 = models.CharField(max_length=200, default=None, blank=True, null=True)
    city = models.CharField(max_length=200, default=None, blank=True, null=True)
    state = models.CharField(max_length=200, default=None, blank=True, null=True)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, null=True, blank=True)
    zipcode = models.CharField(max_length=100, default=None, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=None, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=None, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'addresses'
        verbose_name = "Address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return self.nombre
