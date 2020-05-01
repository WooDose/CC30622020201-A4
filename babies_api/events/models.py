from django.db import models
from datetime import datetime

class Event(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    event_type = models.CharField(max_length=80, default='N/A')
    baby = models.ForeignKey(
        'babies_app.Baby',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.CharField(max_length=800, default="N/A")


    def __str__(self):
        return 'En la fecha {}, ocurrio un evento de {} para el bebe {}. Observaciones: {}'.format(self.date, self.event_type, self.baby, self.notes)