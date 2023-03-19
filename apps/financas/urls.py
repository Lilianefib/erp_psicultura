from django.urls import path
from apps.financas.views import CustoList, CustoCreate, CustoEdit, CustoDelete, PlanoContaList

urlpatterns = [
    path('', CustoList.as_view(), name='list_custo'),
    path('planocontas', PlanoContaList.as_view(), name='list_planocontas'),
    path('novo', CustoCreate.as_view(), name='create_custo'),
    path('editar/<int:pk>', CustoEdit.as_view(), name='edit_custo'),
    path('deletar/<int:pk>', CustoDelete.as_view(), name='del_custo'),
]