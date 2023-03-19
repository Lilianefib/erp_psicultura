from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.financas.models import Custo, PlanoConta


class CustoCreate(CreateView):
    model = Custo
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_custo')


class CustoEdit(UpdateView):
    model = Custo
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_custo')

class CustoList(ListView):
    model = Custo

    def get_queryset(self):
        termo_pesquisa = super(CustoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(descricao__icontains=search)|
                Q(plano_contas__icontains=search)
            )
        else:
            return termo_pesquisa

class PlanoContaList(ListView):
    model = PlanoConta
    template_name = 'planoconta_list.html'

    def get_queryset(self):
        termo_pesquisa = super(PlanoContaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(descricao__icontains=search)|
                Q(codigo__icontains=search)|
                Q(tipo_plano_contas__icontains=search)
            )
        else:
            return termo_pesquisa

class CustoDelete(DeleteView):
    model = Custo
    success_url = reverse_lazy('list_custo')
