from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDERS = (
        ("man", "Man"),
        ("woman", "Woman"),
        ("nonbinary", "Nonbinary"),
        ("prefer no say", "Prefer no say"),
        ("other", "Other"),
    )
    DOCUMENTS_TYPE = (
        ("passport", "Passport"),
        ("dni", "Documento Nacional de Identidad"),
        ("cuit/cuil", "CUIT/CUIL"),
    )

    user = models.OneToOneField(
        User, related_name="profile", null=True, blank=True, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    nickname = models.CharField(max_length=100, default=None, blank=True, null=True)
    gender = models.CharField(
        max_length=100, choices=GENDERS, default=None, blank=True, null=True
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey(
        "Country", on_delete=models.CASCADE, null=True, blank=True
    )
    document_type = models.CharField(
        max_length=100, choices=DOCUMENTS_TYPE, default=None, blank=True, null=True
    )
    document_number = models.CharField(
        max_length=100, default=None, blank=True, null=True
    )
    birth_date = models.DateField(default=None, blank=True, null=True)
    company = models.CharField(max_length=100, default=None, blank=True, null=True)
    job_title = models.CharField(max_length=100, default=None, blank=True, null=True)
    institution_name = models.CharField(
        max_length=100, default=None, blank=True, null=True
    )
    study_program = models.CharField(
        max_length=100, default=None, blank=True, null=True
    )
    student_id = models.CharField(max_length=50, default=None, blank=True, null=True)

    address = models.OneToOneField(
        "Address",
        on_delete=models.CASCADE,
        related_name="profile",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "Profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    @property
    def email(self):
        if self.user:
            return self.user.email
        return None

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
