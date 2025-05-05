from django.db import models

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)
    ParentCategoryID = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.CategoryName

class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=100)
    LogoURL = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.BrandName

class Promotion(models.Model):
    PromotionID = models.AutoField(primary_key=True)
    PromotionName = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    DiscountType = models.CharField(max_length=20, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Amount')])
    DiscountValue = models.DecimalField(max_digits=10, decimal_places=2)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.PromotionName

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)
    SKU = models.CharField(max_length=50, unique=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CategoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    BrandID = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    Image = models.ImageField(upload_to='products/', blank=True, null=True) # Ensure you have Pillow installed
    DateAdded = models.DateTimeField(auto_now_add=True)
    LastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class OrderStatus(models.Model):
    OrderStatusID = models.AutoField(primary_key=True)
    StatusName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.StatusName

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    TransactionID = models.CharField(max_length=100, unique=True)
    PaymentMethod = models.CharField(max_length=50)
    PaymentDate = models.DateTimeField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentStatus = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.PaymentMethod} - {self.TransactionID}"

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    OrderDate = models.DateTimeField(auto_now_add=True)
    OrderStatusID = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    ShippingAddressID = models.ForeignKey('customer.ShippingAddress', on_delete=models.SET_NULL, null=True, related_name='shipping_orders')
    BillingAddressID = models.ForeignKey('customer.ShippingAddress', on_delete=models.SET_NULL, null=True, related_name='billing_orders')
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentID = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.OrderID} - {self.CustomerID}"

class OrderItem(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.Quantity} x {self.ProductID.Name} in Order #{self.OrderID}"