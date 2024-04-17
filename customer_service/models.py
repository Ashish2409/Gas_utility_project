from django.db import models

# Create your models here.

from django.db import models


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submission_time = models.DateTimeField(auto_now_add=True)
    resolution_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.type
    class Meta:
        app_label = 'customer_service'

