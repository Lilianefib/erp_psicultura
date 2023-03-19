from django.urls import path
from apps.parametros.views import ParametroList, ParametroCreate, ParametroEdit, ParametroDelete


urlpatterns = [
    path('', ParametroList.as_view(), name='list_parametro'),
    path('novo', ParametroCreate.as_view(), name='create_parametro'),
    path('editar/<int:pk>', ParametroEdit.as_view(), name='edit_parametro'),
    path('deletar/<int:pk>', ParametroDelete.as_view(), name='del_parametro'),
]