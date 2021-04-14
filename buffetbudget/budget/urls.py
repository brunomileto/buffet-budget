from django.urls import path
from .views import BudgetItemListView

urlpatterns = [
    path("", BudgetItemListView.as_view(), name="budgets_list"),
    #path("budgets/<int:pk>", bot_detail, name="bot_detail")
]