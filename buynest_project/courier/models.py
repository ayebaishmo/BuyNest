from django.db import models

class Courier(models.Model):
    CourierID = models.AutoField(primary_key=True)
    CourierName = models.CharField(max_length=100)
    ContactEmail = models.EmailField(blank=True, null=True)
    ContactPhone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.CourierName

class Shipment(models.Model):
    ShipmentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('adminstrator.Order', on_delete=models.CASCADE)
    CourierID = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)
    TrackingNumber = models.CharField(max_length=100, unique=True)
    ShipmentDate = models.DateTimeField(auto_now_add=True)
    EstimatedDeliveryDate = models.DateTimeField(null=True, blank=True)
    ActualDeliveryDate = models.DateTimeField(null=True, blank=True)
    ShipmentStatus = models.CharField(max_length=50)

    def __str__(self):
        return f"Shipment #{self.ShipmentID} for Order #{self.OrderID}"