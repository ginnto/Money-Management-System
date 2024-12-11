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
