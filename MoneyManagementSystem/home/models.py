from django.db import models
from django.contrib.auth.models import User

class IncomeSource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_date = models.DateField()
    income_type = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Passive', 'Passive')])
    created_at = models.DateTimeField(auto_now_add=True)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    type = models.CharField(max_length=50, choices=[('Real Estate', 'Real Estate'), ('Stocks', 'Stocks'), ('Business', 'Business')])
    created_at = models.DateTimeField(auto_now_add=True)

class Liability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)
    current_savings = models.DecimalField(max_digits=15, decimal_places=2)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class CashFlow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    total_income = models.DecimalField(max_digits=15, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=15, decimal_places=2)
    cash_flow = models.DecimalField(max_digits=15, decimal_places=2)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
