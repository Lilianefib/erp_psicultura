from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.clientes.models import Cliente



class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_cliente')


class ClienteEdit(UpdateView):
    model = Cliente
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('list_cliente')

class ClienteList(ListView):
    model = Cliente
    paginate_by = 5

    def get_queryset(self):
        termo_pesquisa = super(ClienteList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(nome__icontains=search)
            )
        else:
            return termo_pesquisa

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_cliente')
