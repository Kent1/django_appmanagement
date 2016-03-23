from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from .models import Application, Scope


class ApplicationCreateView(CreateView):
    model = Application
    fields = ['name', 'description', 'application_file', 'scope']
    success_url = reverse_lazy('list')


class ApplicationListView(ListView):
    model = Application
    fields = ['name', 'description', 'application_file', 'scope']

    def get_queryset(self):
        queryset = super(ListView, self).get_queryset()
        scope = self.request.GET.get('scope')
        if scope == 'public':
            return Application.objects.filter(scope=Scope.PUBLIC)
        elif scope == 'private':
            return Application.objects.filter(scope=Scope.PRIVATE)
        return queryset


class ApplicationDetailView(DetailView):
    model = Application


class ApplicationEditView(UpdateView):
    model = Application
    fields = ['name', 'description', 'application_file', 'scope']
    success_url = reverse_lazy('list')
