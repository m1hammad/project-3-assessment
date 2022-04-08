from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from main_app.models import Widget
from main_app.forms import WidgetForm

# Create your views here.
class WidgetList(ListView):
    model = Widget
    fields = "__all__"
    template_name = 'widget_list.html'
    
    def get_context_data(self, **kwargs):
        context=super(WidgetList, self).get_context_data(**kwargs)
        context['form']= WidgetForm()
        return context


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
    
    
def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
        number = int(form.data['quantity'])
    # return render('list', {"number": number})
    return redirect('list')