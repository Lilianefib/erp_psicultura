from django.contrib import admin
from .models import Fazenda

#só existe para aparecer no admin o campo personalizado

admin.site.register(Fazenda)

