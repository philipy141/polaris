from rest_framework import serializers
from .models import Category, Department, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'date', 'amount', 'number_of_items', 'cost_per_item', 'CNPJ', 'category', 'department', 'contracted_company', 'item_service']
