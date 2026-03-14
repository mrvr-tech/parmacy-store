from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('store', 'Store'),
        ('lab', 'Lab'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    lab_name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"


class StoreItem(models.Model):
    CATEGORY_CHOICES = (
        ('chemicals', 'Chemicals'),
        ('glassware', 'Glassware'),
        ('instruments', 'Instruments'),
        ('computer', 'Computer Store'),
        ('other', 'Other'),
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=200)
    packages = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., 500mg, 1L, 100 tablets")
    quantity = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()
    bill_no = models.CharField(max_length=100)
    date = models.DateField()
    expiry_date = models.DateField()
    vendor_name = models.CharField(max_length=200)
    vendor_address = models.TextField()
    vendor_pan = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name


class LabRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    
    lab_name = models.CharField(max_length=50)
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    approved_quantity = models.IntegerField(default=0)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return f"{self.lab_name} - {self.item.item_name}"
