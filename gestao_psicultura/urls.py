from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('fornecedores/', include('apps.fornecedores.urls')),
    path('parametros/', include('apps.parametros.urls')),
    path('fazendas/', include('apps.fazendas.urls')),
    path('financas/', include('apps.financas.urls')),
    path('viveiros/', include('apps.viveiros.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('insumos/', include('apps.insumos.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

