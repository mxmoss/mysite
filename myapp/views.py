from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import myRecord

def index(request):
  return HttpResponse("Hello, world. You're at the myapp index.")
	
def post_list(request):
    records = myRecord.objects.filter().order_by('created_date')
#    records = myRecord.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'records': records})
