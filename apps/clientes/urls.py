from django.urls import path

from apps.clientes.views import ClienteList, ClienteCreate, ClienteEdit, ClienteDelete

urlpatterns = [
    path('', ClienteList.as_view(), name='list_cliente'),
    path('novo', ClienteCreate.as_view(), name='create_cliente'),
    path('editar/<int:pk>', ClienteEdit.as_view(), name='edit_cliente'),
    path('deletar/<int:pk>', ClienteDelete.as_view(), name='del_cliente'),
]