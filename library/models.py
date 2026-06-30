from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(
        max_length=200
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    biography = models.TextField(
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_deleted = models.BooleanField(
        default=False
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name