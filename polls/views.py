from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    data = {'data': Post.objects.filter().latest('created_date')}
    return render(request, 'polls/index.html',data)

class ContactCreateCompleteView(TemplateView):
    template_name = 'contact_create_complete.html'
