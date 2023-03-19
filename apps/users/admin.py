from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from apps.users.models import Usuario

admin.site.register(Usuario, auth_admin.UserAdmin)
