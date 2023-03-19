from django.urls import path
from apps.fornecedores.views import FornecedorCreate, FornecedorEdit, \
    FornecedorList, FornecedorDelete

urlpatterns = [
    path('', FornecedorList.as_view(), name='list_fornecedor'),
    path('novo', FornecedorCreate.as_view(), name='create_fornecedor'),
    path('editar/<int:pk>', FornecedorEdit.as_view(), name='edit_fornecedor'),
    path('deletar/<int:pk>', FornecedorDelete.as_view(), name='del_fornecedor'),
]