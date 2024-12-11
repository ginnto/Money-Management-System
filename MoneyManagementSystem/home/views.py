from django.shortcuts import render, get_object_or_404, redirect
from .models import IncomeSource
from .forms import IncomeSourceForm

def income_list(request):
    incomes = IncomeSource.objects.filter(user=request.user)
    return render(request, 'income/income_list.html', {'incomes': incomes})

def add_income(request):
    if request.method == 'POST':
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
    else:
        form = IncomeSourceForm()
    return render(request, 'income/add_income.html', {'form': form})

def delete_income(request, pk):
    income = get_object_or_404(IncomeSource, pk=pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'income/delete_income.html', {'income': income})







#matplot 

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import IncomeSource, Expense

def income_expense_chart(request):
    # Get user-specific data
    incomes = IncomeSource.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    # Aggregate income and expenses
    income_total = sum(income.amount for income in incomes)
    expense_total = sum(expense.amount for expense in expenses)

    # Generate Matplotlib chart
    fig, ax = plt.subplots()
    labels = ['Income', 'Expenses']
    values = [income_total, expense_total]
    colors = ['#76c7c0', '#ff6f61']

    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Pass the chart to the template
    return render(request, 'analytics/income_expense_chart.html', {'chart': image_base64})



from datetime import datetime, timedelta

def income_expense_chart(request):
    # Filter data for the last month
    today = datetime.today()
    last_month = today - timedelta(days=30)
    incomes = IncomeSource.objects.filter(user=request.user, income_date__gte=last_month)
    expenses = Expense.objects.filter(user=request.user, expense_date__gte=last_month)

    # Aggregate income and expenses
    income_total = sum(income.amount for income in incomes)
    expense_total = sum(expense.amount for expense in expenses)

    # Generate Matplotlib chart
    fig, ax = plt.subplots()
    labels = ['Income', 'Expenses']
    values = [income_total, expense_total]
    colors = ['#76c7c0', '#ff6f61']

    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')

    # Save chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Pass the chart to the template
    return render(request, 'analytics/income_expense_chart.html', {'chart': image_base64})



def monthly_income_expense_chart(request):
    # Get user data and group by month
    incomes = IncomeSource.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    # Aggregate data by month
    income_data = incomes.values_list('income_date__month').annotate(total=models.Sum('amount'))
    expense_data = expenses.values_list('expense_date__month').annotate(total=models.Sum('amount'))

    # Data for the chart
    months = range(1, 13)
    income_totals = [income_data.get(month=month, default=0) for month in months]
    expense_totals = [expense_data.get(month=month, default=0) for month in months]

    # Generate Matplotlib chart
    fig, ax = plt.subplots()
    ax.bar(months, income_totals, label='Income', color='#76c7c0')
    ax.bar(months, expense_totals, label='Expenses', color='#ff6f61', bottom=income_totals)

    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.set_title('Monthly Income vs Expenses')
    ax.legend()

    # Save chart to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Pass the chart to the template
    return render(request, 'analytics/monthly_income_expense_chart.html', {'chart': image_base64})


def generate_chart(chart_type, labels, values, colors):
    fig, ax = plt.subplots()
    if chart_type == 'pie':
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
    elif chart_type == 'bar':
        ax.bar(labels, values, color=colors)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return image_base64
