from django.db import models
from django.core.exceptions import ValidationError

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} on {self.date_time}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.fitness_class.available_slots <= 0:
                raise ValidationError("No available slots in this class.")
            self.fitness_class.available_slots -= 1
            self.fitness_class.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"
