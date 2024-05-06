from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Machine, MachineImage

class MachineImageInline(admin.TabularInline):
    model = MachineImage
    extra = 3  # Numero di moduli vuoti da mostrare per aggiungere nuove immagini

class MachineAdmin(admin.ModelAdmin):
    inlines = [MachineImageInline]

admin.site.register(Machine, MachineAdmin)

