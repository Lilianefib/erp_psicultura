from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.fazendas.models import Fazenda



class FazendaCreate(CreateView):
    model = Fazenda
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_fazenda')


class FazendaEdit(UpdateView):
    model = Fazenda
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_fazenda')

class FazendaList(ListView):
    model = Fazenda
    paginate_by = 5

    def get_queryset(self):
        termo_pesquisa = super(FazendaList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(nome__icontains=search)|
                Q(tipoperfil__icontains=search)
            )
        else:
            return termo_pesquisa

class FazendaDelete(DeleteView):
    model = Fazenda
    success_url = reverse_lazy('list_fazenda')
