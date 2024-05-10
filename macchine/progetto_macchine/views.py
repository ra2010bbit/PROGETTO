## views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login
from .models import Machine
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Machine

def home(request):
    return render(request, 'progetto_macchine/home.html')
class MachineListView(ListView):
    model = Machine
    template_name = 'progetto_macchine/pagina.html'
    context_object_name = 'machine_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        machines_list = context['machine_list']
        images_list = []

        for machine in machines_list:
            # Ottieni le immagini associate a ciascuna macchina
            images = machine.machineimage_set.all()
            if images:
                # Se ci sono immagini, aggiungi la prima immagine alla lista
                images_list.append(images.first())
            else:
                # Altrimenti, aggiungi None alla lista
                images_list.append(None)

        context['images'] = images_list
        return context


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'progetto_macchine/detailpagina.html'
    context_object_name = 'machine'

def prive(request):
    return render(request, 'progetto_macchine/prive.html')


def search(request):
    query = request.GET.get('q')
    if query:
        machines = Machine.objects.filter(name__icontains=query)
    else:
        machines = None
    return render(request, 'progetto_macchine/search_results.html', {'machines': machines, 'query': query})




class MachineDetailView(DetailView):
    model = Machine
    template_name = 'progetto_macchine/detailpagina.html'
    context_object_name = 'machine'