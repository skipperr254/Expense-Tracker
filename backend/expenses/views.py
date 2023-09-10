from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Expense
from .serializers import PostSerializer

# Create your views here.
class ExpenseWritePermission(BasePermission):
    message = "Unauthorized"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user

class ExpenseList(generics.ListCreateAPIView, ExpenseWritePermission):
    # permission_classes = [ExpenseWritePermission]
    queryset = Expense.objects.all()
    serializer_class = PostSerializer

# Generic rest framework views
class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView, ExpenseWritePermission):
    permission_classes = [ExpenseWritePermission]
    queryset = Expense.objects.all()
    serializer_class = PostSerializer