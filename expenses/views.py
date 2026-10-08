from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense

def home(request):
    expenses=Expense.objects.all()
    return render(request, 'expenses/home.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request,id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('home')

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit_expense.html', {'form': form})
# Create your views here.
