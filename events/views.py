from django.views import generic
from django.shortcuts import render
from .models import DefaultEvent

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'events/index.html'

    def get_queryset(self):
        return DefaultEvent.objects.all()

class DetailView(generic.DetailView):
    model = DefaultEvent
    template_name = 'events/detail.html'

def ContactView(request):
    return render(request, 'events/contact.html')

def AboutView(request):
    return render(request, 'events/about.html')