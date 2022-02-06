from django.shortcuts import render
from .models import Post
from .models import About
from .models import Member
from .models import Goods

from polls import models
# Create your views here.

def index(request):
    context = {
        'data': Post.objects.filter().latest('created_date'),
        'about' : About.objects.get(id=1),
        'member' : Member.objects.all(),
        'goods' : Goods.objects.all()    
    }
    
    return render(request, 'polls/index.html',context)

