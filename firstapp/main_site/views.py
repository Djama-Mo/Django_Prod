from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Table
from .forms import TableForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    tables = Table.objects.all()
    tables_dic = {'title': 'Main page',
                  'description': tables}
    return render(request, 'main_site/index.html', tables_dic)


class TableListView(ListView):
    model = Table
    template_name = 'main_site/index.html'
    context_object_name = 'description'


class TableDetailView(DetailView):
    model = Table


class TableCreateView(LoginRequiredMixin, CreateView):
    model = Table
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        table = self.get_object()
        if table.user == self.request.user:
            return True
        return False


class TableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Table
    success_url = '/'

    def test_func(self):
        table = self.get_object()
        if table.user == self.request.user:
            return True
        return False
