from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BudgetItem, BudgetHeader

class BudgetItemListView(ListView):
    model = BudgetItem
    template_name = 'budget/budgetlist.html'