from django.contrib import admin
from .models import IncomeSource, Expense, Asset, Liability, FinancialGoal, CashFlow, Budget

admin.site.register(IncomeSource)
admin.site.register(Expense)
admin.site.register(Asset)
admin.site.register(Liability)
admin.site.register(FinancialGoal)
admin.site.register(CashFlow)
admin.site.register(Budget)
