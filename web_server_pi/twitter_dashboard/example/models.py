from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Many to Many Programmer - Language
class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
        
class Framework (models.Model):
    
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null= False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50, null=False)

class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True)
    coupon_code = models.CharField(max_length=50, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)

'''
    how to store many to many objects
    p = Programmer(...)
    l1 = Language(...)
    l2 = Language(...)
    P.language.add(l1)
    P.language.add(l2)
    l1.programmer_set.all() # _set does a reverse look up
    p.language.all()

    result = Framework.objects.filter(language__name__iexact='java') 
    
'''
