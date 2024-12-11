from django.urls import path
from . import views

urlpatterns = [
    # Dashboard and Analytics Home
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),

    # Income vs Expense Pie Chart
    path('analytics/income-expense-chart/', views.income_expense_chart, name='income_expense_chart'),

    # Monthly Income vs Expenses Bar Chart
    path('analytics/monthly-income-expense/', views.monthly_income_expense_chart, name='monthly_income_expense_chart'),

    # User Management
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/profile/', views.user_profile, name='user_profile'),

    # Income Management
    path('income/add/', views.add_income, name='add_income'),
    path('income/list/', views.list_income, name='list_income'),
    path('income/edit/<int:id>/', views.edit_income, name='edit_income'),
    path('income/delete/<int:id>/', views.delete_income, name='delete_income'),

    # Expense Management
    path('expense/add/', views.add_expense, name='add_expense'),
    path('expense/list/', views.list_expense, name='list_expense'),
    path('expense/edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),

    # Bank Account Management
    path('bank-account/add/', views.add_bank_account, name='add_bank_account'),
    path('bank-account/list/', views.list_bank_accounts, name='list_bank_accounts'),
    path('bank-account/edit/<int:id>/', views.edit_bank_account, name='edit_bank_account'),
    path('bank-account/delete/<int:id>/', views.delete_bank_account, name='delete_bank_account'),

    # Budget Planning
    path('budget/set/', views.set_budget, name='set_budget'),
    path('budget/view/', views.view_budget, name='view_budget'),

    # Reports and Analytics
    path('reports/monthly/', views.monthly_report, name='monthly_report'),
    path('reports/quarterly/', views.quarterly_report, name='quarterly_report'),
    path('reports/yearly/', views.yearly_report, name='yearly_report'),
]
