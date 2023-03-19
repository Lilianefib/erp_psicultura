from django.urls import path

from apps.viveiros import views
from apps.viveiros.views import ViveiroList, ViveiroCreate, ViveiroEdit, ViveiroDelete

urlpatterns = [
    path('', ViveiroList.as_view(), name='list_viveiro'),
    path('novo', ViveiroCreate.as_view(), name='create_viveiro'),
    path('editar/<int:pk>', ViveiroEdit.as_view(), name='edit_viveiro'),
    path('deletar/<int:pk>', ViveiroDelete.as_view(), name='del_viveiro'),

]