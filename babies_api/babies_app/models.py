from django.db import models

class Baby(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'parents_app.Parent',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def get_baby_parent(self):
        return self.parent.first_name
        
    def __str__(self):
        return "Child " + self.first_name + " for parent " + self.parent.first_name