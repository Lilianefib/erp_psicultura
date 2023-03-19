from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.fornecedores.models import Fornecedor



class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_fornecedor')


class FornecedorEdit(UpdateView):
    model = Fornecedor
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_fornecedor')

class FornecedorList(ListView):
    model = Fornecedor
    paginate_by = 10

    def get_queryset(self):
        termo_pesquisa = super(FornecedorList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(razao_social__icontains=search)|
                Q(cnpj__icontains=search)
            )
        else:
            return termo_pesquisa

class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('list_fornecedor')