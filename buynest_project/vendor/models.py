from django.db import models

class Vendor(models.Model):
    VendorID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    ContactPerson = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    PhoneNumber = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.CompanyName

class ProductListing(models.Model):
    ProductListingID = models.AutoField(primary_key=True)
    VendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    ProductID = models.ForeignKey('adminstrator.Product', on_delete=models.CASCADE)
    ListingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    VendorSKU = models.CharField(max_length=50)
    StockQuantity = models.PositiveIntegerField(default=0)
    ListingDescription = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('VendorID', 'ProductID') # A vendor should not list the same product twice

    def __str__(self):
        return f"{self.VendorID} - {self.ProductID}"