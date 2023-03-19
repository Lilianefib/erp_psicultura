from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from apps.parametros.models import Parametro


class ParametroCreate(CreateView):
    model = Parametro
    template_name = 'parametro_form.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_parametro')


class ParametroEdit(UpdateView):
    model = Parametro
    fields = '__all__'
    success_url = reverse_lazy('list_parametro')

class ParametroList(ListView):
    model = Parametro
    template_name = 'parametro_list.html'

    def get_queryset(self):
        termo_pesquisa = super(ParametroList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return termo_pesquisa.filter(
                Q(descricao__icontains=search)|
                Q(natureza__icontains=search)
            )
        else:
            return termo_pesquisa

class ParametroDelete(DeleteView):
    model = Parametro
    success_url = reverse_lazy('list_parametro')
