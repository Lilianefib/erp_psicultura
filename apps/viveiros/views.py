from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.viveiros.models import Viveiro


class ViveiroCreate(CreateView):
    model = Viveiro
    fields = (
        'descricao',
        'tipo',
        'area',
        'un_medida',
        'fator_densidade',
        'setor',
        'ativo',
    )

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_viveiro')


class ViveiroEdit(UpdateView):
    model = Viveiro
    fields = '__all__'
    success_url = reverse_lazy('list_viveiro')

class ViveiroList(ListView):
    model = Viveiro
    paginate_by = 5

    def get_queryset(self):
        termo_pesquisa = super(ViveiroList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(descricao__icontains=search)|
                Q(tipo__icontains=search)
            )
        else:
            return termo_pesquisa


class ViveiroDelete(DeleteView):
    model = Viveiro
    success_url = reverse_lazy('list_viveiro')
