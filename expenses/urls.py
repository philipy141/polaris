from django.urls import path
from .views import DailyExpensesView, WeeklyExpensesView, MonthlyExpensesView, SpecificMonthExpensesView, DailyAggregateExpensesView

urlpatterns = [
    path('daily', DailyExpensesView.as_view(), name='daily_expenses'),
    path('weekly', WeeklyExpensesView.as_view(), name='weekly_expenses'),
    path('monthly', MonthlyExpensesView.as_view(), name='monthly_expenses'),
    path('<int:year>/<int:month>', SpecificMonthExpensesView.as_view(), name="specific_month_expenses"),
    path('daily-aggregate', DailyAggregateExpensesView.as_view(), name='daily_aggregate_expenses'),
    path('daily-aggregate/<int:year>/<int:month>/<int:day>', DailyAggregateExpensesView.as_view(), name='specific_day_aggregate_expenses'),


]
