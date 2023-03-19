from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.insumos.forms import InsumoForm
from apps.insumos.models import Insumo



class InsumoCreate(CreateView):
    model = Insumo
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_insumo')


class InsumoEdit(UpdateView):
    model = Insumo
    fields = '__all__'
    success_url = reverse_lazy('list_insumo')

class InsumoList(ListView):
    model = Insumo
    paginate_by = 10

    def get_queryset(self):
        termo_pesquisa = super(InsumoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(descricao__icontains=search)|
                Q(fornecdor__icontains=search)|
                Q(categoria__icontains=search)|
                Q(marca__icontains=search)
            )
        else:
            return termo_pesquisa


class InsumoDelete(DeleteView):
    model = Insumo
    success_url = reverse_lazy('list_insumo')
