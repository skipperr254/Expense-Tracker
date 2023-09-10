from django.test import TestCase
from django.contrib.auth.models import User
from .models import Expense, Category
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class Test_Create_Expense(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        test_category = Category.objects.create(name="Bills")
        test_user1 = User.objects.create_user(
            username="heist1", password="123456789"
        )
        test_expense = Expense.objects.create(
            name="Electricity Bill",
            category=test_category,
            description="Bill for Kenya Power",
            owner=test_user1,
            amount=2000
        )

    def test_expense_(self):
        expense = Expense.objects.get(id=1)
        category = str(Category.objects.get(id=1))
        expense_category = expense.category.name
        user1 = str(User.objects.get(id=1))
        expense_owner = expense.owner.username
        name = expense.name
        description = f'{expense.description}'
        amount = expense.amount

        self.assertEquals(expense_owner, user1)
        self.assertEquals(name, "Electricity Bill")
        self.assertEquals(amount, 2000)
        self.assertEquals(expense_category, category)
        self.assertEquals(description, "Bill for Kenya Power")
        self.assertEquals(str(expense), "Electricity Bill")
        self.assertEquals(str(category), "Bills")


class ExpenseAPITests(APITestCase):
    def test_view_expenses(self):
        url = reverse('expenses:listcreate')
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_create_expense(self):
        test_category = Category.objects.create(name="Bills")
        test_user1 = User.objects.create_user(
            username="heist1", password="123456789"
        )
        data = {
            "name": "Electricity Bill",
            "owner": 1,
            "category": 1,
            "amount": 2000,
            "description": "Kenya Power Monies"
        }
        url = reverse('expenses:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)