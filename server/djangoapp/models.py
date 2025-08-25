from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    
    # Dealer Id referring to dealer in Cloudant DB
    dealer_id = models.IntegerField()
    

    name = models.CharField(max_length=100)

    # Limited choices for type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # Year as DateField (only storing year)
    year = models.DateField()
   
   

    # Optional field
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year.year})"
