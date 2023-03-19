from django.urls import path

from apps.insumos.views import InsumoList, InsumoCreate, InsumoEdit, InsumoDelete

urlpatterns = [
    path('', InsumoList.as_view(), name='list_insumo'),
    path('novo', InsumoCreate.as_view(), name='create_insumo'),
    path('editar/<int:pk>', InsumoEdit.as_view(), name='edit_insumo'),
    path('deletar/<int:pk>', InsumoDelete.as_view(), name='del_insumo'),
]