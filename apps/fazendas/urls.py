from django.urls import path
from apps.fazendas.views import FazendaList, FazendaCreate, \
    FazendaEdit, FazendaDelete

urlpatterns = [
    path('', FazendaList.as_view(), name='list_fazenda'),
    path('novo', FazendaCreate.as_view(), name='create_fazenda'),
    path('editar/<int:pk>', FazendaEdit.as_view(), name='edit_fazenda'),
    path('deletar/<int:pk>', FazendaDelete.as_view(), name='del_fazenda'),

]