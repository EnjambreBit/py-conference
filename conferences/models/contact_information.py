from django.db import models


class ContactInformation(models.Model):
    profile = models.OneToOneField("Profile", related_name="contact_information", on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=300, default=None, blank=True, null=True)
    address_line_2 = models.CharField(max_length=300, default=None, blank=True, null=True)
    city = models.CharField(max_length=200, default=None, blank=True, null=True)
    state = models.CharField("State/Province/Region", max_length=200, default=None, blank=True, null=True)
    zip_code = models.CharField(max_length=20, default=None, blank=True, null=True)
    country = models.ForeignKey("Country", related_name="contact_information", on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_information'
        verbose_name = "ContactInformation"
        verbose_name_plural = "contact_information"

    def __str__(self):
        return self.profile
