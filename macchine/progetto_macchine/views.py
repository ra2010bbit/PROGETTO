## views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login
from .models import Machine
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'progetto_macchine/home.html')


from django.views.generic import ListView
from django.core.paginator import Paginator

class MachineListView(ListView):
    model = Machine
    template_name = 'progetto_macchine/pagina.html'
    context_object_name = 'progetto_macchina'
    paginate_by = 10  # Numero di macchine per pagina

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')  # Ordina per ID o un altro campo appropriato
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        machines_list = context['progetto_macchina']
        paginator = Paginator(machines_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
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


from django.views.generic import DetailView
from .models import Machine

class MachineDetailView(DetailView):
    model = Machine
    template_name = 'progetto_macchine/detailpagina.html'
    context_object_name = 'machine'