from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Department(models.Model):
    name = models.CharField(max_length=200)

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_items = models.IntegerField()
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    CNPJ = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    contracted_company = models.CharField(max_length=200, default="")  # add this new field
    item_service = models.CharField(max_length=1000, default="")  # add this new field
    contract_duration = models.IntegerField( default=0)
