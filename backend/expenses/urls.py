from django.urls import path
from .views import ExpenseList, ExpenseDetail

app_name = 'expenses'

urlpatterns = [
    path('<int:pk>/', ExpenseDetail.as_view(), name='detailcreate'),
    path('', ExpenseList.as_view(), name='listcreate'),
]
