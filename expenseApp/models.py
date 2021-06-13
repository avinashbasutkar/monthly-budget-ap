from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ("needs", "Needs"),
    ("wants", "Wants"),
    ("others", "Others")
)

class Transactions(models.Model):

    itemName = models.CharField(max_length=50)
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    transactionDate = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.itemName

