from django.contrib import admin

from .models import Cursos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'curso', 'email','tiempo')
    search_fields = ('nombre', 'curso', 'email','tiempo')
    date_hierarchy = 'created'
    list_filter = ('curso','tiempo')

admin.site.register(Cursos, AdministrarModelo)
