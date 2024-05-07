from django.db import models
from django.utils import timezone

# Create your models here.


class VisitorProfile(models.Model):
    login = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.login


class Zone(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    number = models.AutoField(primary_key=True)
    visitor_id = models.ForeignKey(VisitorProfile, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=3600)

    def __str__(self):
        return self.number


class TicketZone(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_id) + ": " + str(self.zone_id)
