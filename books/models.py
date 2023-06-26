from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

import uuid


User = get_user_model()

class Book(models.Model):
    """This class is for save books."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})
    

class Review(models.Model):
    """This class is for comment to under book post."""


    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.review
