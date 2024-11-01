from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('conference', 'Conference'),
        ('concert', 'Concert'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar')
    ]

    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    capacity = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])



class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user} booked {self.event}"
