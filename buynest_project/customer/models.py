from django.db import models

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)  # Consider using Django's PasswordField or handling hashing separately
    PhoneNumber = models.CharField(max_length=20)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    LastLogin = models.DateTimeField(null=True, blank=True)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class ShippingAddress(models.Model):
    ShippingAddressID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    AddressLine1 = models.CharField(max_length=100)
    AddressLine2 = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=50)
    Region = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=20)
    Country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.AddressLine1}, {self.City}"

class Wishlist(models.Model):
    WishlistItemID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ProductID = models.ForeignKey('adminstrator.Product', on_delete=models.CASCADE)
    DateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('CustomerID', 'ProductID') # A customer can't have the same product in their wishlist twice

    def __str__(self):
        return f"{self.CustomerID} - {self.ProductID}"

class ShoppingCart(models.Model):
    CartItemID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ProductID = models.ForeignKey('adminstrator.Product', on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    DateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('CustomerID', 'ProductID') # A customer can't have the same product in their cart twice

    def __str__(self):
        return f"{self.CustomerID} - {self.ProductID} ({self.Quantity})"