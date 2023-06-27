from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer

class DailyExpensesView(APIView):
    def get(self, request):
        today = timezone.now().date()
        expenses = Expense.objects.filter(date=today)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
