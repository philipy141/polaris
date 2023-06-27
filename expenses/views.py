from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from datetime import timedelta
from django.db.models import Q
from django.db.models import Sum


class DailyExpensesView(APIView):
    def get(self, request):
        today = timezone.now().date()
        expenses = Expense.objects.filter(date=today)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class WeeklyExpensesView(APIView):
    def get(self, request):
        one_week_ago = timezone.now() - timedelta(days=7)
        expenses = Expense.objects.filter(date__gte=one_week_ago)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class MonthlyExpensesView(APIView):
    def get(self, request):
        one_month_ago = timezone.now() - timedelta(days=30)
        expenses = Expense.objects.filter(date__gte=one_month_ago)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class SpecificMonthExpensesView(APIView):
    def get(self, request, year, month):
        expenses = Expense.objects.filter(Q(date__year=year) & Q(date__month=month))
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)


class DailyAggregateExpensesView(APIView):
    def get(self, request, year=None, month=None, day=None):
        date = timezone.now().date()
        if year and month and day:
            date = timezone.datetime(year, month, day).date()
        aggregate = Expense.objects.filter(date=date).aggregate(total_amount=Sum('amount'))
        return Response(aggregate)