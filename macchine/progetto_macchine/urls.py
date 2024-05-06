from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="progetto_macchine-home"),
    path('pagina/', views.MachineListView.as_view(), name="progetto_macchine-pagina"),
    path('pagina/<int:pk>/', views.MachineDetailView.as_view(), name="progetto_macchine-detailpagina"),
    path('prive/', views.prive,  name='progetto_macchine-prive'),  
    path('search/', views.search, name='search_results'),
    
]
